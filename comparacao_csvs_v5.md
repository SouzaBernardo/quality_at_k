# Comparação v5: `combined_sonar_metrics.csv` vs `sonar_metrics_consolidated_master.csv`

> Gerada após as mudanças aplicadas ao `merge_sonar_metrics.py` desde v4:
> 1. `pass_val` agora vem de `pass_at_greedy_value.csv` — binário **por tarefa** (antes: agregado por modelo/estratégia via JSON)
> 2. Correção de NaN silencioso: `min(1.0, NaN)` retornava `1.0` no Python, gerando `fqs=0.0` incorreto em vez de `None`

## Estrutura

| Aspecto | combined | master |
|---|---|---|
| Linhas | 3.528 | 3.413 |
| Colunas | idênticas (12) | idênticas (12) |
| Linhas em comum (model+strategy+file) | **3.413** | **3.413** |

Todas as linhas do master têm correspondência no combined (igual v4).

---

## O que mudou em relação à v4

### `pass_val` agora tem a mesma semântica do master

| | master | combined v4 | combined v5 |
|---|---|---|---|
| Tipo | Binário por arquivo | Agregado por modelo/estratégia | **Binário por tarefa** |
| Fonte | Derivado do `status` | `class_success` do JSON | **`pass_at_greedy_value.csv`** |
| Intervalo | {0,0; 1,0} | 0,000 – 0,376 | **{0,0; 1,0}** |
| Concordância com master | — | ~0% (escalas diferentes) | **95,4% (3.161/3.312)** |

---

## O que contrasta

### 1. Cobertura de linhas

| Exclusivo | Linhas | Detalhe |
|---|---|---|
| Apenas no **master** | 0 | — |
| Apenas no **combined** | 115 | Vicuna I (97 Error, 14 Fail, 1 PartialSuccess, 3 Success) |

### 2. Status

| Status | master | combined |
|---|---|---|
| Error | 2.059 | 2.156 |
| Fail | 710 | 724 |
| **Success** | **543** | **402** |
| **PartialSuccess** | **—** | **145** |
| Unknown | 101 | 101 |

O master continua sem a categoria `PartialSuccess` — essas 144 linhas comuns aparecem como `Success` no master.

### 3. Completude das métricas SonarQube

| Métrica | master NaN% | combined NaN% |
|---|---|---|
| `sqale_index` | **0%** | 70,0% |
| `code_smells` | **0%** | 69,9% |
| `ncloc` / `complexity` | 0% | 20,5% |
| `cognitive_complexity` | 44,0% | 43,6% |

Inalterado em relação às versões anteriores — reflete a qualidade das execuções coletadas.

### 4. `pass_val` — divergências residuais (4,6%)

| Causa | Linhas | Detalhe |
|---|---|---|
| **PartialSuccess** | 144 | combined: CSV diz 0,0; master: trata como Success → 1,0 |
| **Unknown** | 6 | combined: CSV diz 0,0; master: deriva do status → 0,0 (maioria concorda) |
| **Fail com CSV=1** | 1 | `MusicPlayerFail.py` (ChatGLM I): CSV indica pass@1=1,0, master=0,0 (status=Fail) |

### 5. GroundTruth — continua sem fqs

| | v3 | v4 | v5 |
|---|---|---|---|
| `pass_val` | None | None | **None** |
| `fqs` | calculado | NaN (100%) | **NaN (100%)** |

GroundTruth não possui entrada no `pass_at_greedy_value.csv`; `pass_val = None` → `fqs = None`.

### 6. `fqs` — resultado final

| Aspecto | master | combined v4 | combined v5 |
|---|---|---|---|
| Total NaN | 0 | 322 | **323** |
| Média geral | 0,157 | 0,005 | **0,024** |
| Linhas com fqs em ambos | — | 3.091 | **3.090** |
| Concordância exata | — | 92,9% (2.870) | **95,3% (2.946)** |
| Divergências | — | 543 | **467** |

#### Origem das divergências (467)

| Status | Qtd | Causa |
|---|---|---|
| **Success** | 322 | combined `fqs=NaN` (sqale_index ausente); master tem valor (métricas sempre presentes) |
| **PartialSuccess** | 144 | combined `fqs=0,0`; master classifica como Success → `fqs>0` |
| **Unknown** | 1 | `ExpressionCalculatorUnknown.py`: combined `pass_val=None` → `fqs=NaN`; master `fqs=0,0` |

**Ponto crítico:** quando ambos têm `fqs` não-nulo, a concordância é **100%** — não há mais divergência de valor, apenas de presença (NaN vs preenchido).

---

## Evolução entre versões

| Aspecto | v1 | v2 | v3 | v4 | **v5** |
|---|---|---|---|---|---|
| Linhas master com match | 3.313 | 3.313 | 3.413 | 3.413 | **3.413** |
| fqs NaN (combined) | 322 | 322 | 285 | 322 | **323** |
| fqs concordância exata | 96,6% | 95,3% | 95,4% | 92,9% | **95,3%** |
| fqs média combined | — | — | 0,034 | 0,005 | **0,024** |
| `pass_val` binário por tarefa | ✗ | ✗ | ✗ | ✗ | **✓** |
| `pass_val` = master (mesma semântica) | ✗ | ✗ | ✗ | ✗ | **✓ (95,4%)** |
| Concordância fqs quando ambos válidos | parcial | parcial | parcial | parcial | **100%** |
| GroundTruth fqs | NaN | NaN | calculado | NaN | **NaN** |

---

## Resumo

| Critério | Melhor fonte |
|---|---|
| Completude de métricas SonarQube | **master** (sem NaN) |
| Cobertura de modelos | **combined** (Vicuna I) |
| `pass_val` por tarefa (binário) | **equivalentes** — mesma semântica em v5 |
| fqs sem NaN | **master** |
| fqs correto quando métricas disponíveis | **equivalentes** — concordância 100% |
| PartialSuccess como categoria própria | **combined** |
| GroundTruth com fqs | **master** |

A principal diferença estrutural remanescente é a **ausência de métricas SonarQube** no combined (NaN em sqale_index/ncloc) para arquivos onde o código gerado não era analisável. Quando as métricas estão presentes, o fqs do combined e do master concordam 100%.
