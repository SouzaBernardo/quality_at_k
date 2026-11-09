# Consolidated Statistical Analysis Report (400-Record Dataset)

This report summarizes the functional correctness and software quality (SonarQube) analyses of the **ClassEval** benchmark runs (temperature 0, Holistic generation), covering GPT-4-Turbo, GPT-3.5-Turbo, WizardCoder-15B-V1.0, and GroundTruth.

> These statistics reflect the 400-record dataset analyzed with the previous SonarQube environment. The current pipeline uses a different SonarQube instance and Python quality profile; regenerate this report before comparing its figures with current scan results.

---

## 1. Overall Performance (Means by LLM and GroundTruth)

This table shows unit-test outcomes and mean SonarQube static-analysis metrics for each group.

| Model                |   Tasks |   Success (%) |   Partial Success (%) |   Fail (%) |   Error (%) |   Avg NCLOC |   Avg Cyclomatic |   Avg Cognitive |   Avg Code Smells |   Avg Sqale (Debt min) |   Quality@1 (FQS) |
|:---------------------|--------:|--------------:|----------------------:|-----------:|------------:|------------:|-----------------:|----------------:|------------------:|-----------------------:|------------------:|
| GroundTruth          |     100 |           100 |                     0 |          0 |           0 |       34.84 |            11.65 |           11.82 |              1.13 |                   6.29 |          0.983628 |
| GPT-4-Turbo          |     100 |            37 |                    13 |         20 |          30 |       25.97 |             8.78 |            6.53 |              0.55 |                   2.3  |          0.460208 |
| GPT-3.5-Turbo        |     100 |            26 |                     8 |         26 |          40 |       28.33 |             9.18 |            7.9  |              0.69 |                   2.69 |          0.308721 |
| WizardCoder-15B-V1.0 |     100 |            10 |                     3 |         22 |          65 |       19.28 |             7.24 |            4.82 |              0.75 |                   3.79 |          0.117177 |

*Note: `Quality@1 (FQS)` was calculated using the proposed formula with a scaling factor of $\beta = 0.1$.*

---

## 2. RQ1: Relationship Between Functional Correctness and Structural Quality

We investigated whether functional code differs significantly in structural metrics from code that failed.

### Hypothesis Test (Two-Sided Mann–Whitney U by Model)
| Model                | Metric                |   U Statistic |    p-value | Significant (5%)   |
|:---------------------|:----------------------|--------------:|-----------:|:-------------------|
| GPT-4-Turbo          | Cognitive Complexity  |        1200   | 0.730406   | No                 |
| GPT-4-Turbo          | Cyclomatic Complexity |        1167   | 0.568082   | No                 |
| GPT-3.5-Turbo        | Cognitive Complexity  |        1069.5 | 0.703527   | No                 |
| GPT-3.5-Turbo        | Cyclomatic Complexity |        1057.5 | 0.640383   | No                 |
| WizardCoder-15B-V1.0 | Cognitive Complexity  |         803   | 0.00642196 | Yes                |
| WizardCoder-15B-V1.0 | Cyclomatic Complexity |         659   | 0.336708   | No                 |

### Cognitive Complexity Comparison (GPT-4 vs. WizardCoder)
* U statistic: 6571.0
* **p-value: 6.46e-05**
* *Result:* We reject the null hypothesis ($H_{10}$) at the 5% significance level.

---

## 3. RQ2: Evaluation and Validation of the `Quality@1` (FQS) Metric

We evaluated the statistical significance of the quality penalty in FQS compared with classical Pass@1.

### Wilcoxon Test (Pass@1 vs. Quality@1)
| Model                |   W Statistic |     p-value | Significant (5%)   |
|:---------------------|--------------:|------------:|:-------------------|
| GPT-4-Turbo          |             0 | 0.00220034  | Yes                |
| GPT-3.5-Turbo        |             0 | 0.00768579  | Yes                |
| WizardCoder-15B-V1.0 |             0 | 0.0431144   | Yes                |
| All LLMs Pooled      |             0 | 8.21499e-06 | Yes                |

### Statistical Validation Findings
1. **Silent Technical Debt (LLMs):** In **31.51%** of functionally successful LLM cases (73 files), technical debt reduced the final quality score.
2. **Silent Technical Debt (Overall):** Of the **173** successful cases in the dataset (including GroundTruth), **60** files (**34.68%**) contain silent technical debt.
3. **Convergent Validation (Spearman Correlation for LLM Successes):**
   * The Spearman correlation between `Quality@1` and *Code Smells* is **-0.9825** (p-value: 1.52e-53), indicating strong construct validity with respect to maintainability.
   * The correlation with *Cognitive Complexity* is **0.0190** (p-value: 8.74e-01), indicating no significant correlation among successful cases.

---

## 4. Discussion: Human Reference Analysis (GroundTruth vs. GPT-4-Turbo)

This section presents statistical comparisons between functionally successful GroundTruth and GPT-4-Turbo solutions, and identifies cases where LLMs achieved higher quality scores.

### GroundTruth Findings
* **Classes with Technical Debt:** **37** of the 100 human-reference classes (**37.00%**) have silent technical debt (FQS < 1.0).

### Tasks Where LLMs Outperformed GroundTruth in Structural Quality (FQS_LLM = 1.0 > FQS_GT)
| Task | FQS GT | GPT-4 | GPT-3.5 | WizardCoder |
|:--------------------|---------:|--------:|----------:|--------------:|
| BalancedBrackets.py |   0.8704 |       1 |         1 |             1 |
| BigNumCalculator.py |   0.9839 |       1 |         1 |             0 |
| Calculator.py       |   0.9738 |       1 |         0 |             0 |
| ShoppingCart.py     |   0.9706 |       1 |         1 |             0 |
| TimeUtils.py        |   0.9259 |       0 |         1 |             1 |
| ZipFileProcessor.py |   0.9375 |       1 |         0 |             0 |

### Statistical Comparison (Mann–Whitney U for Successful Solutions: GT vs. GPT-4-Turbo)
This comparison includes only functionally successful implementations ($N_{GT} = 100$, $N_{GPT4} = 37$).

| Metric | GT Mean | GPT-4 Mean | U Statistic | p-value | Significant (5%) |
|:--------------------------|-----------:|--------------:|--------------:|------------:|:---------------------|
| Cognitive Complexity | 11.82 | 5.5676 | 2541.5 | 0.000786148 | Yes |
| Cyclomatic Complexity | 11.65 | 8.3243 | 2493 | 0.00178866 | Yes |
| Code Smells | 1.13 | 0.5946 | 2071 | 0.205596 | No |
| Technical Debt (min) | 6.29 | 2.5405 | 2091 | 0.168138 | No |
| FQS | 0.9836 | 0.9875 | 1692 | 0.367029 | No |
| Code Size (NCLOC) | 34.84 | 24.6757 | 2735 | 1.78378e-05 | Yes |
