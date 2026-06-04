#!/bin/bash

SONAR_HOST="http://localhost:9000"
SONAR_AUTH="admin:sonarLike@21"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SONAR_SH="$SCRIPT_DIR/run_sonar.sh"

criar_projeto_e_token() {
    local key="$1"

    echo ""
    echo "==> Projeto: $key"

    # Criar projeto (silencioso — falha se já existir é ignorada)
    curl -s -u "$SONAR_AUTH" -X POST \
      "$SONAR_HOST/api/projects/create" \
      -d "name=${key}&project=${key}" > /dev/null

    # Gerar token de análise com nome único por timestamp
    local token_name="token-${key}-$(date +%s)"
    local response
    response=$(curl -s -u "$SONAR_AUTH" -X POST \
      "$SONAR_HOST/api/user_tokens/generate" \
      -d "name=${token_name}&type=PROJECT_ANALYSIS_TOKEN&projectKey=${key}")

    local token
    token=$(echo "$response" | jq -r '.token // empty')

    if [ -z "$token" ]; then
        echo "    ERRO ao gerar token: $response"
        return 1
    fi

    echo "    Token: $token"

    # Substituir "" pelo token gerado na linha do projeto em run_sonar.sh
    sed -i '' -E "s|run_analysis \"${key}\"(.*)\"\"|run_analysis \"${key}\"\1\"${token}\"|" "$SONAR_SH"

    echo "    run_sonar.sh atualizado."
}

criar_projeto_e_token "GPT-3.5-Turbo"
criar_projeto_e_token "GPT-4-Turbo"
criar_projeto_e_token "WizardCoder-15B-V1.0"
criar_projeto_e_token "GroundTruth"

echo ""
echo "==> Concluído! Todos os projetos criados e run_sonar.sh atualizado."
