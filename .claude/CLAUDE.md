# Quality@K — Claude Context

## Project

This project evaluates whether LLM-generated code that passes functional tests
on the ClassEval benchmark also has good static quality according to SonarQube.

## Quality@1 Formula

```text
Quality@1(t) = Pass@1(t) × (1 − min(1, β × SQALE_Index(t) / NCLOC(t)))
```

`β = 0.1`; `Pass@1 ∈ {0, 1}`. See `scripts/compute_fqs.py` for edge-case
behavior.

## Current Dataset

The repository contains 100 tasks for each of three model outputs and the
ClassEval human reference (GroundTruth), for four groups total. The model
outputs use the Holistic (H) strategy; GroundTruth uses the GT code.

## Pipeline

Run the full pipeline with:

```bash
python3 scripts/pipeline.py
```

The pipeline extracts and sanitizes solutions, collects SonarQube metrics,
merges the metrics with functional results, calculates Quality@1, aggregates
the results, and runs validation checks. SonarQube must be available when
running the metric extraction steps.

## Key Files

- `output/ClassEval_output/` — raw ClassEval inputs
- `output/solutions/{model}/` — sanitized Python solutions
- `output/results/pass_results.csv` — functional status and Pass@1 per task
- `output/results/combined_sonar_metrics.csv` — per-task SonarQube metrics and Quality@1
- `output/results/aggregated_results.csv` — mean results grouped by model, strategy, and status
