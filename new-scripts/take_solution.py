import csv
import os
import json
import re
import pathlib
import textwrap
from typing import Optional

MODELS = {
    'GPT-4':              'GPT-4-Turbo',
    'GPT-3.5':            'GPT-3.5-Turbo',
    'WizardCoder':        'WizardCoder-15B-V1.0',
}
STRATEGY = "H_greedy"
STRATEGY_KEY = "H(greedy)"  # format used as key in detailed_result.json

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
FILE_SUFIX = f"_class_{STRATEGY}"

def isNotToAnalisyze(file_name: str) -> bool:
    not_have_sufix = FILE_SUFIX not in file_name
    not_in_models = file_name.replace(f"{FILE_SUFIX}.json", '') not in MODELS.values()
    return not_have_sufix or not_in_models

def get_task_status(task_data: dict) -> tuple:
    test_class = task_data.get("TestClass", {})
    class_each = test_class.get("ClassEachTestResult", [])
    class_result = class_each[0] if class_each else "class_fail"

    if class_result == "class_success":
        return "Success", 1.0
    elif class_result == "class_partial_success":
        method_entries = {k: v for k, v in task_data.items() if k != "TestClass"}
        total = len(method_entries)
        passed = sum(1 for v in method_entries.values() if isinstance(v, dict) and v.get("success", 0) > 0)
        pass_value = passed / total if total > 0 else 0.0
        return "PartialSuccess", pass_value
    else:
        for test_name, test_data in task_data.items():
            if test_name == "TestClass":
                continue
            if isinstance(test_data, dict) and test_data.get("error", 0) > 0:
                return "error", 0.0
        return "Fail", 0.0

def read_detailed_results(json_path: pathlib.Path) -> dict:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    results = {}
    for short_name, full_name in MODELS.items():
        key = f"{short_name}_{STRATEGY_KEY}"
        if key not in data:
            print(f"Warning: key '{key}' not found in detailed_result.json")
            continue
        results[full_name] = {}
        for task_key, task_data in data[key].items():
            task_id = task_key.replace("SE-Eval_", "ClassEval_")
            status, pass_value = get_task_status(task_data)
            results[full_name][task_id] = {"pass_value": pass_value, "status": status}
    return results

def save_results_csv(results: dict, output_path: pathlib.Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["model", "strategy", "task", "class_name", "pass_value", "status"])
        for model, tasks in results.items():
            for task, info in tasks.items():
                writer.writerow([model, STRATEGY, task, info.get("class_name", ""), info["pass_value"], info["status"]])

def _best_fence(text: str) -> str:
    """Return the largest python-tagged fence; fall back to the largest untagged fence."""
    python_fences = re.findall(r'```python\n?(.*?)\n?```', text, flags=re.DOTALL)
    if python_fences:
        return max(python_fences, key=len)
    plain_fences = re.findall(r'```\n?(.*?)\n?```', text, flags=re.DOTALL)
    return max(plain_fences, key=len) if plain_fences else ""


def clean_model_output(model_predict: str) -> str:
    text = model_predict

    # WizardCoder pattern: ### Instruction: <skeleton> ### Response: <prose + code>
    # The response section may contain a fenced block with the actual implementation;
    # fall back to the instruction skeleton only when the response has no fence.
    if '### Response:' in text:
        resp_idx = text.find('### Response:')
        response_section = text[resp_idx + len('### Response:'):]
        best = _best_fence(response_section)
        if best and 'class ' in best:
            return textwrap.dedent(best).strip()
        # Unclosed fence (truncated output): extract from ```python to end of text.
        # Only apply when the fence has no closing ``` — if it does, it was already
        # handled by _best_fence above (just didn't contain a class definition).
        unclosed = re.search(r'```python\n?(.*)', response_section, flags=re.DOTALL)
        if unclosed:
            content = unclosed.group(1)
            if '```' not in content and 'class ' in content:
                return textwrap.dedent(content).strip()
        # No fence with class definition — fall back to the instruction skeleton
        instr_idx = text.find('### Instruction:')
        start = (instr_idx + len('### Instruction:')) if instr_idx != -1 else 0
        code_section = text[start:resp_idx]
        code_section = re.sub(r'Please complete the class[^\n]*\n', '', code_section)
        return textwrap.dedent(code_section).strip()

    # GPT-4 pattern: prose preamble + ```python\n<code>\n``` + prose postamble
    # Extract ONLY the fenced content — the largest fence is the complete implementation
    best = _best_fence(text)
    if best:
        return textwrap.dedent(best).strip()

    # GPT-3.5 / fallback: prose prefix followed by Python code
    # Discard leading lines until the first recognisable Python token
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r'^(import |from |class |def |@|#)', line.strip()):
            return textwrap.dedent('\n'.join(lines[i:])).strip()

    # No Python code found at all — return empty string so the caller can skip
    return ""

def save_file(content: str, content_path: pathlib.Path, file_name: str):
    content_path = pathlib.Path(content_path)
    content_path.mkdir(parents=True, exist_ok=True)
    file = content_path / file_name
    with file.open("w", encoding="utf-8") as f:
        f.write(content)

def main():
    # Part 1: read detailed_result.json and save CSV
    json_path = PROJECT_ROOT / "new-scripts" / "output" / "result" / "detailed_result.json"
    csv_output = PROJECT_ROOT / "new-scripts" / "output" / "results" / "pass_results.csv"

    results = read_detailed_results(json_path)

    # Part 2: extract and sanitize predictions from model_output_v1.0.0
    input_dir = PROJECT_ROOT / "new-scripts" / "output" / "model_output_v1.0.0"
    solutions_dir = PROJECT_ROOT / "new-scripts" / "output" / "solutions"
    originals_dir = PROJECT_ROOT / "new-scripts" / "output" / "solutions" / "originals"

    for file_name in os.listdir(input_dir):
        if isNotToAnalisyze(file_name):
            continue

        model_name = file_name.replace(f"{FILE_SUFIX}.json", "")
        model_json_path = input_dir / file_name
        print(f"Processing {file_name}")

        with open(model_json_path, encoding="utf-8") as f:
            tasks = json.load(f)

        for task in tasks:
            task_id = task["task_id"]
            class_name = task["class_name"]

            # enrich CSV results with class_name
            if model_name in results and task_id in results[model_name]:
                results[model_name][task_id]["class_name"] = class_name

            predicts = task.get("predict", [])
            if not predicts:
                continue
            
            # save on originals folder
            save_file(predicts[0], originals_dir / model_name, f"{class_name}.py")
            
            cleaned = clean_model_output(predicts[0])
            if not cleaned:
                print(f"  Warning: no Python code found for {model_name}/{class_name}, saving empty file.")
            save_file(cleaned, solutions_dir / model_name, f"{class_name}.py")

    save_results_csv(results, csv_output)
    print(f"CSV saved to {csv_output}")
    print("Done.")


if __name__ == "__main__":
    main()
