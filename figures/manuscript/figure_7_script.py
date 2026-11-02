import numpy as np
from ase.io import read
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

# Referense magnetic shielding of a free helium
SIGMA_HE = 59.8627


# Load the data

#Dimer data
C70_di_an_pileg_1b = np.loadtxt('../../data/sigma_predicted_dimer/1b_pileg/sig_di_avg.txt')
C70_di_an_gle_1b = np.loadtxt('../../data/sigma_predicted_dimer/1b_gle/sig_di_avg.txt')

C70_di_an_pileg_4b = np.loadtxt('../../data/sigma_predicted_dimer/4b_pileg/sig_all.txt')

C70_di_an_piglet_4b = np.loadtxt('../../data/sigma_predicted_dimer/4b_piglet/sig_all.txt')

C70_di_an_pileg_16b = np.loadtxt('../../data/sigma_predicted_dimer/16b_pileg/sig_all.txt')

#Monomer data
C70_mono_an_pileg_1b = np.loadtxt('../../data/sigma_predicted_monomer/1b_pileg/sig_mono_avg.txt')
C70_mono_an_gle_1b = np.loadtxt('../../data/sigma_predicted_monomer/1b_gle/sig_mono_avg.txt')

C70_mono_an_pileg_4b = np.loadtxt('../../data/sigma_predicted_monomer/4b_pileg/sig_all.txt')

C70_mono_an_piglet_4b = np.loadtxt('../../data/sigma_predicted_monomer/4b_piglet/sig_all.txt')

C70_mono_an_pileg_16b = np.loadtxt('../../data/sigma_predicted_monomer/16b_pileg/sig_all.txt')

# Calculate statistics
dimer_mean_an = np.round(np.mean(C70_di_an_pileg_1b), 3)
dimer_sem_an = np.round(np.std(C70_di_an_pileg_1b)/(len(C70_di_an_pileg_1b))**(1/2), 3)

dimer_mean_an_gle = np.round(np.mean(C70_di_an_gle_1b), 3)
dimer_sem_an_gle = np.round(np.std(C70_di_an_gle_1b)/(len(C70_di_an_gle_1b))**(1/2), 3)

dimer_mean_an_pileg_4b = np.round(np.mean(C70_di_an_pileg_4b), 3)
dimer_sem_an_pileg_4b = np.round(np.std(C70_di_an_pileg_4b)/(len(C70_di_an_pileg_4b))**(1/2), 3)

dimer_mean_an_piglet_4b = np.round(np.mean(C70_di_an_piglet_4b), 3)
dimer_sem_an_piglet_4b = np.round(np.std(C70_di_an_piglet_4b)/(len(C70_di_an_piglet_4b))**(1/2), 3)

dimer_mean_an_pileg_16b = np.round(np.mean(C70_di_an_pileg_16b), 3)
dimer_sem_an_pileg_16b = np.round(np.std(C70_di_an_pileg_16b)/(len(C70_di_an_pileg_16b))**(1/2), 3)

####################
mono_mean_an = np.round(np.mean(C70_mono_an_pileg_1b), 3)
mono_sem_an = np.round(np.std(C70_mono_an_pileg_1b)/(len(C70_mono_an_pileg_1b))**(1/2), 3)

mono_mean_an_gle = np.round(np.mean(C70_mono_an_gle_1b), 3)
mono_sem_an_gle = np.round(np.std(C70_mono_an_gle_1b)/(len(C70_mono_an_gle_1b))**(1/2), 3)

mono_mean_an_pileg_4b = np.round(np.mean(C70_mono_an_pileg_4b), 3)
mono_sem_an_pileg_4b = np.round(np.std(C70_mono_an_pileg_4b)/(len(C70_mono_an_pileg_4b))**(1/2), 3)

mono_mean_an_piglet_4b = np.round(np.mean(C70_mono_an_piglet_4b), 3)
mono_sem_an_piglet_4b = np.round(np.std(C70_mono_an_piglet_4b)/(len(C70_mono_an_piglet_4b))**(1/2), 3)

mono_mean_an_pileg_16b = np.round(np.mean(C70_mono_an_pileg_16b), 3)
mono_sem_an_pileg_16b = np.round(np.std(C70_mono_an_pileg_16b)/(len(C70_mono_an_pileg_16b))**(1/2), 3)


# Convert magnetic shielding to chemical shift
C70_di_an_shift_1b = [SIGMA_HE - a for a in C70_di_an_pileg_1b]
C70_di_an_shift_1b_gle = [SIGMA_HE - a for a in C70_di_an_gle_1b]
C70_di_an_shift_4b = [SIGMA_HE - a for a in C70_di_an_pileg_4b]
C70_di_an_shift_piglet_4b = [SIGMA_HE - a for a in C70_di_an_piglet_4b]
C70_di_an_shift_16b = [SIGMA_HE - a for a in C70_di_an_pileg_16b]

C70_mono_an_shift_1b = [SIGMA_HE - a for a in C70_mono_an_pileg_1b]
C70_mono_an_shift_1b_gle = [SIGMA_HE - a for a in C70_mono_an_gle_1b]
C70_mono_an_shift_4b = [SIGMA_HE - a for a in C70_mono_an_pileg_4b]
C70_mono_an_shift_piglet_4b = [SIGMA_HE - a for a in C70_mono_an_piglet_4b]
C70_mono_an_shift_16b = [SIGMA_HE - a for a in C70_mono_an_pileg_16b]


# Plot area
fig, ax1 = plt.subplots(1, 1, layout='none', figsize=(12, 7))

fig.subplots_adjust(left=0.105, right=0.982, wspace=0.15, top=0.92, bottom=0.1, hspace=0.274)

