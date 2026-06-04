# Relatório de Anomalias do Recorte da Base de Dados

Este documento serve como um guia de auditoria para identificar e corrigir os erros e inconsistências de dados presentes no arquivo de recorte **`sonar_metrics_consolidated_master_recorte.csv`** (que contém 400 registros focando em GPT-4-Turbo, GPT-3.5-Turbo, WizardCoder-15B-V1.0 sob a estratégia Holística e o GroundTruth).

---

## Resumo Simples dos Problemas Detectados

Para um entendimento rápido, a base de dados do recorte possui **quatro problemas principais**:

1. **Arquivos Vazios com Nota Máxima de Qualidade:** O script de limpeza de comentários apagou acidentalmente todo o código de algumas classes. Para as classes corretas que ficaram com 0 linhas de código (NCLOC = 0), a fórmula do FQS calculou erroneamente uma **nota perfeita de 1.0** (como se o código fosse impecável, quando na verdade estava vazio).
2. **Distorção (Inflação) das Médias de Complexidade:** Classes muito simples possuem complexidade cognitiva zero. O SonarQube deixou esses campos vazios e a planilha os importou como `NaN`. Como ferramentas de estatística ignoram `NaN` em vez de tratá-los como `0.0`, as médias de complexidade cognitiva dos modelos foram infladas artificialmente (aumentando a média do WizardCoder em **163%** e a do GPT-4 em **35%**).
3. **Tratamento de FQS Negativo e Status de Falha:** Para arquivos que falharam nos testes (`Fail`/`Error`), a fórmula seca do FQS resulta em valores extremamente negativos (ex: `-8.2`). O script precisa forçar esses valores para `0.0` para manter o FQS estritamente no intervalo lógico de $[0.0, 1.0]$.
4. **Erro de Modelagem do `pass_val` (Perda de Granularidade Funcional):** A taxa de testes unitários que passaram (`pass_val`) foi zerada (**`0.0`**) para todas as instâncias de **`PartialSuccess`**. Em vez de representar a taxa fracionária de acertos (ex: `0.75` se 3 de 4 testes passaram), o Bernardo tratou a métrica de forma binária (apenas `1.0` para `Success` completo e `0.0` para todo o resto), jogando fora a riqueza estatística das execuções parciais.

---

## Lista de Tarefas para o Bernardo (Deixar a Base 100% Confiável)

Para garantir que os dados de qualidade de código do artigo estejam estatisticamente corretos e livres de viés, o **Bernardo** precisa executar as seguintes etapas de correção diretamente nos scripts do pipeline e na re-análise do SonarQube:

### [ ] Tarefa 1: Corrigir o Script de Sanitização por Regex (Pré-análise)
* **O Problema:** O regex atual de limpeza de comentários e docstrings é agressivo demais e está apagando o código fonte inteiro das classes, reduzindo-os a arquivos de 0 bytes (`ncloc = 0.0`).
* **Como Validar na Planilha:**
  * **Caso Exemplo:** Procurar na base pelo arquivo **`BankAccountSuccess.py`** do modelo **`WizardCoder-15B-V1.0`** (estratégia **`H`**). Você verá que a coluna **`ncloc`** está como **`0.0`** (o arquivo foi completamente esvaziado).
* **Ação:**
  1. Localizar o script Python que limpa o código antes do envio ao SonarQube.
  2. Ajustar a lógica de regex para garantir que ela remova apenas comentários (`# ...`) e blocos de strings literais usados como documentação (`""" ... """` ou `''' ... '''`), sem apagar a declaração de classes, métodos e comandos funcionais.
  3. Testar a correção na classe `BankAccountSuccess.py` e garantir que o código útil permaneça intacto.
  4. Re-enviar os arquivos corrigidos ao SonarQube para recalcular seus valores reais de `ncloc`, `code_smells` e `sqale_index`.

### [ ] Tarefa 2: Ajustar a Lógica de Cálculo do FQS no Consolidador (Pós-análise)
* **O Problema:** Arquivos vazios ou corrompidos com status `Success` estão obtendo nota de qualidade máxima (`fqs = 1.0`).
* **Como Validar na Planilha:**
  * **Caso Exemplo:** Procurar na base pelo arquivo **`BankAccountSuccess.py`** do modelo **`WizardCoder-15B-V1.0`** (estratégia **`H`**). Note que o seu status é **`Success`**, seu **`ncloc`** está **`0.0`**, mas seu score **`fqs`** está registrado como **`1.0`** (máximo).
