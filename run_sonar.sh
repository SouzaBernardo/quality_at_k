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

run_analysis "ChatGLM_100_c_t0"               "sqp_cd934d068ca75e16128b04eacb496fd25272399a"                                            "ChatGLM_100_c_t0"
run_analysis "ChatGLM_100_m_dire"              "sqp_37d8ab4c7c6606d7db669ff5fd57d650b387a056"                                            "ChatGLM_100_m_dire"
run_analysis "ChatGLM_100_m_iter"              "sqp_03fc1302c0f55549c58cbd73b0caab76a6b10a82"                                            "ChatGLM_100_m_iter"
run_analysis "GPT-3.5-Turbo_class_H_greedy"   "sqp_aa5da36af894639d69f39135a99520e91eb3fae1"                                            "GPT-3.5-Turbo_class_H_greedy"
run_analysis "GPT-3.5-Turbo_method_C_greedy"  "sqp_067da9f8a0f3c010cb6719503547e9d9b96ab2e0"                                            "GPT-3.5-Turbo_method_C_greedy"
run_analysis "GPT-3.5-Turbo_method_I_greedy"  "sqp_f2a995ddd1314966915d3bd19f48850f9111485c"                                            "GPT-3.5-Turbo_method_I_greedy"
run_analysis "GPT-4-Turbo_class_H_greedy"     "sqp_7c3870f69e4d6d05aa17b37d2ea296ece81df1dd" "GPT-4-Turbo_class_H_greedy"
run_analysis "GPT-4-Turbo_method_C_greedy"    "sqp_1e64cba94dbc2faca144fe9d5fe091ace91001f0" "GPT-4-Turbo_method_C_greedy"
run_analysis "GPT-4-Turbo_method_I_greedy"    "sqp_2d48d1b80005d277303169f8c230c9be1554154e" "GPT-4-Turbo_method_I_greedy"
run_analysis "PolyCoder-2.7B_class_H_greedy"  "sqp_cfa345792dd107368e1ba75428708b91a6bd67b3" "PolyCoder-2.7B_class_H_greedy"
run_analysis "PolyCoder-2.7B_method_C_greedy" "sqp_bd0b6c3a59fbbb969673a56e6940941cab5fb993" "PolyCoder-2.7B_method_C_greedy"
run_analysis "PolyCoder-2.7B_method_I_greedy" "sqp_075b3f65ba89f6da7a5bcf99821a43ad02227ccc" "PolyCoder-2.7B_method_I_greedy"
run_analysis "Vicuna_100_c_t0"                "sqp_396754a048ffd2a71ae1a0f50d4133f01bc7672d"                                            "Vicuna_100_c_t0"
run_analysis "Vicuna_100_m_dire"              "sqp_0ae9ee8dc1541d028bd5823e051f29c2dfdd6a13"                                            "Vicuna_100_m_dire"
run_analysis "Vicuna_100_m_iter"              "sqp_11702aa3928742d89bac5b88bc46c3f9668cbf3d"                                            "Vicuna_100_m_iter"
run_analysis "WizardCoder-15B-V1.0_class_H_greedy"   "sqp_ab8eb1d6c01f973f5c681d9a8d5c579db2155097"                                    "WizardCoder-15B-V1.0_class_H_greedy"
run_analysis "WizardCoder-15B-V1.0_method_C_greedy"  "sqp_0b05a4321961c5784b33670e7a423aa0aaa6e454"                                    "WizardCoder-15B-V1.0_method_C_greedy"
run_analysis "WizardCoder-15B-V1.0_method_I_greedy"  "sqp_477a57c10f65b3838f537dbcc5531551207502fe"                                    "WizardCoder-15B-V1.0_method_I_greedy"
run_analysis "codegeex2-6b_class_H_greedy"   "sqp_6191031e6675bb2d173ede86ead64a564035e34c"                                            "codegeex2-6b_class_H_greedy"
run_analysis "codegeex2-6b_method_C_greedy"  "sqp_bee465497d67442bacee25e31d2e94f45a7fe1e1"                                            "codegeex2-6b_method_C_greedy"
run_analysis "codegeex2-6b_method_I_greedy"  "sqp_7dedfa4ef6bd0f3f676cf92b3bfe75309294300a"                                            "codegeex2-6b_method_I_greedy"
run_analysis "incoder_100_c_t0"              "sqp_5a2480ad937b6a343f6a38facceb4f7cfc32eb9a"                                            "incoder_100_c_t0"
run_analysis "incoder_100_m_dire"            "sqp_f16eeebabdbed1a3c0337a94a57063a0b58650ff"                                            "incoder_100_m_dire"
run_analysis "incoder_100_m_iter"            "sqp_afdc1b2bf0488f126ca6de3db1c322a61e06aaad"                                            "incoder_100_m_iter"
run_analysis "instruct-codegen-16B_class_H_greedy"   "sqp_8a4fe7d73752f2ce9879db89c156e138e491cd03"                                    "instruct-codegen-16B_class_H_greedy"
run_analysis "instruct-codegen-16B_method_C_greedy"  "sqp_cd21cf4da038a738e52510df5ddddc03c7f5543e"                                    "instruct-codegen-16B_method_C_greedy"
run_analysis "instruct-codegen-16B_method_I_greedy"  "sqp_887909ce84bafb2215ec917417568e016c33c8e5"                                    "instruct-codegen-16B_method_I_greedy"
run_analysis "santacoder-1.1B_class_H_greedy"        "sqp_de61f93dd21873fa0b873570f12ef2129c5c6851"                                    "santacoder-1.1B_class_H_greedy"
run_analysis "santacoder-1.1B_method_C_greedy"       "sqp_202ff69fc7d497cae9dd8997b45939e244abd337"                                    "santacoder-1.1B_method_C_greedy"
run_analysis "santacoder-1.1B_method_I_greedy"       "sqp_0043d6f1df7ffc584379b8b5af4fdbdefe53ed86"                                    "santacoder-1.1B_method_I_greedy"
run_analysis "starcoder-instruct-15B_class_H_greedy"  "sqp_0fe7b6e86e6b97c86a5d48f888758a60f3411228"                                   "starcoder-instruct-15B_class_H_greedy"
run_analysis "starcoder-instruct-15B_method_C_greedy" "sqp_fa8ecfd78ea5f7e12d65c1599005dc95996bb660"                                   "starcoder-instruct-15B_method_C_greedy"
run_analysis "starcoder-instruct-15B_method_I_greedy" "sqp_afb960ad3214bbd941726a69829b563f85723077"                                   "starcoder-instruct-15B_method_I_greedy"

echo ""
echo "==> Todas as análises concluídas!"
