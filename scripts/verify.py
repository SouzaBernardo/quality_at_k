import ast
import csv
import os
import re
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
SOLUTIONS_DIR = PROJECT_ROOT / "output" / "solutions"
CSV_PATH = PROJECT_ROOT / "output" / "results" / "pass_results.csv"
COMBINED_CSV = PROJECT_ROOT / "output" / "results" / "combined_sonar_metrics.csv"

# Unambiguous non-Python syntax markers — checked before AST to keep it fast
_INLINE_MARKERS = re.compile(r'```|~~~|^###\s', re.MULTILINE)

# Files confirmed via manual inspection to be model generation errors (e.g. unclosed
# docstrings), not markdown contamination. The detection logic correctly sees prose
# outside a string, but the root cause is the model forgetting a closing """.
_KNOWN_MODEL_ERRORS: set[tuple[str, str]] = {
    ("WizardCoder-15B-V1.0", "CalendarUtil.py"),
}


def _is_prose_sentence(line: str) -> bool:
    """True if the syntax-error line looks like natural language, not broken Python."""
    s = line.strip()
    if len(s) < 10 or not s[0].isupper():
        return False
    words = s.split()
    if len(words) < 3:
        return False
    # Prose has few Python-specific operator characters relative to word count
    python_ops = sum(1 for c in s if c in '=(){}[]@;')
    return python_ops <= len(words) // 2


def has_markdown_text(code: str, model: str, task: str) -> tuple[bool, str]:
    if _INLINE_MARKERS.search(code):
        return True, f"{model} / {task}"
    try:
        ast.parse(code)
        return False, ""
    except SyntaxError as e:
        if e.lineno is None:
            return False, ""
        lines = code.splitlines()
        error_line = lines[e.lineno - 1] if e.lineno <= len(lines) else ""
        if _is_prose_sentence(error_line):
            return True, f"{model} / {task}"
    return False, ""


def count_total_codes(model: str, model_data: list[str], reference=None) -> int:
    size = len(model_data)
    if size != 100:
        print(f"  [FAIL] model '{model}' has {size} classes (expected 100).")
        if reference:
            missing = sorted(reference - set(model_data))
            for f in missing:
                print(f"    missing: {f}")
    return size


def load_csv_statuses(csv_path: pathlib.Path) -> dict[tuple[str, str], str]:
    statuses: dict[tuple[str, str], str] = {}
    with csv_path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            statuses[(row["model"], row["class_name"])] = row["status"]
    return statuses


