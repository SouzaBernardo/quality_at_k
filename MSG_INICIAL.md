Olá! Estou desenvolvendo meu TCC e preciso continuar um trabalho que estava fazendo.

Leia o arquivo @CONTEXTO_SESSAO.md para entender o estado atual do projeto.

Resumindo rapidamente: estou calculando uma métrica chamada **Quality@1** que combina Pass@1 (sucesso funcional) com métricas de qualidade do SonarQube para avaliar código gerado por LLMs no benchmark ClassEval. Já temos os scripts funcionando e os CSVs gerados.

Os próximos passos que podemos tomar (escolha um ou sugira outro):
1. Analisar os resultados do `fqs_aggregated.csv` — comparar modelos e estratégias, gerar visualizações ou tabelas LaTeX
2. Resolver o GroundTruth sem FQS (atribuir `pass_val=1.0` ou criar coluna separada `quality_score`)
3. Investigar por que ~70% dos registros têm `sqale_index=NaN` e se isso afeta as conclusões
4. Qualquer outra análise que precisar
