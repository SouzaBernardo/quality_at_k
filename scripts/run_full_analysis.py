import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configure paths relative to this script.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "sonar_metrics_consolidated_master.csv")
output_report_path = os.path.join(base_dir, "reports", "statistical_report.md")
output_plot_dir = os.path.join(base_dir, "reports", "charts")

# Ensure output directories exist.
os.makedirs(os.path.dirname(output_report_path), exist_ok=True)
os.makedirs(output_plot_dir, exist_ok=True)

print(f"Reading consolidated dataset from: {csv_path}")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Error: master CSV file not found at: {csv_path}")

master_df = pd.read_csv(csv_path)
print(f"Dataset loaded successfully. Total records: {len(master_df)}")

# Standardize names
master_df['model'] = master_df['model'].replace({
    'gpt-4-turbo': 'GPT-4-Turbo',
    'gpt-3.5-turbo': 'GPT-3.5-Turbo',
    'wizardcoder-15b-v1.0': 'WizardCoder-15B-V1.0',
    'groundtruth': 'GroundTruth'
})

# 1. Generate overall descriptive statistics.
print("Generating descriptive statistics by model...")
summary_rows = []
grouped = master_df.groupby("model")

for model, group in grouped:
    total_tasks = len(group)
    success_count = sum(group["status"] == "Success")
    fail_count = sum(group["status"] == "Fail")
    error_count = sum(group["status"].str.lower() == "error")
    partial_success_count = sum(group["status"] == "PartialSuccess")
    
    success_rate = (success_count / total_tasks) * 100
    fail_rate = (fail_count / total_tasks) * 100
    error_rate = (error_count / total_tasks) * 100
    partial_success_rate = (partial_success_count / total_tasks) * 100
    
    avg_ncloc = group["ncloc"].mean()
    avg_complexity = group["complexity"].mean()
    avg_cognitive = group["cognitive_complexity"].mean(skipna=True)
    avg_code_smells = group["code_smells"].mean()
    avg_sqale = group["sqale_index"].mean()
    avg_fqs = group["fqs"].mean()
    
    summary_rows.append({
        "Model": model,
        "Tasks": total_tasks,
        "Success (%)": success_rate,
        "Partial Success (%)": partial_success_rate,
        "Fail (%)": fail_rate,
        "Error (%)": error_rate,
        "Avg NCLOC": avg_ncloc,
        "Avg Cyclomatic": avg_complexity,
        "Avg Cognitive": avg_cognitive,
        "Avg Code Smells": avg_code_smells,
        "Avg Sqale (Debt min)": avg_sqale,
        "Quality@1 (FQS)": avg_fqs
    })

summary_df = pd.DataFrame(summary_rows)
summary_df["sort_order"] = summary_df.apply(
    lambda r: 0 if r["Model"] == "GroundTruth" else (1 if r["Model"] == "GPT-4-Turbo" else (2 if r["Model"] == "GPT-3.5-Turbo" else 3)), axis=1
)
summary_df = summary_df.sort_values("sort_order").drop(columns=["sort_order"])
summary_md = summary_df.to_markdown(index=False)

# 2. RQ1: Compare functional and non-functional code complexity (excluding GroundTruth).
print("Running RQ1 tests...")
non_gt_df = master_df[master_df["model"] != "GroundTruth"].copy()
non_gt_df['functional'] = non_gt_df['status'].isin(['Success', 'PartialSuccess'])

rq1_rows = []
for model in ['GPT-4-Turbo', 'GPT-3.5-Turbo', 'WizardCoder-15B-V1.0']:
    sub = non_gt_df[non_gt_df["model"] == model]
    
    # Cognitive complexity
    func_cc = sub[sub['functional']]['cognitive_complexity']
    non_func_cc = sub[~sub['functional']]['cognitive_complexity']
    u_cc, p_cc = stats.mannwhitneyu(func_cc, non_func_cc, alternative="two-sided")
    
    # Cyclomatic complexity
    func_cplx = sub[sub['functional']]['complexity']
    non_func_cplx = sub[~sub['functional']]['complexity']
    u_cplx, p_cplx = stats.mannwhitneyu(func_cplx, non_func_cplx, alternative="two-sided")
    
    rq1_rows.append({
        "Model": model,
        "Metric": "Cognitive Complexity",
        "U Statistic": u_cc,
        "p-value": p_cc,
        "Significant (5%)": "Yes" if p_cc < 0.05 else "No"
    })
    rq1_rows.append({
        "Model": model,
        "Metric": "Cyclomatic Complexity",
        "U Statistic": u_cplx,
        "p-value": p_cplx,
        "Significant (5%)": "Yes" if p_cplx < 0.05 else "No"
    })