def _has_any_implementation(code: str) -> bool:
    """True if at least one method/function has a non-stub body (beyond docstring/pass/...)."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return True  # can't tell, assume not a skeleton
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body = list(node.body)
            # skip leading docstring
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
                body = body[1:]
            for stmt in body:
                is_pass = isinstance(stmt, ast.Pass)
                is_ellipsis = (
                    isinstance(stmt, ast.Expr)
                    and isinstance(stmt.value, ast.Constant)
                    and stmt.value.value is ...
                )
                if not (is_pass or is_ellipsis):
                    return True
    return False


def check_truncated_originals(
    models: list[str], solutions_dir: pathlib.Path
) -> list[tuple[str, str]]:
    """Return (model, filename) pairs where original has a truncated fence but cleaned is a skeleton."""
    originals_dir = solutions_dir / "originals"
    if not originals_dir.exists():
        return []
    issues: list[tuple[str, str]] = []
    for model in models:
        orig_dir = originals_dir / model
        if not orig_dir.exists():
            continue
        for orig_file in sorted(orig_dir.glob("*.py")):
            text = orig_file.read_text(encoding="utf-8")
            if "### Response:" not in text:
                continue
            resp_idx = text.find("### Response:")
            response_section = text[resp_idx + len("### Response:"):]
            # Skip if there's a complete fence with class (handled by _best_fence)
            complete = re.findall(r'```python\n?(.*?)\n?```', response_section, flags=re.DOTALL)
            if any("class " in f for f in complete):
                continue
            # Check for unclosed fence with class (same guard as clean_model_output:
            # only count as unclosed when no ``` appears after the opening)
            unclosed = re.search(r'```python\n?(.*)', response_section, flags=re.DOTALL)
            if not unclosed:
                continue
            content = unclosed.group(1)
            if '```' in content or 'class ' not in content:
                continue
            # The original had truncated code — verify cleaned solution is not a skeleton
            clean_file = solutions_dir / model / orig_file.name
            if clean_file.exists() and not _has_any_implementation(clean_file.read_text(encoding="utf-8")):
                issues.append((model, orig_file.name))
    return issues


def check_combined_metrics(combined_csv: pathlib.Path, pass_csv: pathlib.Path) -> bool:
    if not combined_csv.exists():
        print(f"  [SKIP] {combined_csv.name} not found, skipping combined metrics check.")
        return True

    pass_lookup: dict[tuple[str, str], dict] = {}
    with pass_csv.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pass_lookup[(row["model"], row["class_name"])] = {
                "status": row["status"],
                "pass_value": float(row["pass_value"]),
            }

    mismatches: list[str] = []
    with combined_csv.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            model = row["model"]
            if model == "GroundTruth":
                continue
            base_task = row["base_task"]
            expected = pass_lookup.get((model, base_task))
            if expected is None:
                mismatches.append(f"    [MISSING] {model} / {base_task}: not found in pass_results.csv")
                continue
            combined_status = row["status"]
            combined_pass_val = float(row["pass_val"]) if row["pass_val"] else 0.0
            if combined_status != expected["status"]:
                mismatches.append(
                    f"    [STATUS] {model} / {base_task}: combined={combined_status!r} expected={expected['status']!r}"
                )
            if abs(combined_pass_val - expected["pass_value"]) > 1e-9:
                mismatches.append(
                    f"    [PASS_VAL] {model} / {base_task}: combined={combined_pass_val} expected={expected['pass_value']}"
                )

    if mismatches:
        print(f"  [COMBINED METRICS MISMATCH] {len(mismatches)} issue(s):")
        for m in mismatches:
            print(m)
        return False
    return True


def main():
    print("Starting verification process...")

    statuses = load_csv_statuses(CSV_PATH)

    models = sorted(d for d in os.listdir(SOLUTIONS_DIR)
                    if (SOLUTIONS_DIR / d).is_dir() and d != "originals")

    # Build a reference file set from the first model that has exactly 100 classes
    reference: set[str] = set()
    for m in models:
        files = [f for f in os.listdir(SOLUTIONS_DIR / m) if f.endswith(".py")]
        if len(files) == 100:
            reference = set(files)
            break

    all_ok = True

    for model in models:
        model_dir = SOLUTIONS_DIR / model
        files = [f for f in os.listdir(model_dir) if f.endswith(".py")]

        count = count_total_codes(model, files, reference)
        if count != 100:
            all_ok = False

        contaminated = []
        ast_mismatches = []
        for file_name in files:
            code = (model_dir / file_name).read_text(encoding="utf-8")

            if (model, file_name) not in _KNOWN_MODEL_ERRORS:
                found, _ = has_markdown_text(code, model, file_name)
                if found:
                    contaminated.append(file_name)
                    all_ok = False

            try:
                ast.parse(code)
            except SyntaxError:
                class_name = file_name.removesuffix(".py")
                csv_status = statuses.get((model, class_name))
                if csv_status != "error":
                    ast_mismatches.append((file_name, csv_status))
                    all_ok = False

        if contaminated:
            print(f"  [CONTAMINATION] {model}: {len(contaminated)} file(s)")
            for f in sorted(contaminated):
                print(f"    - {f}")

        if ast_mismatches:
            print(f"  [AST/CSV MISMATCH] {model}: {len(ast_mismatches)} file(s) fail AST but CSV status != 'error'")
            for f, s in sorted(ast_mismatches):
                print(f"    - {f}  (CSV status: {s!r})")

    truncated_issues = check_truncated_originals(models, SOLUTIONS_DIR)
    if truncated_issues:
        print(f"  [TRUNCATED FENCE / SKELETON] {len(truncated_issues)} file(s) have truncated originals but skeleton solutions:")
        for model, fname in truncated_issues:
            print(f"    - {model} / {fname}")
        all_ok = False

    if not check_combined_metrics(COMBINED_CSV, CSV_PATH):
        all_ok = False

    if all_ok:
        print("All checks passed.")


if __name__ == "__main__":
    main()
