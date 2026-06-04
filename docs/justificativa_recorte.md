# Justificativa 1: Seleção dos Modelos Baseada no Limiar de Viabilidade Funcional

A seleção dos modelos para a análise refinada de qualidade de código baseia-se nos dados empíricos de desempenho reportados na **Tabela 7** (*"Pass@k with Nucleus Sampling on ClassEval"*) do artigo original do ClassEval. Os dados de taxa de acerto em nível de classe (Class-level Pass@1) sob amostragem Nucleus para os 11 modelos avaliados são apresentados a seguir:

| Posição | Modelo | Pass@1 (Class-level) | Tipo de Modelo |
|:---:|:---|:---:|:---:|
| 1º | **GPT-4** | **37,6%** | Comercial Proprietário (Estado da Arte) |
| 2º | **GPT-3.5** | **29,6%** | Comercial Proprietário |
| 3º | **WizardCoder** | **12,2%** | Open-source (Melhor da categoria) |
| 4º | Instruct-StarCoder | 10,2% | Open-source |
| 5º | SantaCoder | 8,6% | Open-source |
| 6º | Instruct-CodeGen | 8,2% | Open-source |
| 7º | CodeGeeX | 7,2% | Open-source |
| 8º | InCoder | 6,2% | Open-source |
| 9º | Vicuna | 3,0% | Open-source Geral |
| 10º | ChatGLM | 1,4% | Open-source Geral |
| 11º | PolyCoder | 1,4% | Open-source |

A delimitação do estudo para focar nos modelos **GPT-4**, **GPT-3.5** e **WizardCoder** sustenta-se em duas evidências auditáveis extraídas diretamente desses resultados:

### 1. Representatividade dos Lideres de Categoria
Os três modelos selecionados representam o topo de desempenho em suas respectivas categorias no benchmark:
* **GPT-4** e **GPT-3.5** constituem a liderança absoluta de geração de classes funcionais, superando significativamente todos os demais modelos avaliados.
* **WizardCoder** posiciona-se como o terceiro colocado geral no benchmark e o **modelo de código aberto (open-source) com melhor desempenho** para a geração de código em nível de classe.

### 2. Viabilidade Funcional para Análise de Qualidade de Código
Para realizar análises de qualidade de código estatisticamente significativas (como cálculo de métricas SonarQube, Code Smells e Dívida Técnica sobre os códigos corretos), é necessário que o modelo apresente uma capacidade mínima de geração de código semanticamente correto (viabilidade funcional).
* A partir do quarto colocado (Instruct-StarCoder, 10,2%), o desempenho cai para menos de 10% (SantaCoder 8,6%, Instruct-CodeGen 8,2%), atingindo patamares críticos próximos a zero em modelos de propósito geral (Vicuna 3,0%, ChatGLM 1,4%) e modelos menores (PolyCoder 1,4%).
* Modelos abaixo do limiar do WizardCoder falham em gerar código correto na imensa maioria das tarefas em nível de classe. A inclusão desses modelos na análise estatística de qualidade geraria amostras corretas muito pequenas e inconsistentes, introduzindo ruído estatístico severo (excesso de valores ausentes ou indeterminados em métricas de qualidade de código funcional).