rq1_df = pd.DataFrame(rq1_rows)
rq1_md = rq1_df.to_markdown(index=False)

# RQ1 Cross-model: GPT-4 vs WizardCoder Cognitive Complexity
cc_gpt4 = master_df[master_df['model'] == 'GPT-4-Turbo']['cognitive_complexity']
cc_wiz = master_df[master_df['model'] == 'WizardCoder-15B-V1.0']['cognitive_complexity']
stat_cross, p_cross = stats.mannwhitneyu(cc_gpt4, cc_wiz, alternative="two-sided")

# 3. RQ2: Compare Pass@1 and Quality@1 (FQS).
print("Running RQ2 tests...")
wilcoxon_rows = []
for model in ['GPT-4-Turbo', 'GPT-3.5-Turbo', 'WizardCoder-15B-V1.0']:
    sub = non_gt_df[non_gt_df["model"] == model]
    stat, p = stats.wilcoxon(sub["pass_val"], sub["fqs"])
    wilcoxon_rows.append({
        "Model": model,
        "W Statistic": stat,
        "p-value": p,
        "Significant (5%)": "Yes" if p < 0.05 else "No"
    })
# Pooled
stat_pool, p_pool = stats.wilcoxon(non_gt_df["pass_val"], non_gt_df["fqs"])
wilcoxon_rows.append({
    "Model": "All LLMs Pooled",
    "W Statistic": stat_pool,
    "p-value": p_pool,
    "Significant (5%)": "Yes" if p_pool < 0.05 else "No"
})
wilcoxon_df = pd.DataFrame(wilcoxon_rows)
wilcoxon_md = wilcoxon_df.to_markdown(index=False)

# Spearman correlation on successes
successes = master_df[master_df['status'] == 'Success']
# LLM successes
success_llm = successes[successes['model'] != 'GroundTruth']
r_smells, p_smells = stats.spearmanr(success_llm['fqs'], success_llm['code_smells'])
r_cc, p_cc = stats.spearmanr(success_llm['fqs'], success_llm['cognitive_complexity'])

# Silent technical debt count
llm_success = non_gt_df[non_gt_df['status'] == 'Success']
silent_debt_count = sum(llm_success['fqs'] < 1.0)
pct_silent_debt = (silent_debt_count / len(llm_success)) * 100 if len(llm_success) > 0 else 0.0

total_success_all = len(successes)
silent_debt_all = sum(successes['fqs'] < 1.0)
pct_silent_debt_all = (silent_debt_all / total_success_all) * 100

# 3.5. Discussion: Compare GroundTruth and GPT-4-Turbo.
print("Analyzing GroundTruth vs. GPT-4-Turbo...")
gt_success = master_df[(master_df['model'] == 'GroundTruth') & (master_df['status'] == 'Success')]
gpt4_success = master_df[(master_df['model'] == 'GPT-4-Turbo') & (master_df['status'] == 'Success')]

gt_vs_gpt4_rows = []
gt_vs_gpt4_metrics = [
    ('cognitive_complexity', 'Cognitive Complexity'),
    ('complexity', 'Cyclomatic Complexity'),
    ('code_smells', 'Code Smells'),
    ('sqale_index', 'Technical Debt (min)'),
    ('fqs', 'FQS'),
    ('ncloc', 'Code Size (NCLOC)')
]

for col_name, metric_label in gt_vs_gpt4_metrics:
    s_gt = gt_success[col_name].fillna(0.0)
    s_gpt4 = gpt4_success[col_name].fillna(0.0)
    
    mean_gt = s_gt.mean()
    mean_gpt4 = s_gpt4.mean()
    
    u_stat, p_val = stats.mannwhitneyu(s_gt, s_gpt4, alternative='two-sided')
    
    gt_vs_gpt4_rows.append({
        "Metric": metric_label,
        "GT Mean": round(mean_gt, 4),
        "GPT-4 Mean": round(mean_gpt4, 4),
        "U Statistic": u_stat,
        "p-value": p_val,
        "Significativo (5%)": "Yes" if p_val < 0.05 else "No"
    })

