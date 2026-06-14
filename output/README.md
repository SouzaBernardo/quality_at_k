# output/

Este diretório reúne dois tipos de conteúdo: **entradas do benchmark ClassEval** (pré-existentes, não geradas por este estudo) e **saídas produzidas pelo pipeline deste trabalho**.

---

## Entradas do Benchmark

### `ClassEval_output/`
Arquivos brutos fornecidos pelo benchmark [ClassEval](https://github.com/FudanSELab/ClassEval). Não são gerados por este projeto — devem estar presentes antes de executar o pipeline.

| Caminho | Descrição |
|---------|-----------|
| `ClassEval_output/model_output_v1.0.0/` | JSONs com as respostas brutas de cada LLM às 100 tarefas |
| `ClassEval_output/result/detailed_result.json` | Resultados funcionais do ClassEval: status (`Success`, `PartialSuccess`, `Fail`, `Error`) e `pass@1` por tarefa |

---

## Saídas do Estudo

### `solutions/`
Gerado por `scripts/take_solution.py`.

| Caminho | Descrição |
|---------|-----------|
| `solutions/{modelo}/*.py` | Código Python sanitizado (sem fences Markdown, sem prosa) — entrada para o SonarQube |
| `solutions/originals/{modelo}/*.py` | Resposta bruta do modelo, antes de qualquer limpeza |

### `results/`
Gerado pelo pipeline (`pipeline.py`).

| Arquivo | Gerado por | Descrição |
|---------|------------|-----------|
| `results/pass_results.csv` | `take_solution.py` | Mapeamento `(modelo, tarefa)` → `pass_val` + status funcional |
| `results/raw/sonar_metrics.csv` | `extract_sonar_metrics.py` | Métricas SonarQube agregadas por projeto |
| `results/raw/sonar_metrics_{projeto}_files.csv` | `extract_all_sonar_metrics_per_file.py` | Métricas SonarQube por arquivo, um CSV por modelo |
| `results/combined_sonar_metrics.csv` | `merge_sonar_metrics.py` | Dataset principal: métricas SonarQube + Quality@1 (FQS) por tarefa |
| `results/aggregated_results.csv` | `aggregate_results.py` | FQS médio agrupado por `(modelo, estratégia, status)` |

### `validation/`
Gerado por `scripts/generate_comparations.py`.

| Arquivo | Descrição |
|---------|-----------|
| `validation/comparation-{modelo}.html` | Diff HTML lado a lado entre a resposta bruta e o código sanitizado, por modelo |
