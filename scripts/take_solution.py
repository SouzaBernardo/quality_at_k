import os
import json
import re
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

def remove_comments(texto: str) -> str:
    regex_rep_test = [
        (r'```python.*?', ''),  # must come before the generic ``` pattern
        (r'```', ''),
        (r'Please replace \'secret\' with your actual secret key for JWT decoding.', ''),
        (r'(?s)^###.*?\n', ''),  # Remove markdown headers
        (r'(?s)This code .*?$', ''),  # Remove explanatory text
        (r'(?s)In this code, .*?$', ''),  # Remove first-person commentary
        (r'(?s)Please note .*?$', '')   # Remove implementation notes
    ]

    new_texto = str(texto)
    for pattern, repl in regex_rep_test:
        new_texto = re.sub(pattern, repl, new_texto, flags=re.IGNORECASE)

    return new_texto.strip()


def get_model_key(file_name: str) -> str:
    """Map input file name to the corresponding key in detailed_result.json.

    Examples:
        GPT-4-Turbo_method_C_greedy.json -> GPT-4_C(greedy)
        PolyCoder-2.7B_method_C_t0.2.json -> PolyCoder_C
    """
    name = file_name.replace('.json', '')
    parts = name.split('_')

    raw_model = parts[0]
    if 'GPT-4' in raw_model:
        model = 'GPT-4'
    elif 'GPT-3.5' in raw_model:
        model = 'GPT-3.5'
    elif 'PolyCoder' in raw_model:
        model = 'PolyCoder'
    else:
        model = raw_model

    mode = parts[2] if len(parts) > 2 else 'C'
    greedy_suffix = '(greedy)' if 'greedy' in name else ''

    return f"{model}_{mode}{greedy_suffix}"


STATUS_MAP = {
    'class_success': 'Success',
    'class_partial_success': 'PartialSuccess',
    'class_fail': 'Fail',
}

def get_predict_status(detailed_results: dict, model_key: str, task_id: str, predict_idx: int) -> str:
    se_key = task_id.replace('ClassEval_', 'SE-Eval_')
    se_data = detailed_results.get(model_key, {}).get(se_key, {})

    if not se_data:
        return 'Unknown'

    for test_key, test_data in se_data.items():
        if test_key == 'TestClass':
            continue
        each_result = test_data.get('EachTestResult', [])
        if predict_idx < len(each_result) and each_result[predict_idx] == 'error':
            return 'Error'

    class_results = se_data.get('TestClass', {}).get('ClassEachTestResult', [])
    if predict_idx < len(class_results):
        return STATUS_MAP.get(class_results[predict_idx], 'Unknown')

    return 'Unknown'


def process_predict_item(class_name: str, class_name_idx: str, file_name: str, predictContent: str):
    file_name_without_extension = file_name.replace('.json', '')
    content_path = PROJECT_ROOT / "classeval_quality" / "output" / file_name_without_extension / class_name
    original_content_path = content_path / "original"
    filtered_content_path = content_path / "filtered"

    new_file_name = f"{class_name_idx}.py"
    save_file(predictContent, original_content_path, new_file_name)

    predict = remove_comments(predictContent)
    save_file(predict, filtered_content_path, new_file_name)

def save_file(content: str, content_path: pathlib.Path, file_name: str):
    content_path = pathlib.Path(content_path)
    content_path.mkdir(parents=True, exist_ok=True)
    file = content_path / file_name
    with file.open("w", encoding="utf-8") as f:
        f.write(content)

def main():
    input_dir = PROJECT_ROOT / "output" / "model_output_v1.0.0"
    detailed_result_path = PROJECT_ROOT / "output" / "result" / "detailed_result.json"
    input_better_llm = "GPT-4"
    input_worse_llm = "PolyCoder"
    checkValidFileName = lambda file_name: not (file_name.startswith(input_better_llm) or file_name.startswith(input_worse_llm))

    with open(detailed_result_path, "r", encoding="utf-8") as f:
        detailed_results = json.load(f)

    for file_name in os.listdir(input_dir):

        if checkValidFileName(file_name):
            continue

        model_key = get_model_key(file_name)

        input_file = input_dir / file_name
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        middleFile = file_name.replace(".json", "")
        (PROJECT_ROOT / "classeval_quality" / "output" / middleFile).mkdir(parents=True, exist_ok=True)

        for item in data:
            class_name = item.get("class_name", "UnknownClass")
            # TODO: por enquanto só to pegando a primeira classe para teste
            # if class_name != 'AccessGatewayFilter':
            #     continue
            task_id = item.get("task_id", "")

            predictArrayContent = item.get("predict", [])
            for i, predict_item in enumerate(predictArrayContent):
                status = get_predict_status(detailed_results, model_key, task_id, i)
                class_name_idx = f"{class_name}{i}{status}"
                process_predict_item(class_name, class_name_idx, file_name, predict_item)

if __name__ == "__main__":
    main()