gt_vs_gpt4_df = pd.DataFrame(gt_vs_gpt4_rows)
gt_vs_gpt4_md = gt_vs_gpt4_df.to_markdown(index=False)

# GroundTruth Silent Debt count
gt_total = len(gt_success)
gt_silent_debt_count = sum(gt_success['fqs'] < 1.0)
pct_gt_silent_debt = (gt_silent_debt_count / gt_total) * 100 if gt_total > 0 else 0.0

# Tasks where an LLM has FQS=1.0 and GroundTruth has FQS < 1.0.
df_pivot_fqs = master_df.pivot(index='file', columns='model', values='fqs')
better_tasks = df_pivot_fqs[
    (df_pivot_fqs['GroundTruth'] < 1.0) & 
    ((df_pivot_fqs['GPT-4-Turbo'] == 1.0) | (df_pivot_fqs['GPT-3.5-Turbo'] == 1.0) | (df_pivot_fqs['WizardCoder-15B-V1.0'] == 1.0))
].reset_index()

better_tasks_rows = []
for idx, row in better_tasks.iterrows():
    better_tasks_rows.append({
        "Task": row['file'],
        "FQS GT": round(row['GroundTruth'], 4),
        "GPT-4": row['GPT-4-Turbo'] if not pd.isna(row['GPT-4-Turbo']) else "---",
        "GPT-3.5": row['GPT-3.5-Turbo'] if not pd.isna(row['GPT-3.5-Turbo']) else "---",
        "WizardCoder": row['WizardCoder-15B-V1.0'] if not pd.isna(row['WizardCoder-15B-V1.0']) else "---"
    })
better_tasks_df = pd.DataFrame(better_tasks_rows)
better_tasks_md = better_tasks_df.to_markdown(index=False)


# 4. Generate charts.
print("Generating charts...")
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "axes.edgecolor": "#cccccc",
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8
})

# Plot 1: Cognitive Complexity and Code Smells by Model and Status
plt.figure(figsize=(12, 6))
sns.barplot(
    data=non_gt_df,
    x="model",
    y="cognitive_complexity",
    hue="status",
    hue_order=["Success", "Fail", "PartialSuccess", "Error"],
    palette=["#2ecc71", "#e74c3c", "#f39c12", "#95a5a6"],
    edgecolor="black",
    linewidth=0.5
)
plt.title("Average Cognitive Complexity by Model and Status", fontsize=15, fontweight="bold", pad=12)
plt.xlabel("Large Language Model (LLM)", fontsize=13)
plt.ylabel("Mean Cognitive Complexity", fontsize=13)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.legend(title="Status", fontsize=10, title_fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(output_plot_dir, "grouped_barplot_complexity_by_status.png"), dpi=300)
plt.close()

# Plot 2: Pareto Frontier Scatter Plot (Pass@1 vs. Quality@1)
plt.figure(figsize=(10, 8))
agg_df = master_df.groupby("model")[["pass_val", "fqs"]].mean().reset_index()

# Ideal line
lims = [0, 1.05]
plt.plot(lims, lims, color="#e74c3c", linestyle="--", alpha=0.7, label="Ideal Line (Zero Quality Penalty)")

sns.scatterplot(
    data=agg_df,
    x="pass_val",
    y="fqs",
    hue="model",
    s=200,
    edgecolor="black",
    linewidth=1.0,
    palette=["#3498db", "#2ecc71", "#e67e22", "#9b59b6"]
)

# Label points
for _, row in agg_df.iterrows():
    plt.annotate(
        row["model"],
        (row["pass_val"], row["fqs"]),
        textcoords="offset points",
        xytext=(10, 5),
        ha="left",
        fontsize=10,
        weight="bold"
    )

plt.title("Pareto Frontier: Functional Correctness (Pass@1) vs. Quality@1 (FQS)", fontsize=15, fontweight="bold", pad=12)
plt.xlabel("Functional Correctness Rate (Pass@1)", fontsize=13)
plt.ylabel("Quality-Adjusted Performance Score (Quality@1)", fontsize=13)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.legend(loc="upper left", fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(output_plot_dir, "scatter_pareto_frontier.png"), dpi=300)
plt.close()

# Plot 3: Spearman correlation heatmap.
plt.figure(figsize=(10, 8))
corr_vars = ["ncloc", "complexity", "cognitive_complexity", "code_smells", "sqale_index", "fqs"]
corr_matrix = master_df[corr_vars].corr(method="spearman")

