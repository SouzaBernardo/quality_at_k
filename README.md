# Quality@K — Análise de Qualidade Estática de Código Gerado por LLMs

Este repositório contém o pipeline de análise estática utilizado no TCC *"Avaliação da Qualidade de Código Gerado por Large Language Models"*. O objetivo é investigar se código funcionalmente correto (medido pelo Pass@k do benchmark ClassEval) também apresenta boa qualidade estrutural, medida via SonarQube.

## Contexto

O benchmark [ClassEval](https://github.com/FudanSELab/ClassEval) avalia LLMs na geração de classes Python completas com 100 tarefas. Este trabalho seleciona os dois extremos de desempenho do benchmark:

| Modelo | Perfil | Pass@1 (classe) |
|--------|--------|-----------------|
| GPT-4-Turbo | Melhor desempenho | 37,6% |
| PolyCoder-2.7B | Pior desempenho | 1,4% |

Ambos são comparados com o **Ground Truth** — implementações escritas por humanos disponibilizadas pelo próprio ClassEval.

### Estratégias de Geração

Cada modelo foi avaliado em três estratégias de geração definidas pelo ClassEval:

| Sigla | Estratégia | Descrição |
|-------|-----------|-----------|
| `H` | Holística | Gera a classe completa de uma só vez |
| `I` | Incremental | Constrói método a método, usando o resultado anterior como contexto |
| `C` | Composicional | Constrói método a método de forma independente |

### Configurações de Decodificação

| Sufixo | Modo | Amostras por tarefa |
|--------|------|---------------------|
| `greedy` | Greedy (T=0) | 1 |
| `t0.2` | Nucleus Sampling (T=0,2) | 5 |

Os diretórios em `data/` combinam essas dimensões — por exemplo, `GPT-4-Turbo_method_C_greedy` representa o GPT-4-Turbo com estratégia Composicional e decodificação gulosa.

### Métricas Coletadas

- **Complexidade Cognitiva** — esforço mental para compreender o código
- **Complexidade Ciclomática** — quantidade de caminhos independentes no fluxo de execução
- **Code Smells** — indícios de más práticas que impactam manutenibilidade
- **Quality@k** — métrica proposta neste trabalho, combina as três acima em um score normalizado por LOC

## Pré-requisitos

- [Docker](https://www.docker.com/) instalado e em execução

## Executando o SonarQube

A imagem já contém todos os projetos analisados, com métricas e usuários configurados. Basta executar:

```bash
docker compose up
```

O SonarQube estará disponível em [http://localhost:9000](http://localhost:9000).

| Campo | Valor |
|-------|-------|
| Usuário | `admin` |
| Senha | `sonarLike@21` |

> Na primeira inicialização, o SonarQube pode levar alguns minutos para reconstruir o índice de busca interno a partir do banco de dados. Aguarde até a interface estar totalmente disponível.

## Reanalisando os projetos

Caso os arquivos em `data/` sejam alterados ou você queira reprocessar as análises do zero:

```bash
# certifique-se de que o SonarQube esteja rodando
docker compose up -d

./run_sonar.sh
```

O script envia cada projeto para o SonarQube via `pysonar`, usando os tokens de autenticação já configurados.

## Estrutura

```
.
├── compose.yaml               # Sobe o SonarQube com a imagem pré-populada
├── run_sonar.sh               # Reenvia todos os projetos ao SonarQube
├── sonar-project.properties   # Configuração base dos projetos Sonar
└── data/
    ├── GPT-4-Turbo_class_H_greedy/
    ├── GPT-4-Turbo_method_C_greedy/
    ├── GPT-4-Turbo_method_I_greedy/
    ├── PolyCoder-2.7B_class_H_greedy/
    ├── PolyCoder-2.7B_class_H_t0.2/
    ├── PolyCoder-2.7B_method_C_greedy/
    ├── PolyCoder-2.7B_method_C_t0.2/
    ├── PolyCoder-2.7B_method_I_greedy/
    ├── PolyCoder-2.7B_method_I_t0.2/
    └── groundTruth/
```

## Reconstruindo a imagem Docker

Se precisar publicar uma nova versão da imagem após novas análises:

```bash
# 1. Suba o SonarQube e rode as análises
docker compose up -d
./run_sonar.sh

# 2. Extraia os dados do container em execução
docker cp <container_id>:/opt/sonarqube/data ./sonarqube-data
docker cp <container_id>:/opt/sonarqube/extensions ./sonarqube-extensions

# 3. Reconstrua e publique
docker build -t beposs/class_eval_sonar:latest .
docker push beposs/class_eval_sonar:latest
```

> As pastas `sonarqube-data/` e `sonarqube-extensions/` estão no `.gitignore` — são geradas localmente apenas durante o build da imagem.
