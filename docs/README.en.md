# Quality@K — Static Code Quality Analysis of LLM-Generated Code

> 🇧🇷 [Leia em Português](../README.md)

This repository contains the static analysis pipeline used in the thesis *"Evaluating the Code Quality of Large Language Model Outputs"*. The goal is to investigate whether functionally correct code (as measured by Pass@k on the ClassEval benchmark) also exhibits good structural quality, assessed via SonarQube.

## Context

The [ClassEval](https://github.com/FudanSELab/ClassEval) benchmark evaluates LLMs on generating complete Python classes across 100 tasks. This work selects the two performance extremes from the benchmark:

| Model | Profile | Pass@1 (class-level) |
|-------|---------|----------------------|
| GPT-4-Turbo | Best performer | 37.6% |
| PolyCoder-2.7B | Worst performer | 1.4% |

Both are compared against the **Ground Truth** — human-written implementations provided by ClassEval itself.

### Generation Strategies

Each model was evaluated under three generation strategies defined by ClassEval:

| Code | Strategy | Description |
|------|----------|-------------|
| `H` | Holistic | Generates the full class at once |
| `I` | Incremental | Builds method by method, feeding the previous result as context |
| `C` | Compositional | Builds method by method independently, without prior context |

### Decoding Configurations

| Suffix | Mode | Samples per task |
|--------|------|------------------|
| `greedy` | Greedy (T=0) | 1 |
| `t0.2` | Nucleus Sampling (T=0.2) | 5 |

The directories in `data/` combine these dimensions — for example, `GPT-4-Turbo_method_C_greedy` represents GPT-4-Turbo with the Compositional strategy and greedy decoding.

### Collected Metrics

- **Cognitive Complexity** — mental effort required to understand the code
- **Cyclomatic Complexity** — number of independent execution paths
- **Code Smells** — indicators of poor practices that impact maintainability
- **Quality@k** — metric proposed in this work, combining the three above into a LOC-normalized score

## Prerequisites

- [Docker](https://www.docker.com/) installed and running

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

## Re-running the Analysis

If the files in `data/` are changed or you want to reprocess the analysis from scratch:

```bash
# make sure SonarQube is running
docker compose up -d

./run_sonar.sh
```

The script submits each project to SonarQube via `pysonar`, using the pre-configured authentication tokens.

## Origin of the `data/` Directory

The `data/` directory is the final output of a two-step pipeline built on top of the raw files from the [ClassEval](https://github.com/FudanSELab/ClassEval) benchmark. The full flow is:

```
ClassEval (output/model_output_v1.0.0/)
        │
        │  scripts/take_solution.py
        ▼
classEval_output/          ← intermediate artifact (in this repository)
        │
        │  scripts/group_filtered_solutions.py
        ▼
data/                      ← SonarQube input
```

### Step 1 — `scripts/take_solution.py`

Reads the raw JSONs from `output/model_output_v1.0.0/` in ClassEval, extracts the `predict` field from each generation and:

- Strips Markdown artifacts and natural language from model responses (` ```python ` blocks, explanations, notes)
- Cross-references each generation with `output/result/detailed_result.json` to obtain the unit test outcome (`Success`, `PartialSuccess`, `Fail`, `Error`)
- Names each file using the pattern `<Class><index><Status>.py` — e.g., `AccessGatewayFilter0Error.py`
- Saves both the original and sanitized versions separately

The output is stored in `classEval_output/`, with the following structure:

```
classEval_output/
└── GPT-4-Turbo_class_H_greedy/
    └── AccessGatewayFilter/
        ├── filtered/
        │   └── AccessGatewayFilter0Error.py   ← sanitized code
        └── original/
            └── AccessGatewayFilter0Error.py   ← raw model response
```

### Step 2 — `scripts/group_filtered_solutions.py`

Reads the `filtered/` files from `classEval_output/` and reorganizes them into a flat structure by model/strategy, which is the format expected by SonarQube and `run_sonar.sh`:

```
data/
└── GPT-4-Turbo_method_C_greedy/
    └── AccessGatewayFilter/
        ├── AccessGatewayFilter0Error.py
        ├── AccessGatewayFilter1Success.py
        └── ...
```

## Repository Structure

```
.
├── compose.yaml               # Starts SonarQube with the pre-populated image
├── run_sonar.sh               # Re-submits all projects to SonarQube
├── sonar-project.properties   # Base SonarQube project configuration
├── classEval_output/          # Intermediate output from take_solution.py
└── data/                      # SonarQube input (output from group_filtered_solutions.py)
    ├── GPT-4-Turbo_class_H_greedy/
    ├── GPT-4-Turbo_method_C_greedy/
    ├── GPT-4-Turbo_method_I_greedy/
    ├── PolyCoder-2.7B_class_H_greedy/
    ├── PolyCoder-2.7B_class_H_t0.2/
    ├── PolyCoder-2.7B_method_C_greedy/
    ├── PolyCoder-2.7B_method_C_t0.2/
    ├── PolyCoder-2.7B_method_I_greedy/
    ├── PolyCoder-2.7B_method_I_t0.2/
    └── groundTruth/
```

## Rebuilding the Docker Image

If you need to publish a new version of the image after new analyses:

```bash
# 1. Start SonarQube and run the analyses
docker compose up -d
./run_sonar.sh

# 2. Extract data from the running container
docker cp <container_id>:/opt/sonarqube/data ./sonarqube-data
docker cp <container_id>:/opt/sonarqube/extensions ./sonarqube-extensions

# 3. Rebuild and publish
docker build -t beposs/class_eval_sonar:latest .
docker push beposs/class_eval_sonar:latest
```

> The `sonarqube-data/` and `sonarqube-extensions/` folders are listed in `.gitignore` — they are generated locally only during the image build.
