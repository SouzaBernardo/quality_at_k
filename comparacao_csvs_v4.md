# Comparação v4: `combined_sonar_metrics.csv` vs `sonar_metrics_consolidated_master.csv`

> Gerada após as mudanças aplicadas ao `merge_sonar_metrics.py` desde v3:
> 1. `compute_fqs` agora multiplica `pass_val` (Pass@1 agregado) — fórmula completa: `Pass@1 × (1 - min(1, β·SI/NCLOC))`
> 2. `PASS_AT_K_JSON` aponta para `result/pass_at_k_result.json` local (antes dependia do repositório ClassEval externo)

## Estrutura

| Aspecto | combined | master |
|---|---|---|
| Linhas | 3.528 | 3.413 |
| Colunas | idênticas (12) | idênticas (12) |
| Linhas em comum (model+strategy+file) | **3.413** | **3.413** |

Todas as linhas do master têm correspondência no combined (igual v3).

---

## O que é idêntico em relação à v3

- **Esquema de colunas** — mesmo nos dois arquivos
- **Cobertura de modelos/estratégias** — mesmos 11 modelos × H/C/I + GroundTruth GT; mesmas contagens por grupo
- **Valores das métricas SonarQube** — `ncloc`, `sqale_index`, `complexity`, `code_smells`, `cognitive_complexity` coincidem 100% onde ambos têm valor
- **Cobertura de linhas** — 115 linhas exclusivas do combined (Vicuna I); 0 exclusivas do master

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

Inalterado em relação à v3.

### 4. `pass_val` — semânticas distintas (inalterado)

| | master | combined |
|---|---|---|
| Tipo | Binário **por arquivo** (0 ou 1) | Agregado **por modelo/estratégia** |
| Fonte | Derivado do `status` do arquivo (`Success=1`, demais=0) | `class_success` do `pass_at_k_result.json` |
| Intervalo | {0,0; 1,0} | 0,000 – 0,376 |

### 5. GroundTruth — regressão em relação à v3

| | v3 | v4 |
|---|---|---|
| `fqs` GroundTruth | calculado (onde sqale_index disponível) | **None (100%)** |

Em v4, `pass_val = None` para GroundTruth (não está no `MODEL_KEY_MAP` com chave de JSON associada). Como `compute_fqs` retorna `None` quando `pass_val is None`, todos os 100 registros do GroundTruth passaram a ter `fqs = NaN`, revertendo o ganho da v3.

### 6. `fqs` — resultado final

| Aspecto | master | combined v3 | combined v4 |
|---|---|---|---|
| Total NaN | 0 | 285 | **322** |
| Média geral | 0,157 | 0,034 | **0,005** |
| Linhas não-nulas em ambos | — | 3.128 | **3.091** |
| Concordância exata | — | 95,4% (2.991) | **92,9% (2.870)** |
| Divergências | — | 144 (PartialSuccess) | **543** |

#### Origem das divergências (543)

| Status | Qtd | Causa |
|---|---|---|
| **PartialSuccess** | 144 | master classifica como Success (fqs > 0); combined zera (fqs = 0,0) |
| **Success** | 399 | combined: `fqs = pass_val × (1-p)` com pass_val ∈ [0,01; 0,376]; master: `fqs = 1,0 × (1-p)` com fqs ∈ [0,83; 1,0] |

O aumento de 144 → 543 divergências é direto consequência da multiplicação por `pass_val` na fórmula de FQS: como o combined usa o Pass@1 agregado (máximo 0,376) e o master usa `1,0` para todos os Success, os valores de `fqs` são sistematicamente menores no combined.

---

## Evolução entre versões

| Aspecto | v1 | v2 | v3 | **v4** |
|---|---|---|---|---|
| Linhas master com match | 3.313 | 3.313 | 3.413 | **3.413** |
| Linhas sem match no master | 100 | 100 | **0** | **0** |
| fqs NaN (combined) | 322 | 322 | 285 | **322** |
| fqs concordância exata | 96,6% (961) | 95,3% (3.091) | 95,4% (3.128) | **92,9% (2.870)** |
| GroundTruth fqs | NaN | NaN | **calculado** | **NaN (regressão)** |
| `pass_val` multiplicado no fqs | ✗ | ✗ | ✗ | **✓** |
| Path JSON local | ✗ | ✗ | ✗ | **✓** |

---

## Análise das diferenças estruturais remanescentes

| Critério | Melhor fonte | Detalhe |
|---|---|---|
| Completude de métricas SonarQube | **master** | Sem NaN; combined reflete qualidade real das execuções |
| Cobertura de modelos | **combined** | Inclui Vicuna I (115 linhas) |
| `pass_val` binário por arquivo | **master** | Derivado do status da execução |
| `pass_val` agregado Pass@1 ClassEval | **combined** | Fonte: `pass_at_k_result.json` |
| fqs fórmula completa (`Pass@1 × qualidade`) | **combined** | master usa `pass_val=1` → ignora taxa de sucesso |
| GroundTruth com fqs calculado | **master** (v3 combined) | v4 combined tem regressão: fqs=NaN para GT |
| PartialSuccess como categoria própria | **combined** | master funde com Success |

---

## Ponto de atenção para correção futura

O GroundTruth não tem entrada no `pass_at_k_result.json`, portanto `pass_val = None` → `fqs = None`. Para que o GroundTruth tenha fqs calculado é necessário ou:
- Tratar GroundTruth como caso especial com `pass_val = 1.0` (código de referência perfeita), ou
- Separar a coluna `quality_score = (1 - penalty)` do fqs final, calculando o fqs apenas onde `pass_val` existe.
