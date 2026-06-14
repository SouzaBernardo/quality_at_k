# Relatório Consolidado de Análise Estatística (Recorte 400 registros)

Este relatório resume os resultados das análises de corretude funcional e qualidade de software (SonarQube) sobre as execuções do benchmark **ClassEval** (Temperatura 0, Geração Holística) focando no recorte de GPT-4-Turbo, GPT-3.5-Turbo, WizardCoder-15B-V1.0 e GroundTruth.

---

## 1. Tabela Geral de Desempenho (Médias por LLM e GroundTruth)

Esta tabela apresenta o sucesso nos testes unitários e as médias das métricas estáticas do SonarQube para cada grupo.

| Model                |   Tasks |   Success (%) |   Partial Success (%) |   Fail (%) |   Error (%) |   Avg NCLOC |   Avg Cyclomatic |   Avg Cognitive |   Avg Code Smells |   Avg Sqale (Debt min) |   Quality@1 (FQS) |
|:---------------------|--------:|--------------:|----------------------:|-----------:|------------:|------------:|-----------------:|----------------:|------------------:|-----------------------:|------------------:|
| GroundTruth          |     100 |           100 |                     0 |          0 |           0 |       34.84 |            11.65 |           11.82 |              1.13 |                   6.29 |          0.983628 |
| GPT-4-Turbo          |     100 |            37 |                    13 |         20 |          30 |       25.97 |             8.78 |            6.53 |              0.55 |                   2.3  |          0.460208 |
| GPT-3.5-Turbo        |     100 |            26 |                     8 |         26 |          40 |       28.33 |             9.18 |            7.9  |              0.69 |                   2.69 |          0.308721 |
| WizardCoder-15B-V1.0 |     100 |            10 |                     3 |         22 |          65 |       19.28 |             7.24 |            4.82 |              0.75 |                   3.79 |          0.117177 |

*Nota: `Quality@1 (FQS)` foi calculado utilizando a fórmula proposta com fator de escala $\beta = 0.1$.*

---

## 2. RQ1: Relação entre Corretude Funcional e Qualidade Estrutural

Investizamos se os códigos funcionais diferem de forma estatisticamente significativa em termos estruturais dos códigos que falharam.

### Teste de Hipótese (Mann-Whitney U por Modelo - Bicaudal):
| Model                | Metric                |   U Statistic |    p-value | Significant (5%)   |
|:---------------------|:----------------------|--------------:|-----------:|:-------------------|
| GPT-4-Turbo          | Cognitive Complexity  |        1200   | 0.730406   | No                 |
| GPT-4-Turbo          | Cyclomatic Complexity |        1167   | 0.568082   | No                 |
| GPT-3.5-Turbo        | Cognitive Complexity  |        1069.5 | 0.703527   | No                 |
| GPT-3.5-Turbo        | Cyclomatic Complexity |        1057.5 | 0.640383   | No                 |
| WizardCoder-15B-V1.0 | Cognitive Complexity  |         803   | 0.00642196 | Yes                |
| WizardCoder-15B-V1.0 | Cyclomatic Complexity |         659   | 0.336708   | No                 |

### Comparação de Complexidade Cognitiva (GPT-4 vs WizardCoder):
* Estatística U: 6571.0
* **p-valor: 6.46e-05**
* *Resultado:* Rejeitamos a Hipótese Nula ($H_{10}$) (nível de significância de 5%).

---

## 3. RQ2: Avaliação e Validação da Métrica `Quality@1` (FQS)

Avaliamos a significância estatística do pedágio de qualidade do FQS em comparação ao Pass@1 clássico.

### Teste de Wilcoxon (Pass@1 vs. Quality@1):
| Model                |   W Statistic |     p-value | Significant (5%)   |
|:---------------------|--------------:|------------:|:-------------------|
| GPT-4-Turbo          |             0 | 0.00220034  | Yes                |
| GPT-3.5-Turbo        |             0 | 0.00768579  | Yes                |
| WizardCoder-15B-V1.0 |             0 | 0.0431144   | Yes                |
| All LLMs Pooled      |             0 | 8.21499e-06 | Yes                |

### Fatos Estatísticos de Validação:
1. **Dívida Técnica Silenciosa (LLMs):** Em **31.51%** dos casos de sucesso funcional das LLMs (73 arquivos), o score final de qualidade foi reduzido devido à dívida técnica.
2. **Dívida Técnica Silenciosa (Total):** Considerando todos os **173** sucessos da base (incluindo GroundTruth), **60** arquivos (**34.68%**) contêm dívida técnica silenciosa.
3. **Validação Convergente (Spearman nos Sucessos das LLMs):**
   * A correlação de Spearman entre `Quality@1` e *Code Smells* é de **-0.9825** (p-valor: 1.52e-53), provando forte validade de construto com manutenibilidade.
   * A correlação com *Complexidade Cognitiva* é de **0.0190** (p-valor: 8.74e-01), sem correlação significativa nos sucessos.

---

## 4. Discussão: Diagnóstico da Referência Humana (GroundTruth vs. GPT-4-Turbo)

Apresentamos as análises estatísticas comparativas entre os sucessos funcionais do GroundTruth e do GPT-4-Turbo, além da identificação de superioridade de qualidade das LLMs.

### Fatos Estatísticos do GroundTruth:
* **Classes com Dívida Técnica:** **37** das 100 classes de referência humana (**37.00%**) possuem dívida técnica silenciosa (FQS < 1.0).

### Tarefas onde LLMs superaram o GroundTruth em Qualidade Estrutural (FQS_LLM = 1.0 > FQS_GT):
| Tarefa              |   FQS GT |   GPT-4 |   GPT-3.5 |   WizardCoder |
|:--------------------|---------:|--------:|----------:|--------------:|
| BalancedBrackets.py |   0.8704 |       1 |         1 |             1 |
| BigNumCalculator.py |   0.9839 |       1 |         1 |             0 |
| Calculator.py       |   0.9738 |       1 |         0 |             0 |
| ShoppingCart.py     |   0.9706 |       1 |         1 |             0 |
| TimeUtils.py        |   0.9259 |       0 |         1 |             1 |
| ZipFileProcessor.py |   0.9375 |       1 |         0 |             0 |

### Contraste Estatístico (MWU nos Sucessos: GT vs GPT-4-Turbo):
Compare exclusivamente implementações funcionais bem-sucedidas ($N_{GT} = 100$, $N_{GPT4} = 37$).

| Métrica                   |   GT Média |   GPT-4 Média |   U Statistic |     p-value | Significativo (5%)   |
|:--------------------------|-----------:|--------------:|--------------:|------------:|:---------------------|
| Complexidade Cognitiva    |    11.82   |        5.5676 |        2541.5 | 0.000786148 | Yes                  |
| Complexidade Ciclomática  |    11.65   |        8.3243 |        2493   | 0.00178866  | Yes                  |
| Code Smells               |     1.13   |        0.5946 |        2071   | 0.205596    | No                   |
| Dívida Técnica (min)      |     6.29   |        2.5405 |        2091   | 0.168138    | No                   |
| FQS                       |     0.9836 |        0.9875 |        1692   | 0.367029    | No                   |
| Tamanho de Código (NCLOC) |    34.84   |       24.6757 |        2735   | 1.78378e-05 | Yes                  |

