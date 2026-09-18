import numpy as np
from ase.io import read
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D

# Referense magnetic shielding of a free helium
SIGMA_HE = 59.874

# Load th data
C70_di_an = np.loadtxt('data/sigma_predicted_dimer/class_3he/sig_di_avg.txt')
C70_mono_an = np.loadtxt('data/sigma_predicted_monomer/class_3he/sig_mono_avg.txt')
C70_di_an_pimd = np.loadtxt('data/sigma_predicted_dimer/3he/sig_di_avg.txt')
C70_mono_an_pimd = np.loadtxt('data/sigma_predicted_monomer/3he/sig_mono_avg.txt')
C70_di_an_pileg_1b = np.loadtxt('data/sigma_predicted_dimer/class_pileg/sig_di_avg.txt')
C70_mono_an_pileg_1b = np.loadtxt('data/sigma_predicted_monomer/class_pileg/sig_mono_avg.txt')

# Calculate statistics
mono_mean_an = np.round(np.mean(C70_mono_an_pimd), 3)
dimer_mean_an = np.round(np.mean(C70_di_an_pimd), 3)
mono_sem_an = np.round(np.std(C70_mono_an_pimd)/(len(C70_mono_an_pimd))**(1/2), 3)
dimer_sem_an = np.round(np.std(C70_di_an_pimd)/(len(C70_di_an_pimd))**(1/2), 3)

mono_mean_an_pileg_1b = np.round(np.mean(C70_mono_an_pileg_1b), 3)
dimer_mean_an_pileg_1b = np.round(np.mean(C70_di_an_pileg_1b), 3)
mono_sem_an_pileg_1b = np.round(np.std(C70_mono_an_pileg_1b)/(len(C70_mono_an_pileg_1b))**(1/2), 3)
dimer_sem_an_pileg_1b = np.round(np.std(C70_di_an_pileg_1b)/(len(C70_di_an_pileg_1b))**(1/2), 3)

mono_mean_an_class = np.round(np.mean(C70_mono_an), 3)
dimer_mean_an_class = np.round(np.mean(C70_di_an), 3)
mono_sem_an_class = np.round(np.std(C70_mono_an)/(len(C70_mono_an))**(1/2), 3)
dimer_sem_an_class = np.round(np.std(C70_di_an)/(len(C70_di_an))**(1/2), 3)

# Convert magnetic shielding to chemical shift
C70_di_an_shift = [SIGMA_HE - a for a in C70_di_an]
C70_mono_an_shift = [SIGMA_HE - a for a in C70_mono_an]
C70_di_an_pimd_shift = [SIGMA_HE - a for a in C70_di_an_pimd]
C70_mono_an_pimd_shift = [SIGMA_HE - a for a in C70_mono_an_pimd]
C70_di_an_pileg_1b_shift = [SIGMA_HE - a for a in C70_di_an_pileg_1b]
C70_mono_an_pileg_1b_shift = [SIGMA_HE - a for a in C70_mono_an_pileg_1b]


# Plot area
fig, ax1 = plt.subplots(1, 1, layout='none', figsize=(12, 7))

fig.subplots_adjust(left=0.105, right=0.982, wspace=0.15, top=0.92, bottom=0.1, hspace=0.274)

