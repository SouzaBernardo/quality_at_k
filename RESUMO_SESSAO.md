# Resumo da Sessão — Quality@K Pipeline

## Projeto

TCC sobre avaliação de qualidade estática de código gerado por LLMs, usando o benchmark ClassEval + SonarQube.  
Repositório: `/Users/bernardo-souza/workspace/tcc/Quality/`

---

## O que foi feito

### 1. Script `scripts/merge_sonar_metrics.py`

Criado do zero. Lê os 34 CSVs de `sonar-metrics/sonar_metrics_*_files.csv` (métricas por arquivo extraídas do SonarQube) e consolida tudo em um único `sonar-metrics/combined_sonar_metrics.csv`.

**Colunas do output:** `model, strategy, file, base_task, status, ncloc, sqale_index, cognitive_complexity, complexity, code_smells, pass_val, fqs`

**Lógica de extração:**
- `model` e `strategy` (H/C/I/GT) → extraídos do nome do arquivo CSV via regex
- `base_task` e `status` (Success/Fail/Error/PartialSuccess/Unknown) → extraídos do nome do `.py` dentro do CSV
- `pass_val` → agregado `class_success` do `../ClassEval/output/result/pass_at_k_result.json`, mapeado via `MODEL_KEY_MAP`
- `fqs` → fórmula Quality@1 do artigo (ver abaixo)

**Mapeamento de modelos para o JSON de pass@k (todos usam o arquivo antigo — greedy eval):**
```
ChatGLM → ChatGLM          GPT-3.5-Turbo → GPT-3.5      GPT-4-Turbo → GPT-4
PolyCoder-2.7B → PolyCoder  Vicuna → Vicuna               WizardCoder-15B-V1.0 → WizardCoder
codegeex2-6b → CodeGeeX     incoder → Incoder             instruct-codegen-16B → Instruct-CodeGen
santacoder-1.1B → SantaCoder  starcoder-instruct-15B → Instruct-StarCoder  GroundTruth → None
```

**Correções aplicadas ao longo da sessão:**
1. `fqs=None` para não-Success com sqale NaN → corrigido: não-Success retorna `0.0` diretamente (curto-circuito antes de checar métricas)
2. GroundTruth `strategy` alterado de `"N/A"` para `"GT"` pelo usuário
3. GroundTruth `status` alterado de `"N/A"` para `"Success"` como fallback pelo usuário

### 2. Fórmula Quality@1 (`fqs`)

Conforme definida no artigo:

```
Quality@1(t) = Pass@1(t) × (1 − min(1.0, β × SQALE_Index(t) / NCLOC(t)))
```

- `Pass@1(t)` ∈ {0, 1}: 1 se `status == "Success"`, 0 para qualquer outro (Fail/Error/PartialSuccess/Unknown)
- `β = 0.1`
- Se `status == "N/A"` (ex: GroundTruth antes da correção) → `fqs = None`
- Se `sqale_index` ou `ncloc` ausentes/zero para status Success → `fqs = None`
- **Atenção:** `float(NaN)` não lança exceção em Python — por isso o `math.isnan()` explícito é necessário

### 3. Comparações com `sonar_metrics_consolidated_master.csv`

Três rodadas de comparação documentadas em:
- `comparacao_csvs.md` — v1 (antes das correções)
- `comparacao_csvs_v2.md` — v2 (após correção do fqs)
- `comparacao_csvs_v3.md` — v3 (após alinhamento do GroundTruth)

---

## Estado atual do `combined_sonar_metrics.csv`

- **3.528 linhas**, 12 colunas
- **Todas as 3.413 linhas do master têm correspondência exata** no combined
- Linhas extras no combined: 115 do Vicuna I (ausente no master)

---

## Diferenças remanescentes entre combined e master

| Aspecto | master | combined |
|---|---|---|
| `pass_val` | Binário por arquivo (0/1), derivado do status | Agregado por modelo/estratégia (0.0–0.376), do JSON ClassEval |
| `PartialSuccess` | Fundido em `Success` (pass_val=1, fqs>0) | Categoria própria (fqs=0.0) — 144 linhas divergem |
| Completude de métricas | 0% NaN em sqale/code_smells/ncloc/complexity | 70% NaN em sqale/code_smells; 20.5% em ncloc/complexity |
| fqs NaN | 0 | 285 (Success sem sqale_index/ncloc) |
| fqs média | 0,157 | 0,034 |
| Vicuna I | Ausente | Presente (115 linhas) |
| Concordância fqs (linhas em comum) | — | 95,4% exata; 144 divergências (todas PartialSuccess) |

---

## Arquivos criados/modificados

| Arquivo | Descrição |
|---|---|
| `scripts/merge_sonar_metrics.py` | Script de consolidação (criado) |
| `sonar-metrics/combined_sonar_metrics.csv` | CSV consolidado (gerado pelo script) |
| `comparacao_csvs.md` | Comparação v1 |
| `comparacao_csvs_v2.md` | Comparação v2 |
| `comparacao_csvs_v3.md` | Comparação v3 (atual) |

---

## Próximos passos sugeridos

- Decidir o tratamento definitivo de `PartialSuccess` para o artigo (conta como pass=1 ou pass=0 no fqs?)
- Avaliar se usar `pass_val` binário (do master) ou agregado (do combined) na análise final
- Possível merge definitivo: outer join combined+master para ter Vicuna I + métricas completas + fqs sem NaN
