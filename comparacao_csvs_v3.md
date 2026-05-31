# Comparação v3: `combined_sonar_metrics.csv` vs `sonar_metrics_consolidated_master.csv`

> Gerada após as três correções aplicadas ao `merge_sonar_metrics.py`:
> 1. Curto-circuito `fqs=0.0` para `Pass@1=0` (v2)
> 2. GroundTruth com `strategy="GT"` (alinha com o master)
> 3. GroundTruth com `status="Success"` como fallback (alinha com o master)

## Estrutura

| Aspecto | combined | master |
|---|---|---|
| Linhas | 3.528 | 3.413 |
| Colunas | idênticas (12) | idênticas (12) |
| Linhas em comum (model+strategy+file) | **3.413** | **3.413** |

Pela primeira vez, **todas** as linhas do master têm correspondência no combined.

---

## O que é idêntico

- **Esquema de colunas** — exatamente o mesmo nos dois arquivos
- **Cobertura de modelos/estratégias** — mesmos 11 modelos × H/C/I + GroundTruth GT; mesmas contagens por grupo
- **Valores das métricas SonarQube** — `ncloc`, `sqale_index`, `complexity`, `code_smells`, `cognitive_complexity` coincidem **100%** em todas as linhas onde ambos têm valor preenchido
- **GroundTruth** — agora totalmente alinhado: `strategy="GT"`, `status="Success"` e `fqs` calculado em ambos

---

## O que contrasta

### 1. Cobertura de linhas

| Exclusivo | Linhas | Detalhe |
|---|---|---|
| Apenas no **master** | **0** | — |
| Apenas no **combined** | 115 | Vicuna I (97 Error, 14 Fail, 1 PartialSuccess, 3 Success) |

O master não contém Vicuna I; o combined tem essas 115 linhas extras.

### 2. Completude das métricas SonarQube

| Métrica | master NaN% | combined NaN% |
|---|---|---|
| `sqale_index` | **0%** | 70,0% |
| `code_smells` | **0%** | 69,9% |
| `ncloc` / `complexity` | 0% | 20,5% |
| `cognitive_complexity` | 44,0% | 43,6% |

O master tem todas as métricas preenchidas. Os NaN no combined refletem arquivos com código inválido onde o SonarQube não conseguiu calcular dívida técnica. Onde ambos têm valor, concordam 100%.

### 3. `pass_val` — semânticas distintas

| | master | combined |
|---|---|---|
| Tipo | Binário **por arquivo** (0 ou 1) | Agregado **por modelo/estratégia** |
| Fonte | Derivado do `status` do arquivo (`Success=1`, demais=0) | `class_success` do `pass_at_k_result.json` |
| Intervalo | {0,0; 1,0} | 0,000 – 0,376 |

### 4. Tratamento de `PartialSuccess` — única fonte de divergência

- **master**: classifica como `status="Success"` com `pass_val=1,0`
- **combined**: classifica como `status="PartialSuccess"` com `fqs=0,0`

São **144 linhas** afetadas. O master não possui a categoria `PartialSuccess` — ela é fundida em `Success`.

| Status | master | combined |
|---|---|---|
| Error | 2.059 | 2.156 |
| Fail | 710 | 724 |
| **Success** | **543** | **402** |
| **PartialSuccess** | **—** | **145** |
| Unknown | 101 | 101 |

> Nota: a diferença de Error/Fail entre os totais inclui as 115 linhas do Vicuna I presentes só no combined.

### 5. `fqs` — resultado final

| Aspecto | master | combined |
|---|---|---|
| Total NaN | **0** | 285 (Success sem sqale_index/ncloc) |
| Média geral | 0,157 | 0,034 |
| Linhas não-nulas em ambos | — | 3.128 |
| Concordância exata | — | **95,4%** |
| Divergências | — | 144 (todos PartialSuccess) |

A diferença de média (0,157 vs 0,034) tem duas causas principais:
1. **PartialSuccess**: master trata como sucesso com `fqs` alto; combined zera
2. **285 NaN no combined**: linhas Success sem `sqale_index` são excluídas da média do combined mas incluídas como zero implícito no master

O fqs do GroundTruth agora é calculado em ambos e concorda onde `sqale_index` está disponível; as divergências do GroundTruth são apenas NaN no combined por métricas ausentes.

---

## Evolução entre versões

| Aspecto | v1 | v2 | v3 |
|---|---|---|---|
| Linhas master com match | 3.313 | 3.313 | **3.413** |
| Linhas sem match no master | 100 (GroundTruth) | 100 (GroundTruth) | **0** |
| fqs NaN (combined) | 322 | 322 | **285** |
| fqs concordância exata | 96,6% (961 linhas) | 95,3% (3.091 linhas) | **95,4% (3.128 linhas)** |
| GroundTruth strategy | NaN | NaN | **GT** |
| GroundTruth status | N/A | N/A | **Success** |
| GroundTruth fqs | NaN | NaN | **calculado** |

---

## Resumo

| Critério | Melhor fonte |
|---|---|
| Completude de métricas SonarQube | **master** (sem NaN) |
| Cobertura de modelos | **combined** (tem Vicuna I) |
| `pass_val` binário por arquivo | **master** |
| `pass_val` agregado (Pass@1 ClassEval) | **combined** |
| PartialSuccess como categoria própria | **combined** |
| fqs sem NaN | **master** |

O combined está agora totalmente alinhado com o master em cobertura de modelos e convenções de nomenclatura. A única diferença estrutural remanescente é o tratamento de `PartialSuccess` e a maior taxa de NaN nas métricas derivada da qualidade das execuções coletadas.
