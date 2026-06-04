"""
Validates compute_fqs against the test cases from the paper table (β = 0.1).

Tarefa | Pass@1 | NCLOC | SQALE | Expected
-------|--------|-------|-------|----------
t1     |   0    |   0   |   0   |  0.000
t2     |   1    |  30   |   0   |  1.000
t3     |   1    |  50   |  15   |  0.970
t4     |   1    |  25   |  60   |  0.760
"""

from compute_fqs import compute_fqs

TEST_CASES = [
    {"name": "t1", "pass_at_1": 0, "sqale_index":  0, "ncloc":  0, "expected": 0.000},
    {"name": "t2", "pass_at_1": 1, "sqale_index":  0, "ncloc": 30, "expected": 1.000},
    {"name": "t3", "pass_at_1": 1, "sqale_index": 15, "ncloc": 50, "expected": 0.970},
    {"name": "t4", "pass_at_1": 1, "sqale_index": 60, "ncloc": 25, "expected": 0.760},
    {"name": "t5", "pass_at_1": 0, "sqale_index": 10, "ncloc": 19, "expected": 0.000},
    {"name": "t6", "pass_at_1": 0, "sqale_index": 10, "ncloc": 19, "expected": 0.000},
    {"name": "t7", "pass_at_1": 1, "sqale_index": 0, "ncloc": 18, "expected": 1.000},
    {"name": "t8", "pass_at_1": 1, "sqale_index": 5, "ncloc": 37, "expected": 0.9864864864864865},
    {"name": "t9", "pass_at_1": 1, "sqale_index": 25, "ncloc": 16, "expected": 0.84375},
    {"name": "t10", "pass_at_1": 1, "sqale_index": 2, "ncloc": 18, "expected": 0.9888888888888889},
]

TOLERANCE = 1e-6


def run_tests() -> None:
    passed = 0
    for case in TEST_CASES:
        result = compute_fqs(case["pass_at_1"], case["sqale_index"], case["ncloc"])
        ok = result is not None and abs(result - case["expected"]) < TOLERANCE
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] {case['name']}: "
            f"compute_fqs({case['pass_at_1']}, {case['sqale_index']}, {case['ncloc']}) "
            f"= {result}  (expected {case['expected']:.3f})"
        )
        if ok:
            passed += 1

    print(f"\n{passed}/{len(TEST_CASES)} tests passed.")
    if passed != len(TEST_CASES):
        raise SystemExit(1)


if __name__ == "__main__":
    run_tests()
