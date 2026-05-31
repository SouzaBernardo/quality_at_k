# Comparação v2: `combined_sonar_metrics.csv` vs `sonar_metrics_consolidated_master.csv`

> Gerada após a correção do `compute_fqs` (curto-circuito para Pass@1=0).

## Estrutura

| Aspecto | combined | master |
|---|---|---|
| Linhas | 3.528 | 3.413 |
| Colunas | idênticas (12) | idênticas (12) |
| Linhas em comum (model+strategy+file) | 3.313 | 3.313 |

---

## O que é idêntico

- **Esquema de colunas** — exatamente o mesmo nos dois arquivos
- **Cobertura de modelos/estratégias** — mesmos 11 modelos × H/C/I, mesmas contagens por grupo (ChatGLM I=113, incoder I=200, etc.)
- **Valores das métricas SonarQube** — `ncloc`, `sqale_index`, `complexity`, `code_smells`, `cognitive_complexity` coincidem **100%** nas linhas em comum onde ambos têm valor preenchido

---

## O que contrasta

### 1. Cobertura de linhas

| Exclusivo | Linhas | Detalhe |
|---|---|---|
| Apenas no **master** | 100 | GroundTruth (strategy=`GT`, todas Success) |
| Apenas no **combined** | 215 | Vicuna I (97 Error, 14 Fail, 1 PartialSuccess, 3 Success) |

O master usa `strategy="GT"` para GroundTruth; o combined usa `strategy=NaN`.

### 2. Completude das métricas SonarQube

| Métrica | master NaN% | combined NaN% |
|---|---|---|
| `sqale_index` | **0%** | 70,0% |
| `code_smells` | **0%** | 69,9% |
| `ncloc` / `complexity` | 0% | 20,5% |
| `cognitive_complexity` | 44,0% | 43,6% |

O master tem todas as métricas preenchidas — foi extraído de uma execução do SonarQube com projetos completamente analisados. Os ~70% de NaN no combined refletem arquivos onde o código gerado era inválido e o SonarQube não conseguiu calcular dívida técnica.

### 3. `pass_val` — semântica diferente

| | master | combined |
|---|---|---|
| Tipo | Binário **por arquivo** (0 ou 1) | Agregado **por modelo/estratégia** (ex: 0,376 para GPT-4 H) |
| Fonte | Status do nome do arquivo (Success→1, demais→0) | `class_success` do `pass_at_k_result.json` |
| Intervalo | {0.0, 1.0} | 0,000 – 0,376 |

### 4. Tratamento de `PartialSuccess` — divergência central

- **master**: classifica como `status="Success"` com `pass_val=1,0` → `fqs > 0`
- **combined**: classifica como `status="PartialSuccess"` com `fqs = 0,0`

São **144 linhas** afetadas (4,3% das linhas em comum). Nos dados do master essas linhas têm `fqs` entre 0,84 e 1,0; no combined têm `fqs = 0,0`.

Essa é a única divergência de `status` entre os dois arquivos — o master simplesmente não possui a categoria `PartialSuccess`.

| Status | master | combined |
|---|---|---|
| Error | 2.059 | 2.156 |
| Fail | 710 | 724 |
| **Success** | **543** | **302** |
| **PartialSuccess** | — | **145** |
| Unknown | 101 | 101 |

### 5. `fqs` — impacto acumulado das diferenças

| Aspecto | master | combined |
|---|---|---|
| Total NaN | **0** | 322 (Success sem sqale/ncloc) |
| Média geral | 0,157 | 0,024 |
| Concordância exata (linhas em comum, ambos não-NaN) | — | **95,3%** |
| Divergências | — | 144 (todos PartialSuccess) |

A diferença de média (0,157 vs 0,024) tem três causas:
1. **PartialSuccess**: master conta como sucesso com fqs alto; combined zera
2. **GroundTruth**: master inclui 100 linhas com fqs alto (~0,85–1,0); combined tem fqs=NaN para GroundTruth
3. **NaN no combined**: 222 linhas Success sem sqale_index → excluídas da média do combined

---

## Resumo de decisões de design

| Critério | master | combined |
|---|---|---|
| Completude de métricas | ✅ completo | ⚠️ muitos NaN |
| Cobertura de modelos | ⚠️ sem Vicuna I | ✅ tem Vicuna I |
| GroundTruth com fqs | ✅ calculado | ❌ NaN |
| PartialSuccess explícito | ❌ fundido no Success | ✅ categoria separada |
| `pass_val` por arquivo | ✅ binário | ❌ agregado (errado para fqs) |
| `pass_val` agregado (Pass@1 ClassEval) | ❌ ausente | ✅ presente |

Para análise do artigo, o **master é a referência mais confiável** para valores de `fqs` (sem NaN, GroundTruth incluído). O **combined é mais correto semanticamente** em `PartialSuccess` e cobre Vicuna I. O ideal seria um merge outer com alinhamento de `pass_val` e tratamento uniforme de PartialSuccess.