* **Ação:**
  1. No script do pipeline que calcula o FQS, adicionar uma verificação de segurança.
  2. Garantir que, se o arquivo estiver vazio ou com `ncloc == 0.0`, ele receba `fqs = 0.0` (ou seja classificado como erro de execução no pipeline, e não como sucesso de alta qualidade).

### [ ] Tarefa 3: Validar FQS Negativos e Status de Falha
* **O Problema:** Em casos de arquivos que falharam (`Fail`/`Error`), a aplicação cega da fórmula resulta em valores negativos.
* **Como Validar na Planilha:**
  * **Caso Exemplo:** Procurar o arquivo **`AccessGatewayFilterError.py`** do modelo **`GPT-3.5-Turbo`** (estratégia **`H`**). Ele possui `ncloc = 9.0` e `sqale_index = 5.0`. A aplicação pura da fórmula resultaria em: $1.0 - (5.0 / (9.0 \times 0.06)) = -8.259$. 
  * O seu script atual corrigiu isso para `0.0` porque o status é `Error`. Você precisa manter essa blindagem no novo script de extração.
* **Ação:**
  1. No script de consolidação de dados do SonarQube, garantir que se o status do arquivo for `Error` ou `Fail`, o score FQS seja setado diretamente para `0.0`.
  2. Para os casos de `Success`, aplicar a fórmula limitando o FQS inferiormente a `0.0` (usando um limite mínimo de zero) caso a dívida técnica calculada supere o esforço de reescrita.

### [ ] Tarefa 4: Corrigir a Modelagem da Taxa de Testes (`pass_val`)
* **O Problema:** Para arquivos com status `PartialSuccess`, a coluna `pass_val` está preenchida com `0.0`. Ela deveria conter o valor real fracionário da taxa de acerto de testes (ex: se a classe passou em 6 de 8 testes, a taxa é `0.75`).
* **Como Validar na Planilha:**
  * **Caso Exemplo:** Procurar na base pelo arquivo **`DatabaseProcessorPartialSuccess.py`** do modelo **`GPT-3.5-Turbo`** (estratégia **`H`**). Você verá que o status é **`PartialSuccess`** e a coluna **`pass_val`** está preenchida com **`0.0`**.
* **Ação:**
  1. No script que executa a suite de testes e gera os JSONs de resultados (ou no script de parsing da consolidação), calcular a taxa real contínua de testes passados usando os dados das chaves de resultados (`testsRun`, `errors` e `failures`):
     $$\text{pass\_val} = \frac{\text{testsRun} - (\text{errors} + \text{failures})}{\text{testsRun}}$$
  2. Substituir o valor estático `0.0` de `PartialSuccess` pela taxa contínua calculada acima.

### [ ] Tarefa 5: Tratar Valores Ausentes (NaNs) de Complexidade Cognitiva
* **O Problema:** O SonarQube não emite valor de complexidade cognitiva para códigos lineares/simples (que têm complexidade 0.0), e o Pandas importa isso como `NaN`. O Pandas ignora esses NaNs ao calcular médias, inflacionando as estatísticas em até 163%.
* **Como Validar na Planilha:**
  * **Caso Exemplo:** Procurar o arquivo **`CamelCaseMapSuccess.py`** do modelo **`GPT-3.5-Turbo`** (estratégia **`H`**). Você verá que a coluna **`cognitive_complexity`** está completamente em branco (**`NaN`**). No cálculo de médias, o Pandas exclui esse arquivo, quando ele deveria contar como complexidade `0.0`.
* **Ação:**
  1. No script que analisa os dados e plota os gráficos do artigo, preencher explicitamente os nulos da complexidade cognitiva com `0.0` logo após o carregamento da base de dados:
     ```python
     df['cognitive_complexity'] = df['cognitive_complexity'].fillna(0.0)
     ```

