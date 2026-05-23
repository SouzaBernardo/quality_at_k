import os
import json
import re
import pathlib
from typing import Optional

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

'''
- guardar o jeito que veio (cru) e o que limpamos

opcoes:
    - pegar tudo de uma ia
    - ter certeza que o GPT-4 foi o melhor resultado
        - GPT-4 melhor
        - se der tempo avancar para o pior caso (Poly)
'''
def _strip_leading_prose(text: str) -> str:
    match = re.search(r'^(?:import |from |class |def |@)', text, re.MULTILINE)
    return text[match.start():] if match else text


def _strip_trailing_prose(text: str) -> str:
    text = re.sub(r'(?is)\n\n(?:In this example|In the above example|Here\'?s?\s+an?\s+example)[^\n]*.*', '', text)
    text = re.sub(r'(?s)\n\nOutput:.*', '', text)
    text = re.sub(r'(?is)\n\n(?:This completes?|This completed|The implementation is)[^\n]*.*', '', text)
    text = re.sub(r'(?is)\n\n(?:Please let me know|Please note that|Both methods have)[^\n]*.*', '', text)
    text = re.sub(r'(?is)\n\n(?:Note that|With these changes)[^\n]*.*', '', text)
    return text


_ENGLISH_WORDS_RE = re.compile(
    r'\b(?:a|an|the|all|of|in|for|from|with|to|by|and|or|that|which|'
    r'its|their|is|are|was|were|be|been|have|has|had|this|these|those)\b',
    re.IGNORECASE,
)
_PYTHON_STARTER_RE = re.compile(
    r'^(?:import|from|class|def|if|elif|else|for|while|try|except|finally|'
    r'with|return|yield|raise|pass|break|continue|assert|del|global|'
    r'nonlocal|lambda|#|@|\d|[a-z_]\w*\s*[=(.\[\'"@])',
)


