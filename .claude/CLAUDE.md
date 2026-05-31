# Quality@K — Contexto para Claude

## Projeto
TCC: avaliar se código gerado por LLMs que passa nos testes funcionais (ClassEval) também tem boa qualidade estática (SonarQube).

## Fórmula Quality@1
```
Quality@1(t) = Pass@1(t) × (1 − min(1, β × SQALE_Index(t) / NCLOC(t)))
```
β = 0.1. Pass@1 ∈ {0, 1}. Quando ncloc=0 ou sqale=NaN → assume sqale=0 (sem penalidade).

## Pipeline (executar com `python3 scripts/run_pipeline.py`)
1. `merge_sonar_metrics.py`  — lê `sonar-metrics/raw/` + `pass_at_greedy_value.csv` → `combined_sonar_metrics.csv`
2. `prioritize_duplicates.py` — remove duplicatas por `(model, strategy, base_task)`, prioridade: Success > PartialSuccess > Fail > Error > Unknown
3. `aggregate_fqs.py` — média FQS por `(model, strategy)` → `fqs_aggregated.csv`

## Decisões fixadas
- GroundTruth: `pass_val = 1.0` (não está no `pass_at_greedy_value.csv`)
- PartialSuccess: `fqs = 0.0` (não conta como sucesso)
- `sqale_index` ou `ncloc` ausentes/NaN: assume 0 (sem penalidade)
- `fqs_aggregated.csv`: GroundTruth sempre na 1ª linha, resto em ordem decrescente de `fqs_mean`

## Arquivos-chave
- `sonar-metrics/combined_sonar_metrics.csv` — 3.400 linhas (34 grupos × 100 tarefas)
- `sonar-metrics/fqs_aggregated.csv`         — 34 linhas (1 por modelo/estratégia)
- `sonar-metrics/pass_at_greedy_value.csv`   — mapeamento `(model_strategy, task) → pass@1`
- `sonar-metrics/raw/`                       — 34 CSVs brutos do SonarQube (1 por modelo/estratégia)

## Modelos (11 modelos × 3 estratégias H/C/I + GroundTruth GT = 34 grupos)
ChatGLM, codegeex2-6b, GPT-3.5-Turbo, GPT-4-Turbo, GroundTruth,
incoder, instruct-codegen-16B, PolyCoder-2.7B, santacoder-1.1B,
starcoder-instruct-15B, Vicuna, WizardCoder-15B-V1.0
