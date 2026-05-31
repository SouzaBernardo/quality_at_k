import subprocess
import sys
import pathlib

SCRIPTS_DIR = pathlib.Path(__file__).parent

PIPELINE = [
    "merge_sonar_metrics.py",
    "prioritize_duplicates.py",
    "aggregate_fqs.py",
]


def run(script: str) -> None:
    print(f"\n{'='*50}")
    print(f"Running {script}")
    print('='*50)
    result = subprocess.run(
        [sys.executable, SCRIPTS_DIR / script],
        cwd=SCRIPTS_DIR,
    )
    if result.returncode != 0:
        print(f"\nERROR: {script} failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def main() -> None:
    for script in PIPELINE:
        run(script)
    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
