# Contexto da sessão — Quality@1 (FQS) para TCC

Cole este arquivo em um novo chat com a mensagem:
> "Leia o @CONTEXTO_SESSAO.md e continue de onde paramos."

---

## Projeto

TCC que usa SonarQube para extrair métricas de qualidade dos resultados gerados pelo benchmark **ClassEval**. O objetivo é calcular uma métrica chamada **Quality@1** (também chamada FQS) que combina a taxa de sucesso funcional com a qualidade estrutural do código gerado.

Repositório: `/Users/bernardo-souza/workspace/tcc/Quality`  
Branch atual: `check/sonar`

---

## Fórmula implementada

```
Quality@1(t) = Pass@1(t) × (1 - min(1, β × SQALE_Index(t) / NCLOC(t)))
```

- `t` = tarefa individual (ex: `AccessGatewayFilter`, `ShoppingCart`)
- `Pass@1(t)` = binário {0, 1} por tarefa (vem do CSV de mapeamento)
- `β = 0.1`
- `SQALE_Index` = dívida técnica em minutos (SonarQube)
- `NCLOC` = linhas de código não comentadas (SonarQube)

---

## Arquivos criados/modificados nesta sessão

### Scripts (`scripts/`)

| Arquivo | Função |
|---|---|
| `compute_fqs.py` | Função `compute_fqs(pass_at_1, sqale_index, ncloc, beta=0.1)` — cálculo puro da fórmula. Também executável via CLI: `python3 compute_fqs.py <pass_at_1> <sqale_index> <ncloc>` |
| `test_fqs.py` | Valida `compute_fqs` com os 10 casos de teste da tabela do paper. Todos passando. |
| `merge_sonar_metrics.py` | Script principal: lê CSVs do SonarQube + `pass_at_greedy_value.csv`, calcula FQS por linha, gera `combined_sonar_metrics.csv` |
| `prioritize_duplicates.py` | Remove duplicatas de `base_task` por `(model, strategy)` mantendo a prioridade: `Success > PartialSuccess > Fail > Error > Unknown` |
| `aggregate_fqs.py` | Calcula média do FQS por `(model, strategy)`, gera `fqs_aggregated.csv` |

### CSVs (`sonar-metrics/`)

| Arquivo | Descrição |
|---|---|
| `pass_at_greedy_value.csv` | Mapeamento `(model_strategy, task) → pass@1` binário por tarefa. Ex: `ChatGLM_C, Hotel, 1.0`. Criado manualmente pelo usuário. |
| `combined_sonar_metrics.csv` | Saída principal: 3.400 linhas (34 grupos × 100 tarefas), 12 colunas |
| `fqs_aggregated.csv` | Média do FQS por modelo/estratégia (34 linhas) |

### Arquivos de comparação

| Arquivo | Descrição |
|---|---|
| `comparacao_csvs_v5.md` | Comparação mais recente entre `combined` e `sonar_metrics_consolidated_master.csv` |

---

## Estado atual do `combined_sonar_metrics.csv`

**Colunas:** `model, strategy, file, base_task, status, ncloc, sqale_index, cognitive_complexity, complexity, code_smells, pass_val, fqs`

**Tamanho:** 3.400 linhas (34 grupos × 100 tarefas após deduplicação)

**`pass_val`:** binário {0.0, 1.0} por tarefa, vindo de `pass_at_greedy_value.csv`  
**`fqs`:** `None` quando métricas SQALE ausentes ou quando GroundTruth (sem pass_val no CSV)

---

## Fluxo de execução

```bash
cd scripts/

# 1. Gerar combined (lê sonar-metrics/sonar_metrics_*_files.csv + pass_at_greedy_value.csv)
python3 merge_sonar_metrics.py

# 2. Remover duplicatas por prioridade de status
python3 prioritize_duplicates.py

# 3. Calcular médias por modelo/estratégia
python3 aggregate_fqs.py

# Validar a fórmula
python3 test_fqs.py
```

---

## Decisões e pontos de atenção

1. **GroundTruth sem FQS**: O modelo `GroundTruth` não tem entrada no `pass_at_greedy_value.csv`, então `pass_val=None` e `fqs=NaN` para todos os 100 registros. Possíveis soluções: atribuir `pass_val=1.0` manualmente ou separar uma coluna `quality_score` independente de Pass@1.

2. **NaN em SQALE/NCLOC**: ~70% dos registros não-GT têm `sqale_index=NaN`. Isso ocorre quando o código gerado não era analisável pelo SonarQube. Nesses casos `fqs=NaN`.

3. **PartialSuccess**: O combined trata como `fqs=0.0` (pass@1=0 no CSV). O master trata como Success.

4. **Deduplicação**: Todos os grupos agora têm exatamente 100 tarefas (128 pares de duplicatas foram removidos, não apenas Vicuna I).

5. **Concordância com master**: Quando ambos têm `fqs` não-nulo, concordância é 100%. As divergências são apenas de presença (NaN vs preenchido) ou de tratamento do PartialSuccess.

---

## Resultados do `fqs_aggregated.csv` (top 5 por fqs_mean)

| model | strategy | pass_rate | fqs_mean | fqs_mean_all |
|---|---|---|---|---|
| GPT-4-Turbo | H | 0.37 | 0.1306 | 0.0954 |
| GPT-4-Turbo | I | 0.29 | 0.1075 | 0.0860 |
| GPT-3.5-Turbo | I | 0.27 | 0.1058 | 0.0868 |
| GPT-3.5-Turbo | H | 0.26 | 0.1047 | 0.0869 |
| GPT-4-Turbo | C | 0.29 | 0.0880 | 0.0687 |
