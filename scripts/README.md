# Scripts

Visão geral de todos os scripts do projeto, organizados por função.

---

## Orquestração

### `pipeline.py`
Entry point do projeto. Executa dois estágios em sequência:
1. **PIPELINE** — 5 scripts de extração e cálculo
2. **CHECKS** — 2 scripts de validação

Aborta com código de erro se qualquer script do PIPELINE falhar. Os CHECKS são executados apenas se o PIPELINE concluir com sucesso.

```bash
python3 scripts/pipeline.py
```

---

## Pipeline Principal

Scripts executados em ordem por `pipeline.py`.

### `take_solution.py`
Lê os JSONs brutos do ClassEval (`output/ClassEval_output/`) e extrai o código Python gerado por cada modelo. Aplica limpeza (remove fences Markdown, prosa ao redor do código). Salva as respostas brutas em `output/solutions/originals/{modelo}/` e as versões sanitizadas em `output/solutions/{modelo}/`. Gera `output/results/pass_results.csv` com o status funcional e o `pass_val` de cada tarefa.

### `extract_sonar_metrics.py`
Conecta à API REST do SonarQube (`http://localhost:9000`) e extrai métricas agregadas por projeto (NCLOC, complexidade, code smells, SQALE index, etc.). Salva em `output/results/raw/sonar_metrics.csv`.

### `extract_all_sonar_metrics_per_file.py`
Extrai métricas por arquivo para todos os projetos via API do SonarQube (paginado). Gera um CSV por modelo em `output/results/raw/sonar_metrics_{projeto}_files.csv`.

### `merge_sonar_metrics.py`
Une `pass_results.csv` com os CSVs de métricas por arquivo. Para cada tarefa, calcula o **Quality@1 (FQS)** usando a fórmula:

```
Quality@1(t) = Pass@1(t) × (1 − min(1, β × SQALE_Index(t) / NCLOC(t)))
```

com β = 0.1. Gera `output/results/combined_sonar_metrics.csv`.

### `aggregate_results.py`
Agrupa `combined_sonar_metrics.csv` por `(modelo, estratégia, status)` e calcula média de `pass_val` e FQS. Gera `output/results/aggregated_results.csv`.

---

## Verificação

Scripts executados após o pipeline por `pipeline.py`.

### `verify.py`
Validações pós-pipeline:
- Cada modelo tem exatamente 100 arquivos `.py`
- Nenhum arquivo contém contaminação Markdown (fences, prosa)
- Todo código é Python válido (sem erros de AST)
- `combined_sonar_metrics.csv` e `pass_results.csv` estão consistentes entre si

Emite relatório no console; encerra com erro se alguma verificação falhar.

### `generate_comparations.py`
Para cada modelo, gera um diff HTML lado a lado entre o código original (bruto) e a versão sanitizada. Salva em `output/validation/comparation-{modelo}.html`.

---

## Utilitários

Scripts independentes, não executados pelo `pipeline.py`.

### `compute_fqs.py`
Implementa a fórmula Quality@1 como função pura. Pode ser importado por outros scripts ou usado via CLI:

```bash
python3 scripts/compute_fqs.py --pass_val 1.0 --sqale 120 --ncloc 80
```

### `sort_csv.py`
Ordena qualquer CSV pelas colunas `(model, strategy, file)` com ordem customizada de estratégias: H → C → I → GT. Usado internamente por `merge_sonar_metrics.py`.

### `test_fqs.py`
Testes unitários para `compute_fqs`. Valida a fórmula contra casos do trabalho e situações de borda (Pass@1 = 0, NCLOC = 0, dívida alta/baixa).

```bash
python3 scripts/test_fqs.py
```

### `run_full_analysis.py`
Análise estatística separada do pipeline principal. Lê um CSV consolidado e gera:
- Testes de Mann-Whitney (RQ1: complexidade de código funcional vs. não-funcional)
- Testes de Wilcoxon e correlação de Spearman (RQ2: Pass@1 vs. Quality@1)
- 3 visualizações (barplot, scatter Pareto, heatmap de correlação)
- Relatório Markdown em `reports/relatorio_estatistico.md`

---

## Infraestrutura SonarQube

Scripts de configuração e manutenção do SonarQube. Executar manualmente quando necessário.

### `run_sonar.sh`
Reenvia todos os projetos ao SonarQube via `sonar-scanner`. Usar quando quiser re-analisar o código do zero (requer SonarQube rodando).

### `setup_sonar_projects.sh`
Cria os projetos e tokens de autenticação no SonarQube. Executar uma única vez na configuração inicial. Atualiza `run_sonar.sh` com os tokens gerados.

### `delete_sonar_projects.sh`
Remove todos os projetos do SonarQube. Útil para reset completo.