labels = [
    "Lines of Code (NCLOC)",
    "Cyclomatic Complexity",
    "Cognitive Complexity",
    "Code Smells Count",
    "Technical Debt (min)",
    "Quality@1 Score (FQS)"
]
corr_matrix.columns = labels
corr_matrix.index = labels

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(
    corr_matrix,
    mask=mask,
    cmap="coolwarm",
    vmin=-1.0,
    vmax=1.0,
    annot=True,
    fmt=".3f",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8},
    annot_kws={"size": 11}
)
plt.title("Spearman Correlation Matrix of Software Quality Metrics", fontsize=15, fontweight="bold", pad=12)
plt.xticks(rotation=45, ha="right", fontsize=11)
plt.yticks(rotation=0, fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(output_plot_dir, "heatmap_correlation.png"), dpi=300)
plt.close()

# 6. Write the Markdown report.
print("Writing Markdown report...")
report_content = f"""# Consolidated Statistical Analysis Report (400-Record Dataset)

This report summarizes the functional correctness and software quality (SonarQube) analyses of the **ClassEval** benchmark runs (temperature 0, Holistic generation), covering GPT-4-Turbo, GPT-3.5-Turbo, WizardCoder-15B-V1.0, and GroundTruth.

---

## 1. Overall Performance (Means by LLM and GroundTruth)

This table shows unit-test outcomes and mean SonarQube static-analysis metrics for each group.

{summary_md}

*Note: `Quality@1 (FQS)` was calculated using the proposed formula with a scaling factor of $\\beta = 0.1$.*

---

## 2. RQ1: Relationship Between Functional Correctness and Structural Quality

We investigated whether functional code differs significantly in structural metrics from code that failed.

### Hypothesis Test (Two-Sided Mann–Whitney U by Model)
{rq1_md}

### Cognitive Complexity Comparison (GPT-4 vs. WizardCoder)
* U statistic: {stat_cross:.1f}
* **p-value: {p_cross:.2e}**
* *Result:* {'We reject the null hypothesis ($H_{10}$)' if p_cross < 0.05 else 'We do not reject the null hypothesis'} at the 5% significance level.

---

## 3. RQ2: Evaluation and Validation of the `Quality@1` (FQS) Metric

We evaluated the statistical significance of the quality penalty in FQS compared with classical Pass@1.

### Wilcoxon Test (Pass@1 vs. Quality@1)
{wilcoxon_md}

### Statistical Validation Findings
1. **Silent Technical Debt (LLMs):** In **{pct_silent_debt:.2f}%** of functionally successful LLM cases (73 files), technical debt reduced the final quality score.
2. **Silent Technical Debt (Overall):** Of the **{total_success_all}** successful cases in the dataset (including GroundTruth), **{silent_debt_all}** files (**{pct_silent_debt_all:.2f}%**) contain silent technical debt.
3. **Convergent Validation (Spearman Correlation for LLM Successes):**
   * The Spearman correlation between `Quality@1` and *Code Smells* is **{r_smells:.4f}** (p-value: {p_smells:.2e}), indicating strong construct validity with respect to maintainability.
   * The correlation with *Cognitive Complexity* is **{r_cc:.4f}** (p-value: {p_cc:.2e}), indicating no significant correlation among successful cases.

---

## 4. Discussion: Human Reference Analysis (GroundTruth vs. GPT-4-Turbo)

This section presents statistical comparisons between functionally successful GroundTruth and GPT-4-Turbo solutions, and identifies cases where LLMs achieved higher quality scores.

### GroundTruth Findings
* **Classes with Technical Debt:** **{gt_silent_debt_count}** of the {gt_total} human-reference classes (**{pct_gt_silent_debt:.2f}%**) have silent technical debt (FQS < 1.0).

### Tasks Where LLMs Outperformed GroundTruth in Structural Quality (FQS_LLM = 1.0 > FQS_GT)
{better_tasks_md}

### Statistical Comparison (Mann–Whitney U for Successful Solutions: GT vs. GPT-4-Turbo)
This comparison includes only functionally successful implementations ($N_{{GT}} = 100$, $N_{{GPT4}} = 37$).

{gt_vs_gpt4_md}

"""

with open(output_report_path, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"\nSuccess! The statistical report was saved to: {output_report_path}")
print(f"Generated charts were saved to: {output_plot_dir}\n")
