#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$SCRIPT_DIR/../output/solutions"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
COMPOSE_FILE="$PROJECT_ROOT/compose.yaml"
COMPOSE_ENV_FILE="$PROJECT_ROOT/.env"
SONAR_HOST="${SONAR_HOST_URL:-http://sonarqube:9000}"
TOKEN_FILE="$SCRIPT_DIR/.sonar-tokens"

if [[ ! -f "$COMPOSE_ENV_FILE" ]]; then
    echo "ERROR: platform config not found. Copy .env.windows or .env.macos to .env first." >&2
    exit 1
fi

if [[ ! -f "$TOKEN_FILE" ]]; then
    echo "ERROR: tokens not found. Run ./scripts/setup_sonar_projects.sh first." >&2
    exit 1
fi

# The setup script creates this local, Git-ignored file with mode 600.
source "$TOKEN_FILE"

docker compose --env-file "$COMPOSE_ENV_FILE" -f "$COMPOSE_FILE" build python

run_analysis() {
    local project_key="$1"
    local token="$2"

    if [[ -z "$token" ]]; then
        echo "ERROR: no token configured for $project_key." >&2
        return 1
    fi

    echo ""
    echo "==> Analyzing: $project_key"
    local project_dir="$BASE_DIR/$project_key"
    if [[ ! -d "$project_dir" ]]; then
        echo "ERROR: project directory not found: $project_dir" >&2
        return 1
    fi

    cp "$PROJECT_ROOT/sonar-project.properties" "$project_dir/"
    docker compose --env-file "$COMPOSE_ENV_FILE" -f "$COMPOSE_FILE" run --rm --no-deps \
        --entrypoint pysonar \
        --workdir "/app/output/solutions/$project_key" \
        --env "SONAR_TOKEN=$token" \
        python \
        --sonar-host-url="$SONAR_HOST" \
        --sonar-project-key="$project_key"
}

run_analysis "GPT-3.5-Turbo"        "${SONAR_TOKEN_GPT_35_TURBO:-}"
run_analysis "GPT-4-Turbo"          "${SONAR_TOKEN_GPT_4_TURBO:-}"
run_analysis "WizardCoder-15B-V1.0" "${SONAR_TOKEN_WIZARDCODER:-}"
run_analysis "GroundTruth"          "${SONAR_TOKEN_GROUNDTRUTH:-}"

echo ""
echo "==> All analyses completed!"
