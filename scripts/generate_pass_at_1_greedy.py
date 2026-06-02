import csv
import json
import pathlib
from scipy.special import comb

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def cal_pass_at_k(n, k, k_success):
    total_combinations = comb(k, n)
    if k - k_success >= n:
        without_k_success_combinations = comb(k - k_success, n)
    else:
        without_k_success_combinations = 0

    with_k_success_combinations = total_combinations - without_k_success_combinations

    pass_at_k = with_k_success_combinations / total_combinations

    return pass_at_k


def task_sort_key(task_id):
    # Sort SE-Eval_0..SE-Eval_99 numerically
    return int(task_id.split("_")[-1])


with open(PROJECT_ROOT / "data" / "ClassEval_data.json", encoding="utf-8") as f:
    classeval_data = json.load(f)
task_to_class = {f"SE-Eval_{i}": item["class_name"] for i, item in enumerate(classeval_data)}

with open(PROJECT_ROOT / "output" / "result" / "detailed_result.json", encoding="utf-8") as f:
    data = json.load(f)

greedy_keys = sorted(k for k in data if "(greedy)" in k)

STATUS_MAP = {
    'class_success': 'Success',
    'class_partial_success': 'PartialSuccess',
    'class_fail': 'Fail',
}

rows = []
for model_key in greedy_keys:
    model_name = model_key.replace("(greedy)", "").strip()
    all_tasks = sorted(task_to_class.keys(), key=task_sort_key)
    for task in all_tasks:
        task_data = data[model_key].get(task, {})
        test_class = task_data.get("TestClass", {})
        class_success = test_class.get("class_success", 0)
        # greedy: n=1, k=1
        pass_at_1 = cal_pass_at_k(n=1, k=1, k_success=class_success)

        class_each = test_class.get("ClassEachTestResult", [])
        if not class_each:
            status = 'Unknown'
        else:
            has_error = any(
                isinstance(v, dict) and v.get('EachTestResult', [''])[0] == 'error'
                for k, v in task_data.items()
                if k != 'TestClass'
            )
            status = 'Error' if has_error else STATUS_MAP.get(class_each[0], 'Unknown')

        rows.append({"model": model_name, "task": task_to_class.get(task, task), "pass@1_value": pass_at_1, "status": status})

output_path = PROJECT_ROOT / "classeval_quality" / "pass_at_1_greedy_per_task.csv"
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "task", "pass@1_value", "status"])
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV gerado: {output_path}")
print(f"Total de linhas: {len(rows)} ({len(greedy_keys)} modelos × 100 tarefas)")