### [ ] Tarefa 6: Re-executar os Testes de Hipótese e Atualizar Tabelas
* **Ação:**
  1. Após concluir as tarefas de 1 a 5 re-executando a análise de dados, rodar novamente os testes estatísticos (Mann-Whitney U e correlações de Spearman).
  2. Atualizar as tabelas do artigo com as novas médias de complexidade cognitiva, scores FQS e taxas funcionais corretas.

### [ ] Tarefa Bônus (Para a Base Consolidada Master Completa)
* **O Problema:** O registro de índice **1839** (`instruct-codegen-16B`, estratégia `I`) possui status de teste registrado como **`Unknown`**.
* **Ação:** O Bernardo deve verificar por que o pipeline de testes gerou esse status especial e corrigi-lo para `Error` ou `Fail` correspondente, de forma a eliminar qualquer status inválido da base final.

---

## Guia de Implementação e Código de Exemplo (Python)

Hierarquia de tarefas para ajudar o **Bernardo** no processamento de testes:

### Calculando o `pass_val` Real a partir do JSON de Testes (Tarefa 4)
O pipeline de testes salva os dados brutos no caminho `output/result/[Model]_[Strategy]_class_result.json`. O Bernardo pode processá-los com o seguinte trecho:

```python
import json

# Exemplo de leitura de um arquivo de teste de modelo
with open('output/result/gpt-3.5-turbo_H_class_result.json', 'r') as f:
    test_results = json.load(f)

# Loop por tarefa e testes
for task_id, task_data in test_results.items():
    for sample_key, test_metrics in task_data.items():
        # test_metrics possui chaves: 'testsRun', 'errors', 'failures'
        tests_run = test_metrics.get('testsRun', 0)
        errors = test_metrics.get('errors', 0)
        failures = test_metrics.get('failures', 0)
        
        # Fórmula correta para pass_val contínuo
        if tests_run > 0:
            pass_val = (tests_run - (errors + failures)) / tests_run
        else:
            pass_val = 0.0
            
        print(f"Classe {sample_key} | pass_val real: {pass_val:.2f}")
```

---

## Script de Validação Final (Sanity Check)

Para garantir que a base consolidada final reconstruída pelo Bernardo esteja **100% livre de erros**, ele pode executar o seguinte script de validação de sanidade sobre o arquivo CSV corrigido. O script apontará imediatamente se alguma anomalia persistir:

```python
import pandas as pd

def check_database_sanity(csv_path):
    df = pd.read_csv(csv_path)
    errors_found = 0
    
    # 1. Validar NCLOC = 0 com FQS > 0
    bug_fqs_vazio = df[(df['ncloc'] == 0.0) & (df['fqs'] > 0.0)]
    if len(bug_fqs_vazio) > 0:
        print(f"[X] ERRO: Encontrados {len(bug_fqs_vazio)} arquivos com NCLOC = 0 mas FQS > 0!")
        errors_found += 1
        
    # 2. Validar NaNs na base
    nans = df.drop(columns=['cognitive_complexity']).isna().any().sum()
    if nans > 0:
        print("[X] ERRO: Existem valores nulos (NaN) em colunas que não deveriam conter!")
        errors_found += 1
        
    # 3. Validar se cognitive_complexity ainda tem NaNs
    cc_nans = df['cognitive_complexity'].isna().sum()
    if cc_nans > 0:
        print(f"[X] ERRO: Existem {cc_nans} valores nulos (NaN) na complexidade cognitiva! Preencher com 0.0.")
        errors_found += 1
        
    # 4. Validar FQS fora do limite lógico [0.0, 1.0]
    out_of_bounds = df[(df['fqs'] < 0.0) | (df['fqs'] > 1.0)]
    if len(out_of_bounds) > 0:
        print(f"[X] ERRO: Encontrados {len(out_of_bounds)} registros com FQS fora de [0.0, 1.0]!")
        errors_found += 1
        
    # 5. Validar pass_val zerado em PartialSuccess
    partial_zero = df[(df['status'] == 'PartialSuccess') & (df['pass_val'] == 0.0)]
    if len(partial_zero) > 0:
        print(f"[X] AVISO: Existem {len(partial_zero)} registros de PartialSuccess com pass_val zerado. Corrigir para taxa real.")
        errors_found += 1
        
    # 6. Validar status inválidos (como Unknown)
    invalid_status = df[~df['status'].isin(['Success', 'Fail', 'Error', 'PartialSuccess'])]
    if len(invalid_status) > 0:
        print(f"[X] ERRO: Encontrados {len(invalid_status)} registros com status inválidos (ex: Unknown)!")
        errors_found += 1
        
    if errors_found == 0:
        print("[✓] PARABÉNS: A base de dados passou em todos os testes de sanidade e está 100% confiável!")
    else:
        print(f"[!] ATENÇÃO: Foram identificadas {errors_found} inconsistências. Revise os passos anteriores.")

# Bernardo pode rodar assim:
# check_database_sanity('sonar_metrics_consolidated_master_corrigida.csv')
```

