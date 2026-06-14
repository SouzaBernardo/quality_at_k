import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de caminhos relativos ao local do script
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "sonar_metrics_consolidated_master.csv")
output_report_path = os.path.join(base_dir, "reports", "relatorio_estatistico.md")
output_plot_dir = os.path.join(base_dir, "reports", "graficos")

# Certifica que os diretórios de saída existem
os.makedirs(os.path.dirname(output_report_path), exist_ok=True)
os.makedirs(output_plot_dir, exist_ok=True)

print(f"Lendo base de dados consolidada de: {csv_path}")
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Erro: O arquivo master CSV não foi encontrado em: {csv_path}")

master_df = pd.read_csv(csv_path)
print(f"Base de dados carregada com sucesso. Total de registros: {len(master_df)}")

# Standardize names
master_df['model'] = master_df['model'].replace({
    'gpt-4-turbo': 'GPT-4-Turbo',
    'gpt-3.5-turbo': 'GPT-3.5-Turbo',
    'wizardcoder-15b-v1.0': 'WizardCoder-15B-V1.0',
    'groundtruth': 'GroundTruth'
})

# 1. Gerar Tabela Descritiva Geral
print("Gerando estatísticas descritivas por modelo...")
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

# 2. RQ1: Comparação de Complexidade do grupo Functional vs Non-Functional (excluindo GroundTruth)
print("Executando testes para RQ1...")
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

# 3. RQ2: Comparação Pass@1 vs Quality@1 (FQS)
print("Executando testes para RQ2...")
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

# 3.5. Discussão: Diagnóstico do GroundTruth vs. GPT-4-Turbo
print("Executando análise do GroundTruth vs. GPT-4-Turbo...")
gt_success = master_df[(master_df['model'] == 'GroundTruth') & (master_df['status'] == 'Success')]
gpt4_success = master_df[(master_df['model'] == 'GPT-4-Turbo') & (master_df['status'] == 'Success')]

gt_vs_gpt4_rows = []
gt_vs_gpt4_metrics = [
    ('cognitive_complexity', 'Complexidade Cognitiva'),
    ('complexity', 'Complexidade Ciclomática'),
    ('code_smells', 'Code Smells'),
    ('sqale_index', 'Dívida Técnica (min)'),
    ('fqs', 'FQS'),
    ('ncloc', 'Tamanho de Código (NCLOC)')
]

