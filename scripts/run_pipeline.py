import subprocess
import sys
import pathlib

SCRIPTS_DIR = pathlib.Path(__file__).parent
ROOT = SCRIPTS_DIR.parent

# (type, path_relative_to_root)
PIPELINE = [
    ("sh",  "run_sonar.sh"),
    ("py",  "scripts/extract_all_sonar_metrics_per_file.py"),
    ("py",  "scripts/extract_sonar_metrics.py"),
    ("py",  "scripts/merge_sonar_metrics.py"),
    ("py",  "scripts/aggregate_fqs.py"),
]

CHECKS = [
    ("py",  "scripts/count_per_model_strategy.py"),
    ("py",  "scripts/check_pass_val.py"),
    ("py",  "scripts/find_duplicates.py"),
]


def run(kind: str, rel_path: str) -> None:
    path = ROOT / rel_path
    print(f"\n{'='*50}")
    print(f"Running {rel_path}")
    print('='*50)

    if kind == "sh":
        cmd = ["bash", str(path)]
    else:
        cmd = [sys.executable, str(path)]

    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        print(f"\nERROR: {rel_path} failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def main() -> None:
    for kind, rel_path in PIPELINE:
        run(kind, rel_path)

    print("\n" + "="*50)
    print("Pipeline complete. Running checks...")
    print("="*50)

    for kind, rel_path in CHECKS:
        run(kind, rel_path)

    print("\nAll done.")


if __name__ == "__main__":
    main()