---

## Detalhamento Técnico das Anomalias Encontradas

### Detalhamento A: O Bug da Sanitização e o "FQS Perfeito" em Arquivos Vazios

Em **16 instâncias** no recorte, o script de limpeza apagou todo o código útil. Abaixo estão listadas as instâncias para auditoria do Bernardo. Atenção especial aos 2 casos de sucesso funcional (`Success`) que ganharam score `fqs = 1.0` de forma incorreta:

| Modelo | Arquivo / Classe | Status | NCLOC | SQALE Index | FQS | Observação / Erro |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **wizardcoder-15b-v1.0** | `BankAccountSuccess.py` | **Success** | **0.0** | 0.0 | **1.0** | **BUG: FQS perfeito em arquivo vazio** |
| **wizardcoder-15b-v1.0** | `NLPDataProcessor2Success.py` | **Success** | **0.0** | 0.0 | **1.0** | **BUG: FQS perfeito em arquivo vazio** |
| gpt-3.5-turbo | `CalendarUtilError.py` | Error | 0.0 | 0.0 | 0.0 | Correto (fqs zerado por ser falha) |
| gpt-3.5-turbo | `RegexUtilsError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| gpt-3.5-turbo | `SplitSentenceFail.py` | Fail | 0.0 | 0.0 | 0.0 | Correto |
| gpt-4-turbo | `SplitSentenceFail.py` | Fail | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `CalendarUtilError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `ClassRegistrationSystemError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `ExpressionCalculatorError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `HRManagementSystemError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `InterpolationFail.py` | Fail | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `KappaCalculatorFail.py` | Fail | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `MahjongConnectError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `MinesweeperGameError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `PageUtilError.py` | Error | 0.0 | 0.0 | 0.0 | Correto |
| wizardcoder-15b-v1.0 | `SplitSentenceFail.py` | Fail | 0.0 | 0.0 | 0.0 | Correto |

### Detalhamento B: A Distorção Estatística dos NaNs na Complexidade Cognitiva

Os NaNs de complexidade cognitiva estão inflacionando artificialmente as médias por não serem tratados como `0.0`. A tabela abaixo quantifica a distorção no recorte que o Bernardo precisa corrigir com a substituição de NaNs por zero:

| Modelo | Total de Linhas | Ocorrências de `NaN` | Média Ignorando NaNs (Distorcida) | Média Correta (Substituindo NaN por 0.0) | Inflação Artificial |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **wizardcoder-15b-v1.0** | 100 | **62 (62%)** | **9.92** | **3.77** | **+163%** |
| **gpt-4-turbo** | 100 | **26 (26%)** | **8.82** | **6.53** | **+35%** |
| **gpt-3.5-turbo** | 100 | **23 (23%)** | **10.09** | **7.77** | **+30%** |
| **groundtruth** | 100 | **9 (9%)** | **12.98** | **11.82** | **+10%** |

### Detalhamento C: Perda de Granularidade Funcional no `pass_val`

* **Inconsistência Identificada:** No banco de dados consolidado completo, existem **137 registros** com status `PartialSuccess` (e **24 registros** no seu recorte). Em 100% dessas execuções, o valor da coluna `pass_val` está gravado como `0.0`.
* **Consequência:** A planilha descarta a informação estatística de quantos testes passaram em execuções de sucesso parcial. O cálculo correto deve ser dinâmico com base nos resultados das suites de testes unitários salvos no pipeline do ClassEval.
