# Justificativa 2: Foco na Geração Holística (Relevância Prática e Coesão de Software)

O foco na estratégia de **Geração Holística (Holistic Generation)** — em que a classe inteira é gerada de uma única vez a partir do esqueleto e da especificação da classe — baseia-se em evidências empíricas do próprio artigo do ClassEval e em princípios fundamentais de engenharia de software orientado a objetos.

---

## 1. Evidências Empíricas do Artigo ClassEval

No artigo original do ClassEval, os autores identificaram os seguintes comportamentos nas estratégias de geração (Seção 5.2, Finding 3):

* **Melhor Desempenho nos Modelos de Alta Capacidade:** O artigo demonstra que para os modelos de maior desempenho (**GPT-4** e **GPT-3.5**), a geração holística é a melhor estratégia de geração de código. De acordo com os autores:
  > *"generating the entire class all at once is actually beneficial for them to fully capture and utilize the constraints between each method, leading to better class-level code correctness."*
  *(gerar a classe inteira de uma vez só é benéfico para eles capturarem e utilizarem plenamente as restrições entre cada método, levando a uma melhor correção do código no nível de classe).*

* **Limitação Tecnológica de Modelos Menores como Causa de Desvio:** Os modelos inferiores performaram melhor nas estratégias método-a-método (*incremental* e *compositional*) apenas devido a limitações de arquitetura da época (2023), como a incapacidade de lidar com contextos de entrada longos (*"limited capability of utilizing long input contexts"*) e a perda de atenção em informações no meio do prompt (*"lost in the middle"*).

---

## 2. Coesão e Gerenciamento de Estado de Software

A estratégia de geração holística é a única que avalia a integridade estrutural e o design de software de forma realista no paradigma orientado a objetos, sustentada por duas evidências conceituais e empíricas:

### A. Raciocínio de Dependência Inter-Método (Evidência Empírica do ClassEval)
Na Seção 5.3 (**RQ3: Dependency Generation**) e na **Figura 7** do artigo do ClassEval, os autores analisam a taxa de sucesso dos modelos em gerar código contendo dependências de campos (`DEP(F)`) e dependências de outros métodos internos (`DEP(M)`). 
* Os dados mostram que os modelos enfrentam uma dificuldade significativamente maior para gerar códigos corretos que invocam outros métodos da mesma classe (`DEP(M)`). 
* A geração holística força o LLM a resolver esse grafo de dependências e chamadas internas síncronas de uma única vez no mesmo espaço de atenção, fornecendo o teste mais rigoroso sobre o raciocínio arquitetural do modelo.

### B. Coesão Interna (Fundamentação em Engenharia de Software)
A qualidade estrutural de uma classe está diretamente associada à sua coesão. Métricas consolidadas como **LCOM (*Lack of Cohesion of Methods*)** estabelecem que os métodos de uma classe devem compartilhar atributos e estados em comum. 
* Avaliar a qualidade do código gerado (como Code Smells e Dívida Técnica) requer analisar a classe como uma unidade coesa integrada.
* A geração holística simula fielmente a escrita de classes coesas na prática, enquanto abordagens isoladas (como gerar métodos separadamente para depois combiná-los) ignoram as dependências de estado compartilhado e mascaram defeitos de acoplamento que geram cheiros de código na produção.
