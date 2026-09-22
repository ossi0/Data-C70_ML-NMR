import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
import pandas as pd
import scipy
import sklearn

#Predicted TRAIN SET
train_off1 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=1)
train_off2 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=2)
train_off3 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=5)

train_diag1 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=0)
train_diag2 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=4)
train_diag3 = np.loadtxt('../../data/dft/sigma/he_shielding_pred_DFT2.txt', usecols=8)

#True Values
true_off1 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=1)
true_off2 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=2)
true_off3 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=5)

true_diag1 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=0)
true_diag2 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=4)
true_diag3 = np.loadtxt('../../data/dft/sigma/he_shielding_true_DFT2.txt', usecols=8)

#Create data frames
diag1_fr = pd.DataFrame({"Sigma_true": true_diag1, "Sigma_pred": train_diag1, "index":"sigma_11"})
diag2_fr = pd.DataFrame({"Sigma_true": true_diag2, "Sigma_pred": train_diag2, "index":"sigma_22"})
diag3_fr = pd.DataFrame({"Sigma_true": true_diag3, "Sigma_pred": train_diag3, "index":"sigma_33"})

off1_fr = pd.DataFrame({"Sigma_true": true_off1, "Sigma_pred": train_off1, "index":"sigma_12"})
off2_fr = pd.DataFrame({"Sigma_true": true_off2, "Sigma_pred": train_off2, "index":"sigma_13"})
off3_fr = pd.DataFrame({"Sigma_true": true_off3, "Sigma_pred": train_off3, "index":"sigma_23"})

# Initialize plot area
fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(2, 3, figure=fig, left=0.088, bottom=0.094, right=0.945, top=0.98, wspace=0.35, hspace=0.25)

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


plot0 = sns.regplot(data=diag1_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint0)
r2_0 = sklearn.metrics.r2_score(diag1_fr["Sigma_true"], diag1_fr["Sigma_pred"])
rmse_0 = sklearn.metrics.root_mean_squared_error(diag1_fr["Sigma_true"], diag1_fr["Sigma_pred"])
mae_0 = sklearn.metrics.mean_absolute_error(diag1_fr["Sigma_true"], diag1_fr["Sigma_pred"])
ax_joint0.text(0.05, 0.90, f'R$^2$ = {r2_0:.3f}', fontsize=16, transform=ax_joint0.transAxes)
ax_joint0.text(0.05, 0.81, f'RMSE = {rmse_0:.2f}', fontsize=16, transform=ax_joint0.transAxes)
ax_joint0.text(0.05, 0.72, f'MAE = {mae_0:.2f}', fontsize=16, transform=ax_joint0.transAxes)
sns.histplot(data=diag1_fr, x="Sigma_true", bins=30, ax=ax_marg_x0, color="teal")
sns.histplot(data=diag1_fr, y="Sigma_pred", bins=30, ax=ax_marg_y0, color="teal")

