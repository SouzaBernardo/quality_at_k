#!/usr/bin/env bash

set -euo pipefail
umask 077

SONAR_HOST="${SONAR_HOST:-http://localhost:9000}"
SONAR_AUTH="${SONAR_AUTH:-admin:sonarLike@21}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TOKEN_FILE="$SCRIPT_DIR/.sonar-tokens"
TEMP_TOKEN_FILE="$(mktemp "$SCRIPT_DIR/.sonar-tokens.XXXXXX")"
trap 'rm -f "$TEMP_TOKEN_FILE"' EXIT

project_exists() {
    local key="$1"

    curl --fail --silent --show-error --user "$SONAR_AUTH" --get \
        --data-urlencode "projects=$key" \
        --data-urlencode "ps=1" \
        "$SONAR_HOST/api/projects/search" |
        python3 -c '
import json
import sys

try:
    projects = json.load(sys.stdin).get("components", [])
except (json.JSONDecodeError, AttributeError):
    sys.exit("ERRO: resposta inválida ao consultar projetos no SonarQube.")

sys.exit(0 if projects else 1)
'
}

criar_projeto_e_token() {
    local key="$1"
    local token_variable="$2"
    local token_name="token-${key}-$(date +%s)-$$-${RANDOM}"
    local response
    local token

    echo ""
    echo "==> Projeto: $key"

    if project_exists "$key"; then
        echo "    Projeto já existe."
    else
        curl --fail --silent --show-error --user "$SONAR_AUTH" \
            --request POST \
            --data-urlencode "name=$key" \
            --data-urlencode "project=$key" \
            "$SONAR_HOST/api/projects/create" >/dev/null
        echo "    Projeto criado."
    fi

    response=$(curl --fail --silent --show-error --user "$SONAR_AUTH" \
        --request POST \
        --data-urlencode "name=$token_name" \
        --data-urlencode "type=PROJECT_ANALYSIS_TOKEN" \
        --data-urlencode "projectKey=$key" \
        "$SONAR_HOST/api/user_tokens/generate")

    if ! token=$(printf '%s' "$response" | python3 -c '
import json
import re
import sys

try:
    token = json.load(sys.stdin).get("token", "")
except (json.JSONDecodeError, AttributeError):
    sys.exit(1)

if not isinstance(token, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", token):
    sys.exit(1)

print(token)
'); then
        echo "    ERRO: o SonarQube não retornou um token válido para $key." >&2
        return 1
    fi

    printf '%s=%s\n' "$token_variable" "$token" >> "$TEMP_TOKEN_FILE"
    echo "    Token gerado."
}

criar_projeto_e_token "GPT-3.5-Turbo" "SONAR_TOKEN_GPT_35_TURBO"
criar_projeto_e_token "GPT-4-Turbo" "SONAR_TOKEN_GPT_4_TURBO"
criar_projeto_e_token "WizardCoder-15B-V1.0" "SONAR_TOKEN_WIZARDCODER"
criar_projeto_e_token "GroundTruth" "SONAR_TOKEN_GROUNDTRUTH"

mv -f "$TEMP_TOKEN_FILE" "$TOKEN_FILE"
echo ""
echo "==> Concluído! Tokens salvos em scripts/.sonar-tokens."
