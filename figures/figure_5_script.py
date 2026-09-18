import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.gridspec as gridspec
import sklearn


#Sigma iso values
train_sigma_iso = np.loadtxt('./data/dft/sigma/iso_pred_DFT2.txt', usecols=0)
true_sigma_iso = np.loadtxt('./data/dft/sigma/iso_true_DFT2.txt', usecols=0)

#Create data frame
iso_fr = pd.DataFrame({"Sigma_true": true_sigma_iso, "Sigma_pred": train_sigma_iso, "index":"sigma_iso"})

# Initialize the plot area
fig = plt.figure(figsize=(6, 6))
gs = gridspec.GridSpec(1, 1, figure=fig, left=0.18, bottom=0.12, right=0.954, top=0.988, wspace=0.2, hspace=0.2)

# ---- First joint plot ----
gs0 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[0],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint0 = fig.add_subplot(gs0[1, 0])
ax_marg_x0 = fig.add_subplot(gs0[0, 0], sharex=ax_joint0)
ax_marg_y0 = fig.add_subplot(gs0[1, 1], sharey=ax_joint0)

# Plot the correlations
plot0 = sns.regplot(data=iso_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint0)
ax_joint0.plot([30, 65], [30, 65], linestyle="--", color="gray")
r2_0 = sklearn.metrics.r2_score(iso_fr["Sigma_true"], iso_fr["Sigma_pred"])
rmse_0 = sklearn.metrics.root_mean_squared_error(iso_fr["Sigma_true"], iso_fr["Sigma_pred"])
mae_0 = sklearn.metrics.mean_absolute_error(iso_fr["Sigma_true"], iso_fr["Sigma_pred"])
ax_joint0.text(0.05, 0.90, f'R$^2$ = {r2_0:.3f}', fontsize=16, transform=ax_joint0.transAxes)
ax_joint0.text(0.05, 0.82, f'RMSE = {rmse_0:.2f}', fontsize=16, transform=ax_joint0.transAxes)
ax_joint0.text(0.05, 0.74, f'MAE = {mae_0:.2f}', fontsize=16, transform=ax_joint0.transAxes)
ax_joint0.tick_params(axis='x', labelsize=16)
ax_joint0.tick_params(axis='y', labelsize=16)
ax_joint0.set_xticks([35, 50, 65])
ax_joint0.set_yticks([35, 50, 65])
sns.histplot(data=iso_fr, x="Sigma_true", bins=30, ax=ax_marg_x0, color="teal")
sns.histplot(data=iso_fr, y="Sigma_pred", bins=30, ax=ax_marg_y0, color="teal")

ax_marg_x0.axis("off")
ax_marg_y0.axis("off")
ax_joint0.set_xlabel(r'$^{3}\text{He}\ \sigma_{\text{iso}}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint0.set_ylabel(r'$^{3}\text{He}\ \sigma_{\text{iso}}^{\text{ML}}$ (ppm)', fontsize=16)

# Save the figure
plt.savefig('C70_He_an_iso_corr.png', dpi=300)
plt.show()