ax_marg_x0.axis("off")
ax_marg_y0.axis("off")
ax_joint0.set_xlabel(r'He $\sigma_{xx}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint0.set_ylabel(r'He $\sigma_{xx}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint0.tick_params(axis='x', labelsize=16)
ax_joint0.tick_params(axis='y', labelsize=16)
ax_joint0.set_xticks([0, 25, 50, 75])

# ---- Second joint plot ----
gs1 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[1],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint1 = fig.add_subplot(gs1[1, 0])
ax_marg_x1 = fig.add_subplot(gs1[0, 0], sharex=ax_joint1)
ax_marg_y1 = fig.add_subplot(gs1[1, 1], sharey=ax_joint1)

plot1 = sns.regplot(data=diag2_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint1)
r2_1 = sklearn.metrics.r2_score(diag2_fr["Sigma_true"], diag2_fr["Sigma_pred"])
rmse_1 = sklearn.metrics.root_mean_squared_error(diag2_fr["Sigma_true"], diag2_fr["Sigma_pred"])
mae_1 = sklearn.metrics.mean_absolute_error(diag2_fr["Sigma_true"], diag2_fr["Sigma_pred"])
ax_joint1.text(0.05, 0.90, f'R$^2$ = {r2_1:.3f}', fontsize=16, transform=ax_joint1.transAxes)
ax_joint1.text(0.05, 0.81, f'RMSE = {rmse_1:.2f}', fontsize=16, transform=ax_joint1.transAxes)
ax_joint1.text(0.05, 0.72, f'MAE = {mae_1:.2f}', fontsize=16, transform=ax_joint1.transAxes)
sns.histplot(data=diag2_fr, x="Sigma_true", bins=30, ax=ax_marg_x1, color="teal")
sns.histplot(data=diag2_fr, y="Sigma_pred", bins=30, ax=ax_marg_y1, color="teal")

ax_marg_x1.axis("off")
ax_marg_y1.axis("off")
ax_joint1.set_xlabel(r'He $\sigma_{yy}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint1.set_ylabel(r'He $\sigma_{yy}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint1.tick_params(axis='x', labelsize=16)
ax_joint1.tick_params(axis='y', labelsize=16)
ax_joint1.set_xticks([0, 25, 50, 75])

# ---- Third joint plot ----
gs2 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[2],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint2 = fig.add_subplot(gs2[1, 0])
ax_marg_x2 = fig.add_subplot(gs2[0, 0], sharex=ax_joint2)
ax_marg_y2 = fig.add_subplot(gs2[1, 1], sharey=ax_joint2)

plot2 = sns.regplot(data=diag3_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint2)
r2_2 = sklearn.metrics.r2_score(diag3_fr["Sigma_true"], diag3_fr["Sigma_pred"])
rmse_2 = sklearn.metrics.root_mean_squared_error(diag3_fr["Sigma_true"], diag3_fr["Sigma_pred"])
mae_2 = sklearn.metrics.mean_absolute_error(diag3_fr["Sigma_true"], diag3_fr["Sigma_pred"])
ax_joint2.text(0.05, 0.90, f'R$^2$ = {r2_2:.3f}', fontsize=16, transform=ax_joint2.transAxes)
ax_joint2.text(0.05, 0.81, f'RMSE = {rmse_2:.2f}', fontsize=16, transform=ax_joint2.transAxes)
ax_joint2.text(0.05, 0.72, f'MAE = {mae_2:.2f}', fontsize=16, transform=ax_joint2.transAxes)
sns.histplot(data=diag3_fr, x="Sigma_true", bins=30, ax=ax_marg_x2, color="teal")
sns.histplot(data=diag3_fr, y="Sigma_pred", bins=30, ax=ax_marg_y2, color="teal")

ax_marg_x2.axis("off")
ax_marg_y2.axis("off")
ax_joint2.set_xlabel(r'He $\sigma_{zz}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint2.set_ylabel(r'He $\sigma_{zz}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint2.tick_params(axis='x', labelsize=16)
ax_joint2.tick_params(axis='y', labelsize=16)
ax_joint2.set_xticks([0, 25, 50, 75])

# ---- Fourth joint plot ----
gs3 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[3],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint3 = fig.add_subplot(gs3[1, 0])
ax_marg_x3 = fig.add_subplot(gs3[0, 0], sharex=ax_joint3)
ax_marg_y3 = fig.add_subplot(gs3[1, 1], sharey=ax_joint3)

plot3 = sns.regplot(data=off1_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint3)
r2_3 = sklearn.metrics.r2_score(off1_fr["Sigma_true"], off1_fr["Sigma_pred"])
rmse_3 = sklearn.metrics.root_mean_squared_error(off1_fr["Sigma_true"], off1_fr["Sigma_pred"])
mae_3 = sklearn.metrics.mean_absolute_error(off1_fr["Sigma_true"], off1_fr["Sigma_pred"])
ax_joint3.text(0.05, 0.90, f'R$^2$ = {r2_3:.3f}', fontsize=16, transform=ax_joint3.transAxes)
ax_joint3.text(0.05, 0.81, f'RMSE = {rmse_3:.2f}', fontsize=16, transform=ax_joint3.transAxes)
ax_joint3.text(0.05, 0.72, f'MAE = {mae_3:.2f}', fontsize=16, transform=ax_joint3.transAxes)
sns.histplot(data=off1_fr, x="Sigma_true", bins=30, ax=ax_marg_x3, color="teal")
sns.histplot(data=off1_fr, y="Sigma_pred", bins=30, ax=ax_marg_y3, color="teal")

ax_marg_x3.axis("off")
ax_marg_y3.axis("off")
ax_joint3.set_xlabel(r'He $\sigma_{xy}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint3.set_ylabel(r'He $\sigma_{xy}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint3.tick_params(axis='x', labelsize=16)
ax_joint3.tick_params(axis='y', labelsize=16)


# ---- Fifth joint plot ----
gs4 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[4],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint4 = fig.add_subplot(gs4[1, 0])
ax_marg_x4 = fig.add_subplot(gs4[0, 0], sharex=ax_joint4)
ax_marg_y4 = fig.add_subplot(gs4[1, 1], sharey=ax_joint4)

plot4 = sns.regplot(data=off2_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint4)
r2_4 = sklearn.metrics.r2_score(off2_fr["Sigma_true"], off2_fr["Sigma_pred"])
rmse_4 = sklearn.metrics.root_mean_squared_error(off2_fr["Sigma_true"], off2_fr["Sigma_pred"])
mae_4 = sklearn.metrics.mean_absolute_error(off2_fr["Sigma_true"], off2_fr["Sigma_pred"])
ax_joint4.text(0.05, 0.90, f'R$^2$ = {r2_4:.3f}', fontsize=16, transform=ax_joint4.transAxes)
ax_joint4.text(0.05, 0.81, f'RMSE = {rmse_4:.2f}', fontsize=16, transform=ax_joint4.transAxes)
ax_joint4.text(0.05, 0.72, f'MAE = {mae_4:.2f}', fontsize=16, transform=ax_joint4.transAxes)
sns.histplot(data=off2_fr, x="Sigma_true", bins=30, ax=ax_marg_x4, color="teal")
sns.histplot(data=off2_fr, y="Sigma_pred", bins=30, ax=ax_marg_y4, color="teal")

ax_marg_x4.axis("off")
ax_marg_y4.axis("off")
ax_joint4.set_xlabel(r'He $\sigma_{xz}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint4.set_ylabel(r'He $\sigma_{xz}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint4.tick_params(axis='x', labelsize=16)
ax_joint4.tick_params(axis='y', labelsize=16)

# ---- Sixth joint plot ----
gs5 = gridspec.GridSpecFromSubplotSpec(
    2, 2, subplot_spec=gs[5],
    width_ratios=[4, 1],
    height_ratios=[1, 4],
    wspace=0.05, hspace=0.08
)

ax_joint5 = fig.add_subplot(gs5[1, 0])
ax_marg_x5 = fig.add_subplot(gs5[0, 0], sharex=ax_joint5)
ax_marg_y5 = fig.add_subplot(gs5[1, 1], sharey=ax_joint5)

plot5 = sns.regplot(data=off3_fr, x="Sigma_true", y="Sigma_pred", ci=99, marker="x", color="teal", line_kws=dict(color="black", lw=1), ax=ax_joint5)
r2_5 = sklearn.metrics.r2_score(off3_fr["Sigma_true"], off3_fr["Sigma_pred"])
rmse_5 = sklearn.metrics.root_mean_squared_error(off3_fr["Sigma_true"], off3_fr["Sigma_pred"])
mae_5 = sklearn.metrics.mean_absolute_error(off3_fr["Sigma_true"], off3_fr["Sigma_pred"])
ax_joint5.text(0.05, 0.90, f'R$^2$ = {r2_5:.3f}', fontsize=16, transform=ax_joint5.transAxes)
ax_joint5.text(0.05, 0.81, f'RMSE = {rmse_5:.2f}', fontsize=16, transform=ax_joint5.transAxes)
ax_joint5.text(0.05, 0.72, f'MAE = {mae_5:.2f}', fontsize=16, transform=ax_joint5.transAxes)
sns.histplot(data=off3_fr, x="Sigma_true", bins=30, ax=ax_marg_x5, color="teal")
sns.histplot(data=off3_fr, y="Sigma_pred", bins=30, ax=ax_marg_y5, color="teal")

ax_marg_x5.axis("off")
ax_marg_y5.axis("off")
ax_joint5.set_xlabel(r'He $\sigma_{yz}^{\text{DFT}}$ (ppm)', fontsize=16)
ax_joint5.set_ylabel(r'He $\sigma_{yz}^{\text{ML}}$ (ppm)', fontsize=16)
ax_joint5.tick_params(axis='x', labelsize=16)
ax_joint5.tick_params(axis='y', labelsize=16)

# Save the figure
plt.savefig('figure_S6.png', dpi=300)
plt.show()