def _is_prose_statement(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if not re.match(r'^[A-Z]', s):
        return False
    if not (s.endswith('.') or s.endswith(':')):
        return False
    if len(s.split()) < 4:
        return False
    if _PYTHON_STARTER_RE.match(s):
        return False
    return bool(_ENGLISH_WORDS_RE.search(s))


def _extract_last_code_block(text: str) -> str:
    """For WizardCoder format: when ### Response: appears mid-file, extract the last code block."""
    if not re.search(r'^###', text, re.MULTILINE):
        return text
    parts = re.split(r'^###[^\n]*\n?', text, flags=re.MULTILINE)
    for part in reversed(parts):
        candidate = _strip_leading_prose(part)
        if re.search(r'^(?:import |from |class |def |@)', candidate, re.MULTILINE):
            return candidate
    return text


def _strip_markdown_non_code_lines(text: str) -> str:
    """Remove markdown bullets, numbered lists, and English prose statements outside strings/comments."""
    lines = text.split('\n')
    result = []
    in_triple = False
    for line in lines:
        stripped = line.strip()
        count_dq = line.count('"""')
        count_sq = line.count("'''")
        if (count_dq % 2 == 1) or (count_sq % 2 == 1):
            in_triple = not in_triple
        if not in_triple and not stripped.startswith('#'):
            if re.match(r'^[-*]\s+', stripped):
                continue
            if re.match(r'^\d+\.\s+[A-Z]', stripped):
                continue
            if _is_prose_statement(stripped):
                continue
        result.append(line)
    return '\n'.join(result)


def remove_comments(texto: str) -> str:
    regex_rep_test = [
        (r'```python.*?', ''),  # must come before the generic ``` pattern
        (r'```', ''),
        (r'<\|[^|]*\|>', ''),  # InCoder/FIM tokenizer markers e.g. <|/ file |>
        (r'Please replace \'secret\' with your actual secret key for JWT decoding.', ''),
        (r'(?m)^###[^\n]*\n?', ''),  # Remove markdown headers (multiline)
        (r'(?s)This code .*?$', ''),  # Remove explanatory text
        (r'(?s)In this code, .*?$', ''),  # Remove first-person commentary
        (r'(?s)Please note .*?$', ''),  # Remove implementation notes
    ]

    new_texto = str(texto)
    new_texto = _extract_last_code_block(new_texto)
    for pattern, repl in regex_rep_test:
        new_texto = re.sub(pattern, repl, new_texto, flags=re.IGNORECASE)
    new_texto = _strip_markdown_non_code_lines(new_texto)
    new_texto = _strip_leading_prose(new_texto)
    new_texto = _strip_trailing_prose(new_texto)

    return new_texto.strip()


_FILE_PREFIX_TO_MODEL = {
    'GPT-4':              'GPT-4',
    'GPT-3.5':            'GPT-3.5',
    'ChatGPT':            'GPT-3.5',
    'PolyCoder':          'PolyCoder',
    'WizardCoder':        'WizardCoder',
    'codegeex2':          'CodeGeeX',
    'CodeGeeX':           'CodeGeeX',
    'instruct-codegen':   'Instruct-CodeGen',
    'santacoder':         'SantaCoder',
    'SantaCoder':         'SantaCoder',
    'starcoder-instruct': 'Instruct-StarCoder',
    'instruct-StarCoder': 'Instruct-StarCoder',
    'incoder':            'Incoder',
    'Vicuna':             'Vicuna',
    'ChatGLM':            'ChatGLM',
}


def get_model_key(file_name: str) -> Optional[str]:
    """Map input file name to the corresponding key in detailed_result.json.
    Returns None if the model is not part of the ClassEval study.

    Examples:
        GPT-4-Turbo_method_C_greedy.json -> GPT-4_C(greedy)
        starcoder-instruct-15B_class_H_greedy.json -> Instruct-StarCoder_H(greedy)
        CodeLlama-13b-Instruct-hf_method_C_greedy.json -> None
    """
    name = file_name.replace('.json', '')
    parts = name.split('_')
    raw_model = parts[0]

    model = next(
        (v for prefix, v in _FILE_PREFIX_TO_MODEL.items() if raw_model.lower().startswith(prefix.lower())),
        None,
    )
    if model is None:
        return None

    mode = parts[2] if len(parts) > 2 else 'C'
    greedy_suffix = '(greedy)' if 'greedy' in name else ''
    return f"{model}_{mode}{greedy_suffix}"


def get_model_key_v0(file_name: str) -> Optional[str]:
    """Map model_output (original ClassEval) file name to detailed_result.json key.

    Strategy codes: c → H (Holística), m_iter → I (Incremental), m_dire → C (Composicional)
    Greedy: _t0 suffix for class-level; no _rep5 suffix for method-level.

    Examples:
        ChatGLM_100_c_t0.json       -> ChatGLM_H(greedy)
        incoder_100_m_iter.json     -> Incoder_I(greedy)
        Vicuna_100_m_dire_rep5.json -> Vicuna_C
    """
    name = file_name.replace('.json', '')
    parts = name.split('_')
    raw_model = parts[0]

    model = next(
        (v for prefix, v in _FILE_PREFIX_TO_MODEL.items() if raw_model.lower().startswith(prefix.lower())),
        None,
    )
    if model is None:
        return None

    rest = parts[1:]
    if rest and rest[0] == '100':
        rest = rest[1:]

    if not rest:
        return None

    if rest[0] == 'c':
        mode = 'H'
        sampling = rest[1] if len(rest) > 1 else ''
        greedy_suffix = '(greedy)' if sampling == 't0' else ''
    elif rest[0] == 'm':
        sub = rest[1] if len(rest) > 1 else ''
        if sub == 'iter':
            mode = 'I'
        elif sub == 'dire':
            mode = 'C'
        else:
            return None
        greedy_suffix = '' if 'rep5' in rest else '(greedy)'
    else:
        return None

    return f"{model}_{mode}{greedy_suffix}"


def _is_greedy_v0(file_name: str) -> bool:
    """Select greedy/T0 files from model_output directory.

    Class-level (_c_): requires _t0 sampling (excludes _5).
    Method-level (_m_): requires absence of _rep5 (default = greedy).
    """
    name = file_name.replace('.json', '')
    if '_m_' in name:
        return 'rep5' not in name
    return '_t0' in name


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
    detailed_result_path = PROJECT_ROOT / "output" / "result" / "detailed_result.json"
    with open(detailed_result_path, "r", encoding="utf-8") as f:
        detailed_results = json.load(f)

    input_dir = PROJECT_ROOT / "output" / "model_output_v1.0.0"
    for file_name in os.listdir(input_dir):
        if 'greedy' not in file_name:
            continue

        model_key = get_model_key(file_name)
        if model_key is None:
            continue

        input_file = input_dir / file_name
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        middleFile = file_name.replace(".json", "")
        (PROJECT_ROOT / "classeval_quality" / "output" / middleFile).mkdir(parents=True, exist_ok=True)

        for item in data:
            class_name = item.get("class_name", "UnknownClass")
            task_id = item.get("task_id", "")

            predictArrayContent = item.get("predict", [])
            for i, predict_item in enumerate(predictArrayContent):
                status = get_predict_status(detailed_results, model_key, task_id, i)
                class_name_idx = f"{class_name}{status}"
                process_predict_item(class_name, class_name_idx, file_name, predict_item)

    input_dir_v0 = PROJECT_ROOT / "output" / "model_output"
    look_to_LLM = ["chatglm", "incoder", "vicuna"]

    for file_name in os.listdir(input_dir_v0):
        if not _is_greedy_v0(file_name):
            continue

        if not any(file_name.lower().startswith(llm) for llm in look_to_LLM):
            continue

        model_key = get_model_key_v0(file_name)
        if model_key is None:
            continue

        input_file = input_dir_v0 / file_name
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        middleFile = file_name.replace(".json", "")
        (PROJECT_ROOT / "classeval_quality" / "output" / middleFile).mkdir(parents=True, exist_ok=True)

        for item in data:
            class_name = item.get("class_name", "UnknownClass")
            task_id = item.get("task_id", "")

            for i, predict_item in enumerate(item.get("predict", [])):
                status = get_predict_status(detailed_results, model_key, task_id, i)
                class_name_idx = f"{class_name}{status}"
                process_predict_item(class_name, class_name_idx, file_name, predict_item)

if __name__ == "__main__":
    main()
