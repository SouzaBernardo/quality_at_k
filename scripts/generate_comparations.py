import difflib
from pathlib import Path

SOLUTIONS_DIR = Path(__file__).parent.parent / "output" / "solutions"
ORIGINALS_DIR = SOLUTIONS_DIR / "originals"
VALIDATION_DIR = Path(__file__).parent.parent / "output" / "validation"

DIFFER = difflib.HtmlDiff(wrapcolumn=100)


def _html_css() -> str:
    dummy = DIFFER.make_file([], [])
    start = dummy.index("<style")
    end = dummy.index("</style>") + len("</style>")
    return dummy[start:end]


# ── HTML ──────────────────────────────────────────────────────────────────────

def generate_html(llm: str, llm_dir: Path, original_dir: Path) -> None:
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    output_path = VALIDATION_DIR / f"comparation-{llm}.html"
    toc_items: list[str] = []
    sections: list[str] = []

    for py_file in sorted(llm_dir.glob("*.py")):
        name = py_file.name
        anchor = name.replace(".", "_")
        cleaned = py_file.read_text(encoding="utf-8").splitlines()

        original_path = original_dir / name
        if not original_path.exists():
            toc_items.append(f'<li><a href="#{anchor}">{name}</a> <em>(original not found)</em></li>')
            sections.append(f'<h2 id="{anchor}">{name}</h2><p><em>Original file not found.</em></p>')
            continue

        original = original_path.read_text(encoding="utf-8").splitlines()

        if original == cleaned:
            toc_items.append(f'<li><a href="#{anchor}">{name}</a> <em>(no changes)</em></li>')
            sections.append(f'<h2 id="{anchor}">{name}</h2><p><em>No changes.</em></p>')
            continue

        table = DIFFER.make_table(
            original,
            cleaned,
            fromdesc=f"originals/{llm}/{name}",
            todesc=f"{llm}/{name}",
            context=False,
        )
        toc_items.append(f'<li><a href="#{anchor}">{name}</a></li>')
        sections.append(f'<h2 id="{anchor}">{name}</h2>\n{table}')

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Comparation: {llm}</title>
{_html_css()}
<style>
  body {{ font-family: monospace; padding: 1rem 2rem; }}
  h1, h2, #toc strong {{ font-family: sans-serif; }}
  h2 {{ margin-top: 2rem; border-top: 1px solid #ccc; padding-top: 0.5rem; }}
  table.diff {{ width: 100%; }}
  #toc {{ background: #f9f9f9; border: 1px solid #ddd; padding: 1rem 1.5rem;
          display: inline-block; margin-bottom: 2rem; }}
  #toc ul {{ margin: 0.25rem 0; padding-left: 1.25rem; }}
</style>
</head>
<body>
<h1>Comparation: {llm}</h1>
<nav id="toc">
  <strong>Table of contents</strong>
  <ul>{''.join(toc_items)}</ul>
</nav>
{''.join(sections)}
</body>
</html>"""

    output_path.write_text(page, encoding="utf-8")
    print(f"Written: {output_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    llm_dirs = [
        d for d in sorted(SOLUTIONS_DIR.iterdir())
        if d.is_dir() and d.name != "originals"
    ]
    if not llm_dirs:
        print("No LLM directories found.")
        return
    for llm_dir in llm_dirs:
        llm = llm_dir.name
        original_dir = ORIGINALS_DIR / llm
        generate_html(llm, llm_dir, original_dir)


if __name__ == "__main__":
    main()