# Frame the data
C70_di_fr_an = pd.DataFrame({"r": C70_di_an_pimd_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm'})
C70_mono_fr_an = pd.DataFrame({"r": C70_mono_an_pimd_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm'})
C70_di_fr_an_pileg_1b = pd.DataFrame({"r": C70_di_an_pileg_1b_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_1b:.3f} $\pm$ {dimer_sem_an_pileg_1b:.3f} ppm'})
C70_mono_fr_an_pileg_1b = pd.DataFrame({"r": C70_mono_an_pileg_1b_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_1b:.3f} $\pm$ {mono_sem_an_pileg_1b:.3f} ppm'})
C70_di_fr_an_class = pd.DataFrame({"r": C70_di_an_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, GLE) = {SIGMA_HE-dimer_mean_an_class:.3f} $\pm$ {dimer_sem_an_class:.3f} ppm'})
C70_mono_fr_an_class = pd.DataFrame({"r": C70_mono_an_shift, "System": f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=1, GLE) = {SIGMA_HE-mono_mean_an_class:.3f} $\pm$ {mono_sem_an_class:.3f} ppm'})

# Concat the frames
C70_all_an = pd.concat([C70_mono_fr_an, C70_di_fr_an, C70_mono_fr_an_class, C70_di_fr_an_class, C70_mono_fr_an_pileg_1b, C70_di_fr_an_pileg_1b])

# Plot the monomer kdeplots
sns.kdeplot(data=C70_all_an, x="r", hue="System", common_norm=False, palette=['red', 'green', 'blue'], clip=(-5, 30), bw_adjust=1.2, fill=False, linewidth=2, alpha=0.8, ax=ax1, hue_order=
            [f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=1, GLE) = {SIGMA_HE-mono_mean_an_class:.3f} $\pm$ {mono_sem_an_class:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{monomer}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an_pileg_1b:.3f} $\pm$ {mono_sem_an_pileg_1b:.3f} ppm'])

# Plot the dimer kdeplots
sns.kdeplot(data=C70_all_an, x="r", hue="System", common_norm=False, palette=['red', 'green', 'blue'], clip=(-5, 30), bw_adjust=1.2, linestyle="--", fill=False, linewidth=2, alpha=0.8, ax=ax1, hue_order=
            [f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, GLE) = {SIGMA_HE-dimer_mean_an_class:.3f} $\pm$ {dimer_sem_an_class:.3f} ppm',
             f'$\\langle\delta_{{\\text{{iso}}}}\\rangle[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an_pileg_1b:.3f} $\pm$ {dimer_sem_an_pileg_1b:.3f} ppm'])

# Add vertical lines of experimental and geometry-optimized chemical shifts
exp_mono = ax1.vlines(8.20, 0, 0.20, color='black', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}} [\\text{{monomer}}]$ (exp)')
exp_di = ax1.vlines(8.04, 0, 0.20, color='black',  linestyle='--', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}} [\\text{{dimer}}]$ (exp)')
eq_mono = ax1.vlines(10.36, 0, 0.20, color='orange', linestyle='solid', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{monomer}}]$ (equilibrium geom.)')
eq_di = ax1.vlines(10.83, 0, 0.20, color='orange', linestyle='--', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (equilibrium geom.)')

# Add vertical lines of average chemical shift from data
mono_an_pimd_line = ax1.vlines(SIGMA_HE - mono_mean_an, 0, 0.20, color='red', linewidth=1.2)
dimer_an_pimd_line = ax1.vlines(SIGMA_HE - dimer_mean_an, 0, 0.20, color='red', linewidth=1.2, linestyle='--')
mono_an_line = ax1.vlines(SIGMA_HE - mono_mean_an_class, 0, 0.20, color='green', linewidth=1.2)
dimer_an_line = ax1.vlines(SIGMA_HE - dimer_mean_an_class, 0, 0.20, color='green', linewidth=1.2, linestyle='--')
mono_an_line_pileg_1b = ax1.vlines(SIGMA_HE - mono_mean_an_pileg_1b, 0, 0.20, color='blue', linewidth=1.2)
dimer_an_line_pileg_1b = ax1.vlines(SIGMA_HE - dimer_mean_an_pileg_1b, 0, 0.20, color='blue', linewidth=1.2, linestyle='--')


# Plot labels and ticks
ax1.set_xlabel(f'$^{3}\\text{{He}}\ \delta_{{\\text{{iso}}}}$ (ppm)', fontsize=16)
ax1.set_ylabel("Probability density", fontsize=16)
ax1.set_ylim(0, 0.15)
ax1.set_xlim(-2.5, 25)
ax1.set_xticks([24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0])
ax1.set_yticks([0, 0.05, 0.1, 0.15])
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.xaxis.set_inverted(True)

# Remove the automatic legend
ax1.get_legend().remove()

# Manually create desired legends
handles = [
    Line2D([0], [0], color='red', lw=2, label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{monomer}}]$ (P=4, PIGLET)'),
    Line2D([0], [0], color='red', lw=2, ls='--', label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{dimer}}]$ (P=4, PIGLET)'),
    Line2D([0], [0], color='green', lw=2, label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{monomer}}]$ (P=1, GLE)'),
    Line2D([0], [0], color='green', lw=2, ls='--', label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{dimer}}]$ (P=1, GLE)'),
    Line2D([0], [0], color='blue', lw=2, label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{monomer}}]$ (P=1, PILE-G)'),
    Line2D([0], [0], color='blue', lw=2, ls='--', label=f'$\\langle\delta_{{\\text{{iso}}}}\\rangle\ [\\text{{dimer}}]$ (P=1, PILE-G)'),
    Line2D([0], [0], color='orange', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{monomer}}]$ (equilibrium geom.)'), 
    Line2D([0], [0], color='orange', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (equilibrium geom.)'), 
    Line2D([0], [0], color='black', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{monomer}}]$ (exp)'),
    Line2D([0], [0], color='black', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (exp)'),
]
ax1.legend(handles=handles)
plt.setp(ax1.get_legend().get_texts(), fontsize='12') # for legend text
plt.setp(ax1.get_legend().get_title(), fontsize='12') # for legend title

# Save the figure as png
plt.savefig('dist_anion.png', dpi=300)
plt.show()
