#!/bin/bash

set -e

SONAR_HOST="http://localhost:9000"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$SCRIPT_DIR/data"

run_analysis() {
    local project_key="$1"
    local token="$2"
    local folder="$3"

    echo ""
    echo "==> Analisando: $project_key"
    cd "$BASE_DIR/$folder"
    cp "$SCRIPT_DIR/sonar-project.properties" .
    pysonar \
        --sonar-host-url="$SONAR_HOST" \
        --sonar-token="$token" \
        --sonar-project-key="$project_key"
}

run_analysis "GPT-4-Turbo_class_H_greedy"    "sqp_7c3870f69e4d6d05aa17b37d2ea296ece81df1dd"  "GPT-4-Turbo_class_H_greedy"
run_analysis "GPT-4-Turbo_method_C_greedy"   "sqp_1e64cba94dbc2faca144fe9d5fe091ace91001f0"  "GPT-4-Turbo_method_C_greedy"
run_analysis "GPT-4-Turbo_method_I_greedy"   "sqp_2d48d1b80005d277303169f8c230c9be1554154e"  "GPT-4-Turbo_method_I_greedy"
run_analysis "PolyCoder-2.7B_class_H_greedy" "sqp_cfa345792dd107368e1ba75428708b91a6bd67b3"  "PolyCoder-2.7B_class_H_greedy"
run_analysis "PolyCoder-2.7B_class_H_t0.2"  "sqp_60564faf990f7819fbac21c927b7ab26e838f5e0"  "PolyCoder-2.7B_class_H_t0.2"
run_analysis "PolyCoder-2.7B_method_C_greedy" "sqp_bd0b6c3a59fbbb969673a56e6940941cab5fb993" "PolyCoder-2.7B_method_C_greedy"
run_analysis "PolyCoder-2.7B_method_C_t0.2" "sqp_1964ac029ca62b37648c53483031656737778301"  "PolyCoder-2.7B_method_C_t0.2"
run_analysis "PolyCoder-2.7B_method_I_greedy" "sqp_075b3f65ba89f6da7a5bcf99821a43ad02227ccc" "PolyCoder-2.7B_method_I_greedy"
run_analysis "PolyCoder-2.7B_method_I_t0.2" "sqp_009711286292167397386dc4189448689bedb28a"  "PolyCoder-2.7B_method_I_t0.2"
run_analysis "GroundTruth"                  "sqp_ecd939b4a8a31274b3144a83ae6bdeb9e887a416"  "groundTruth"

echo ""
echo "==> Todas as análises concluídas!"
