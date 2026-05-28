# Comparação: `combined_sonar_metrics.csv` vs `sonar_metrics_consolidated_master.csv`

## Estrutura

| Aspecto | combined | master |
|---|---|---|
| Linhas | 3.528 | 3.413 |
| Colunas | idênticas (12) | idênticas (12) |

Colunas: `model, strategy, file, base_task, status, ncloc, sqale_index, cognitive_complexity, complexity, code_smells, pass_val, fqs`

---

## O que é idêntico

- **Esquema de colunas** — exatamente o mesmo nos dois arquivos
- **Cobertura de modelos/estratégias** — mesmos 11 modelos × 3 estratégias (H/C/I), com as mesmas contagens por grupo (ex: ChatGLM I = 113, incoder I = 200)
- **Valores métricos do SonarQube** — `ncloc`, `sqale_index`, `complexity`, `code_smells` coincidem 100% nas 3.313 linhas em comum (verificado via merge em `model + strategy + file`)

---

## O que contrasta

### 1. Cobertura de linhas

| Diferença | Linhas |
|---|---|
| Apenas no **master** | 100 linhas do GroundTruth (strategy=`GT`, status=`Success`) |
| Apenas no **combined** | 115 linhas do Vicuna I (ausente no master) |

O master tem GroundTruth mas não tem Vicuna I. O combined tem Vicuna I mas trata GroundTruth com `strategy=NaN`.

### 2. `pass_val` — semântica completamente diferente

| | master | combined |
|---|---|---|
| Tipo | Binário **por arquivo** (0.0 ou 1.0) | Agregado **por modelo/estratégia** (ex: 0.376 para GPT-4 H) |
| Fonte | Derivado do status no nome do arquivo (`Success=1`, demais=0) | `class_success` do `ClassEval/output/result/pass_at_k_result.json` |

### 3. Tratamento de `PartialSuccess`

- **master**: classifica `PartialSuccess` como `status="Success"` com `pass_val=1.0`
- **combined**: classifica como `status="PartialSuccess"` com `pass_binary=0` → `fqs=0.0`

Isso gera **33 divergências no `fqs`**: master tem fqs > 0 nesses casos; combined tem fqs = 0.0.

### 4. Completude de `sqale_index` e `code_smells`

| Métrica | master NaN% | combined NaN% |
|---|---|---|
| `sqale_index` | **0%** | 70% |
| `code_smells` | **0%** | 70% |
| `ncloc` / `complexity` | 0% | 20.5% |
| `cognitive_complexity` | 44% | 43.6% |

O master foi extraído com os projetos mais completos no SonarQube — todos os arquivos têm métricas preenchidas. O combined tem muitos NaN porque algumas runs não geraram código válido e o SonarQube não calculou essas métricas.

### 5. `fqs` — impacto combinado

Dos 961 arquivos com `fqs` preenchido em ambos: **96.6% concordam exatamente**. Os 33 divergentes são todos casos de `PartialSuccess` (tratados como sucesso no master, como falha no combined).

---

## Resumo

| Critério | Melhor fonte |
|---|---|
| Completude de métricas SonarQube | **master** (sem NaN) |
| Cobertura de modelos | **combined** (tem Vicuna I) |
| `pass_val` por arquivo (binário) | **master** |
| `pass_val` agregado (Pass@1 do ClassEval) | **combined** |
| Tratamento de PartialSuccess | **combined** (mais granular) |

Para um CSV definitivo seria necessário: fazer outer join para incluir Vicuna I e GroundTruth, uniformizar o tratamento de `PartialSuccess`, e decidir qual semântica de `pass_val` usar.