# Frame the data
C70_di_fr_1b = pd.DataFrame({"r": C70_di_an_shift_1b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm'})
C70_di_fr_1b_gle = pd.DataFrame({"r": C70_di_an_shift_1b_gle, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, GLE) = {SIGMA_HE-dimer_mean_an_gle:.3f} $\pm$ {dimer_sem_an_gle:.3f} ppm'})
C70_di_fr_4b = pd.DataFrame({"r": C70_di_an_shift_4b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_4b:.3f} $\pm$ {dimer_sem_an_pileg_4b:.3f} ppm'})
C70_di_fr_piglet4b = pd.DataFrame({"r": C70_di_an_shift_piglet_4b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an_piglet_4b:.3f} $\pm$ {dimer_sem_an_piglet_4b:.3f} ppm'})
C70_di_fr_16b = pd.DataFrame({"r": C70_di_an_shift_16b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=16, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_16b:.3f} $\pm$ {dimer_sem_an_pileg_16b:.3f} ppm'})

C70_mono_fr_1b = pd.DataFrame({"r": C70_mono_an_shift_1b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm'})
C70_mono_fr_1b_gle = pd.DataFrame({"r": C70_mono_an_shift_1b_gle, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=1, GLE) = {SIGMA_HE-mono_mean_an_gle:.3f} $\pm$ {mono_sem_an_gle:.3f} ppm'})
C70_mono_fr_4b = pd.DataFrame({"r": C70_mono_an_shift_4b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=4, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_4b:.3f} $\pm$ {mono_sem_an_pileg_4b:.3f} ppm'})
C70_mono_fr_piglet4b = pd.DataFrame({"r": C70_mono_an_shift_piglet_4b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an_piglet_4b:.3f} $\pm$ {mono_sem_an_piglet_4b:.3f} ppm'})
C70_mono_fr_16b = pd.DataFrame({"r": C70_mono_an_shift_16b, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=16, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_16b:.3f} $\pm$ {mono_sem_an_pileg_16b:.3f} ppm'})

# Concat the dimer frames
C70_all_an = pd.concat([C70_di_fr_1b_gle, C70_di_fr_1b, C70_di_fr_4b, C70_di_fr_piglet4b, C70_di_fr_16b])

# Concat the mono frames
C70_all_an_mono = pd.concat([C70_mono_fr_1b_gle, C70_mono_fr_1b, C70_mono_fr_4b, C70_mono_fr_piglet4b, C70_mono_fr_16b])

# Plot the dimer kdeplots
sns.kdeplot(data=C70_all_an, x="r", hue="System", common_norm=False, palette=['orange', 'blue', 'purple', 'red', 'green'], clip=(-5, 30), bw_adjust=1.2, linestyle="--", fill=False, linewidth=1.5, alpha=0.8, ax=ax1, hue_order=
            [f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, GLE) = {SIGMA_HE-dimer_mean_an_gle:.3f} $\pm$ {dimer_sem_an_gle:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_4b:.3f} $\pm$ {dimer_sem_an_pileg_4b:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an_piglet_4b:.3f} $\pm$ {dimer_sem_an_piglet_4b:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=16, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_16b:.3f} $\pm$ {dimer_sem_an_pileg_16b:.3f} ppm'])

# Plot the monomer kdeplots
sns.kdeplot(data=C70_all_an_mono, x="r", hue="System", common_norm=False, palette=['orange', 'blue', 'purple', 'red', 'green'], clip=(-5, 30), bw_adjust=1.2, fill=False, linewidth=1.5, alpha=0.8, ax=ax1, hue_order=
            [f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=1, GLE) = {SIGMA_HE-mono_mean_an_gle:.3f} $\pm$ {mono_sem_an_gle:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=4, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_4b:.3f} $\pm$ {mono_sem_an_pileg_4b:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an_piglet_4b:.3f} $\pm$ {mono_sem_an_piglet_4b:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{mono}}]$ (P=16, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_16b:.3f} $\pm$ {mono_sem_an_pileg_16b:.3f} ppm'])

# Plot labels and ticks
ax1.set_xlabel(f'$^{3}\\text{{He}}\ \delta_{{\\text{{iso}}}}$ (ppm)', fontsize=16)
ax1.set_ylabel("Probability density", fontsize=16)
ax1.set_ylim(0, 0.15)
ax1.set_xlim(-2.5, 25)
ax1.set_xticks([24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2])
ax1.set_yticks([0, 0.05, 0.1, 0.15])
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.xaxis.set_inverted(True)

# Remove the automatic legend
ax1.get_legend().remove()

# Manually create desired legends
handles = [
    Line2D([0], [0], color='orange', lw=2, ls='solid', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=1, GLE)'),
    Line2D([0], [0], color='orange', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=1, GLE)'),
    Line2D([0], [0], color='blue', lw=2, ls='solid', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=1, PILE-G)'),
    Line2D([0], [0], color='blue', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=1, PILE-G)'),
    Line2D([0], [0], color='purple', lw=2, ls='solid', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=4, PILE-G)'),
    Line2D([0], [0], color='purple', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=4, PILE-G)'),
    Line2D([0], [0], color='red', lw=2, ls='solid', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=4, PIGLET)'),
    Line2D([0], [0], color='red', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=4, PIGLET)'),
    Line2D([0], [0], color='green', lw=2, ls='solid', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=16, PILE-G)'),
    Line2D([0], [0], color='green', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=16, PILE-G)'),
]
ax1.legend(handles=handles)
plt.setp(ax1.get_legend().get_texts(), fontsize='12') # for legend text
plt.setp(ax1.get_legend().get_title(), fontsize='12') # for legend title

# Save the figure as png
plt.savefig('figure_7.png', dpi=300)
plt.show()
