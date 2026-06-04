#!/bin/bash

set -e

SONAR_HOST="http://localhost:9000"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$SCRIPT_DIR/../output/solutions"

run_analysis() {
    local project_key="$1"
    local token="$2"

    echo ""
    echo "==> Analisando: $project_key"
    cd "$BASE_DIR/$project_key"
    cp "$SCRIPT_DIR/../sonar-project.properties" .
    pysonar \
        --sonar-host-url="$SONAR_HOST" \
        --sonar-token="$token" \
        --sonar-project-key="$project_key"
}

run_analysis "GPT-3.5-Turbo"        "sqp_6b5c9fcc578088cf5d2ffffcc42c60f1bd1f4e9a"
run_analysis "GPT-4-Turbo"          "sqp_895f43d93786c7c2467716411bd6e7722dc51dee"
run_analysis "WizardCoder-15B-V1.0" "sqp_e4f828a8ad9a6e31ce7da57ff99aff2f09d78f90"
run_analysis "GroundTruth"          "sqp_c18ec8d0fcc701c5aaf2930ba7906b9b3197461e"

echo ""
echo "==> Todas as análises concluídas!"
