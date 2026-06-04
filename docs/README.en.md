# Quality@K — Static Code Quality Analysis of LLM-Generated Code

> 🇧🇷 [Leia em Português](../README.md)

This repository contains the static analysis pipeline used in the thesis *"Evaluating the Code Quality of Large Language Model Outputs"*. The goal is to investigate whether functionally correct code (as measured by Pass@k on the ClassEval benchmark) also exhibits good structural quality, assessed via SonarQube.

## Context

The [ClassEval](https://github.com/FudanSELab/ClassEval) benchmark evaluates LLMs on generating complete Python classes across 100 tasks. This work analyzes **11 models × 3 strategies + GroundTruth = 34 groups**:

| Model | Profile |
|-------|---------|
| GPT-4-Turbo | High performance |
| GPT-3.5-Turbo | High performance |
| WizardCoder-15B-V1.0 | High performance |
| starcoder-instruct-15B | Medium performance |
| instruct-codegen-16B | Medium performance |
| Vicuna | Medium performance |
| ChatGLM | Medium performance |
| codegeex2-6b | Low performance |
| incoder | Low performance |
| santacoder-1.1B | Low performance |
| PolyCoder-2.7B | Low performance |
| GroundTruth | Human reference (ClassEval) |

### Generation Strategies

| Code | Strategy | Description |
|------|----------|-------------|
| `H` | Holistic | Generates the full class at once |
| `I` | Incremental | Builds method by method, feeding the previous result as context |
| `C` | Compositional | Builds method by method independently, without prior context |

### Collected Metrics

- **Cognitive Complexity** — mental effort required to understand the code
- **Cyclomatic Complexity** — number of independent execution paths
- **Code Smells** — indicators of poor practices that impact maintainability
- **SQALE Index** — accumulated technical debt in minutes (SonarQube)
- **Quality@1 (FQS)** — metric proposed in this work, combining Pass@1 and LOC-normalized technical debt

## Prerequisites

- [Docker](https://www.docker.com/) installed and running
- `output/ClassEval_output/` populated with raw ClassEval files (model output JSONs and `detailed_result.json`)

## Running SonarQube

The image already contains all analyzed projects, with metrics and users pre-configured. Just run:

```bash
docker compose up
```

SonarQube will be available at [http://localhost:9000](http://localhost:9000).

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `sonarLike@21` |

> On the first startup, SonarQube may take a few minutes to rebuild its internal search index from the database. Wait until the interface is fully available.

## Quality@1 Pipeline

### Formula

```
Quality@1(t) = Pass@1(t) × (1 − min(1, β × SQALE_Index(t) / NCLOC(t)))
```

Where `Pass@1(t) ∈ {0, 1}`, `β = 0.1`, `SQALE_Index` is the technical debt in minutes (SonarQube), and `NCLOC` is the number of non-commented lines of code.

### How to run

With Python 3 and pandas installed:

```bash
python3 scripts/pipeline.py
```

Steps executed automatically:

| Step | Script | Description |
|------|--------|-------------|
| 1 | `take_solution.py` | Extracts and sanitizes solutions from ClassEval JSONs; generates `pass_results.csv` |
| 2 | `extract_sonar_metrics.py` | Extracts aggregated metrics per project via SonarQube API |
| 3 | `extract_all_sonar_metrics_per_file.py` | Extracts per-file metrics for all projects via SonarQube API |
| 4 | `merge_sonar_metrics.py` | Merges raw CSVs + `pass_results.csv`, computes FQS per task |
| 5 | `aggregate_results.py` | Aggregates FQS by `(model, strategy, status)` |

After the pipeline, diagnostic scripts run automatically:

| Script | Description |
|--------|-------------|
| `verify.py` | Validates count (100 classes/model), detects Markdown contamination, AST errors, and mismatches between `combined_sonar_metrics.csv` and `pass_results.csv` |
| `generate_comparations.py` | Generates HTML diffs (original vs. sanitized) per model in `output/validation/` |

### Outputs

All files are generated under `output/`:

| File | Description |
|------|-------------|
| `output/solutions/{model}/*.py` | Sanitized solutions per model |
| `output/solutions/originals/{model}/*.py` | Raw model responses |
| `output/results/raw/sonar_metrics*.csv` | Raw SonarQube CSVs — per-file metrics |
| `output/results/pass_results.csv` | Input: mapping `(model, class)` → `pass@1` + status |
| `output/results/combined_sonar_metrics.csv` | Main output: SonarQube metrics + FQS per task |
| `output/results/aggregated_results.csv` | Mean FQS by `(model, strategy, status)` |
| `output/validation/comparation-{llm}.html` | HTML diffs: original vs. sanitized per model |

---

## Re-running the Analysis

If you want to resubmit all projects to SonarQube from scratch:

```bash
# make sure SonarQube is running
docker compose up -d

./scripts/run_sonar.sh
```

The script submits each project to SonarQube via `sonar-scanner`, using the pre-configured authentication tokens.

## Repository Structure

```
.
├── compose.yaml                              # Starts SonarQube with the pre-populated image
├── scripts/
│   ├── pipeline.py                           # Runs the full Quality@1 pipeline
│   │
│   ├── # — Extraction (SonarQube API) —
│   ├── extract_all_sonar_metrics_per_file.py # Extracts per-file metrics for all projects
│   ├── extract_sonar_metrics.py              # Extracts aggregated metrics per project
│   │
│   ├── # — Main pipeline —
│   ├── take_solution.py                      # Extracts and sanitizes solutions from ClassEval JSONs
│   ├── merge_sonar_metrics.py                # Merges raw CSVs + computes FQS per task
│   ├── aggregate_results.py                  # Aggregates FQS by (model, strategy, status)
│   ├── compute_fqs.py                        # Pure function implementing the Quality@1 formula
│   ├── sort_csv.py                           # Sorts a CSV by (model, strategy, file)
│   │
│   ├── # — Diagnostics —
│   ├── verify.py                             # Validates solutions and cross-checks metrics
│   ├── generate_comparations.py             # Generates HTML diffs original vs sanitized per model
│   │
│   └── # — SonarQube —
│       ├── run_sonar.sh                      # Re-submits all projects to SonarQube
│       ├── setup_sonar_projects.sh           # Creates projects and tokens in SonarQube
│       └── delete_sonar_projects.sh          # Removes projects from SonarQube
│
└── output/
    ├── ClassEval_output/                     # Input: raw ClassEval files (pre-existing)
    │   ├── model_output_v1.0.0/             # Model output JSONs
    │   └── result/
    │       └── detailed_result.json
    ├── solutions/                            # Generated by take_solution.py
    │   ├── {model}/
    │   │   └── *.py                         # Sanitized solutions
    │   └── originals/
    │       └── {model}/
    │           └── *.py                     # Raw model responses
    ├── results/                             # Generated by the pipeline
    │   ├── raw/
    │   │   └── sonar_metrics*.csv           # Per-file raw metrics
    │   ├── pass_results.csv                 # (model, class) → pass@1 + status
    │   ├── combined_sonar_metrics.csv       # Main output: metrics + FQS per task
    │   └── aggregated_results.csv           # Mean FQS by (model, strategy, status)
    └── validation/                          # Generated by generate_comparations.py
        └── comparation-{llm}.html
```

## Rebuilding the Docker Image

If you need to publish a new version of the image after new analyses:

```bash
# 1. Start SonarQube and run the analyses
docker compose up -d
./scripts/run_sonar.sh

# 2. Extract data from the running container
docker cp quality-sonarqube-1:/opt/sonarqube/data ./sonar-data/sonarqube-data
docker cp quality-sonarqube-1:/opt/sonarqube/extensions ./sonar-data/sonarqube-extensions

# 3. Rebuild and publish
docker build -t beposs/class_eval_sonar:latest .
docker push beposs/class_eval_sonar:latest
```

> The `sonar-data/` folder is listed in `.gitignore` — it is generated locally only during the image build.