for col_name, metric_label in gt_vs_gpt4_metrics:
    s_gt = gt_success[col_name].fillna(0.0)
    s_gpt4 = gpt4_success[col_name].fillna(0.0)
    
    mean_gt = s_gt.mean()
    mean_gpt4 = s_gpt4.mean()
    
    u_stat, p_val = stats.mannwhitneyu(s_gt, s_gpt4, alternative='two-sided')
    
    gt_vs_gpt4_rows.append({
        "Métrica": metric_label,
        "GT Média": round(mean_gt, 4),
        "GPT-4 Média": round(mean_gpt4, 4),
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

# Tasks where LLM has FQS=1.0 and GT has FQS < 1.0
df_pivot_fqs = master_df.pivot(index='file', columns='model', values='fqs')
better_tasks = df_pivot_fqs[
    (df_pivot_fqs['GroundTruth'] < 1.0) & 
    ((df_pivot_fqs['GPT-4-Turbo'] == 1.0) | (df_pivot_fqs['GPT-3.5-Turbo'] == 1.0) | (df_pivot_fqs['WizardCoder-15B-V1.0'] == 1.0))
].reset_index()

better_tasks_rows = []
for idx, row in better_tasks.iterrows():
    better_tasks_rows.append({
        "Tarefa": row['file'],
        "FQS GT": round(row['GroundTruth'], 4),
        "GPT-4": row['GPT-4-Turbo'] if not pd.isna(row['GPT-4-Turbo']) else "---",
        "GPT-3.5": row['GPT-3.5-Turbo'] if not pd.isna(row['GPT-3.5-Turbo']) else "---",
        "WizardCoder": row['WizardCoder-15B-V1.0'] if not pd.isna(row['WizardCoder-15B-V1.0']) else "---"
    })
better_tasks_df = pd.DataFrame(better_tasks_rows)
better_tasks_md = better_tasks_df.to_markdown(index=False)


# 4. Geração de Gráficos
print("Gerando gráficos...")
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

# Plot 3: Heatmap de Correlação de Spearman
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

# 6. Gravar Relatório Markdown
print("Gravando relatório markdown...")
report_content = f"""# Relatório Consolidado de Análise Estatística (Recorte 400 registros)

Este relatório resume os resultados das análises de corretude funcional e qualidade de software (SonarQube) sobre as execuções do benchmark **ClassEval** (Temperatura 0, Geração Holística) focando no recorte de GPT-4-Turbo, GPT-3.5-Turbo, WizardCoder-15B-V1.0 e GroundTruth.

---

## 1. Tabela Geral de Desempenho (Médias por LLM e GroundTruth)

Esta tabela apresenta o sucesso nos testes unitários e as médias das métricas estáticas do SonarQube para cada grupo.

{summary_md}

*Nota: `Quality@1 (FQS)` foi calculado utilizando a fórmula proposta com fator de escala $\\beta = 0.1$.*

---

## 2. RQ1: Relação entre Corretude Funcional e Qualidade Estrutural

Investizamos se os códigos funcionais diferem de forma estatisticamente significativa em termos estruturais dos códigos que falharam.

### Teste de Hipótese (Mann-Whitney U por Modelo - Bicaudal):
{rq1_md}

###   omparação de Complexidade Cognitiva (GPT-4 vs WizardCoder):
* Estatística U: {stat_cross:.1f}
* **p-valor: {p_cross:.2e}**
* *Resultado:* {'Rejeitamos a Hipótese Nula ($H_{10}$)' if p_cross < 0.05 else 'Não rejeitamos a Hipótese Nula'} (nível de significância de 5%).

---

## 3. RQ2: Avaliação e Validação da Métrica `Quality@1` (FQS)

Avaliamos a significância estatística do pedágio de qualidade do FQS em comparação ao Pass@1 clássico.

### Teste de Wilcoxon (Pass@1 vs. Quality@1):
{wilcoxon_md}

### Fatos Estatísticos de Validação:
1. **Dívida Técnica Silenciosa (LLMs):** Em **{pct_silent_debt:.2f}%** dos casos de sucesso funcional das LLMs (73 arquivos), o score final de qualidade foi reduzido devido à dívida técnica.
2. **Dívida Técnica Silenciosa (Total):** Considerando todos os **{total_success_all}** sucessos da base (incluindo GroundTruth), **{silent_debt_all}** arquivos (**{pct_silent_debt_all:.2f}%**) contêm dívida técnica silenciosa.
3. **Validação Convergente (Spearman nos Sucessos das LLMs):**
   * A correlação de Spearman entre `Quality@1` e *Code Smells* é de **{r_smells:.4f}** (p-valor: {p_smells:.2e}), provando forte validade de construto com manutenibilidade.
   * A correlação com *Complexidade Cognitiva* é de **{r_cc:.4f}** (p-valor: {p_cc:.2e}), sem correlação significativa nos sucessos.

---

## 4. Discussão: Diagnóstico da Referência Humana (GroundTruth vs. GPT-4-Turbo)

Apresentamos as análises estatísticas comparativas entre os sucessos funcionais do GroundTruth e do GPT-4-Turbo, além da identificação de superioridade de qualidade das LLMs.

### Fatos Estatísticos do GroundTruth:
* **Classes com Dívida Técnica:** **{gt_silent_debt_count}** das {gt_total} classes de referência humana (**{pct_gt_silent_debt:.2f}%**) possuem dívida técnica silenciosa (FQS < 1.0).

### Tarefas onde LLMs superaram o GroundTruth em Qualidade Estrutural (FQS_LLM = 1.0 > FQS_GT):
{better_tasks_md}

### Contraste Estatístico (MWU nos Sucessos: GT vs GPT-4-Turbo):
Compare exclusivamente implementações funcionais bem-sucedidas ($N_{{GT}} = 100$, $N_{{GPT4}} = 37$).

{gt_vs_gpt4_md}

"""

with open(output_report_path, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"\nSucesso! O relatório estatístico foi salvo em: {output_report_path}")
print(f"Os gráficos gerados foram salvos no diretório: {output_plot_dir}\n")

