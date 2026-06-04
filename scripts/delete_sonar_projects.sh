#!/bin/bash

SONAR_HOST="http://localhost:9000"
SONAR_AUTH="admin:sonarLike@21"

delete_project() {
    local key="$1"

    echo "==> Deletando: $key"

    local response
    response=$(curl -s -o /dev/null -w "%{http_code}" -u "$SONAR_AUTH" -X POST \
      "$SONAR_HOST/api/projects/delete" \
      -d "project=${key}")

    if [ "$response" = "204" ]; then
        echo "    OK"
    else
        echo "    ERRO (HTTP $response)"
    fi
}

delete_project "GPT-3.5-Turbo"
delete_project "GPT-4-Turbo"
delete_project "WizardCoder-15B-V1.0"
delete_project "GroundTruth"

echo ""
echo "==> Concluído!"
