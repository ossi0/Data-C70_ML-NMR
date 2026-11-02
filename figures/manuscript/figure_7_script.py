import numpy as np
from ase.io import read
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Referense magnetic shielding of a free helium
SIGMA_HE = 59.8627

# Load th data
C70_di_an_pimd = np.loadtxt('../../data/sigma_predicted_dimer/4b_piglet/sig_all.txt')
C70_mono_an_pimd = np.loadtxt('../../data/sigma_predicted_monomer/4b_piglet/sig_all.txt')
C70_di_an_nhc_1b = np.loadtxt('../../data/sigma_predicted_dimer/1b_nhc/sig_di_avg.txt')
C70_mono_an_nhc_1b = np.loadtxt('../../data/sigma_predicted_monomer/1b_nhc/sig_mono_avg.txt')

# Calculate statistics
mono_mean_an = np.round(np.mean(C70_mono_an_pimd), 3)
dimer_mean_an = np.round(np.mean(C70_di_an_pimd), 3)
mono_sem_an = np.round(np.std(C70_mono_an_pimd)/(len(C70_mono_an_pimd))**(1/2), 3)
dimer_sem_an = np.round(np.std(C70_di_an_pimd)/(len(C70_di_an_pimd))**(1/2), 3)

mono_mean_an_nhc_1b = np.round(np.mean(C70_mono_an_nhc_1b), 3)
dimer_mean_an_nhc_1b = np.round(np.mean(C70_di_an_nhc_1b), 3)
mono_sem_an_nhc_1b = np.round(np.std(C70_mono_an_nhc_1b)/(len(C70_mono_an_nhc_1b))**(1/2), 3)
dimer_sem_an_nhc_1b = np.round(np.std(C70_di_an_nhc_1b)/(len(C70_di_an_nhc_1b))**(1/2), 3)

print("NHC mono std: " + str(np.std(C70_mono_an_nhc_1b)))
print("NHC di std: " + str(np.std(C70_di_an_nhc_1b)))
print("PIGLET mono std: " + str(np.std(C70_mono_an_pimd)))
print("PIGLET di std: " + str(np.std(C70_di_an_pimd)))


# Convert magnetic shielding to chemical shift
C70_di_an_pimd_shift = [SIGMA_HE - a for a in C70_di_an_pimd]
C70_mono_an_pimd_shift = [SIGMA_HE - a for a in C70_mono_an_pimd]
C70_di_an_nhc_1b_shift = [SIGMA_HE - a for a in C70_di_an_nhc_1b]
C70_mono_an_nhc_1b_shift = [SIGMA_HE - a for a in C70_mono_an_nhc_1b]


# Plot area
fig, ax1 = plt.subplots(1, 1, layout='none', figsize=(8, 7))

fig.subplots_adjust(left=0.125, right=0.983, wspace=0.15, top=0.92, bottom=0.1, hspace=0.274)

#fig, ax1 = plt.subplots(1, 1, layout='none', figsize=(13, 7))

#fig.subplots_adjust(left=0.075, right=0.99, wspace=0.15, top=0.92, bottom=0.1, hspace=0.274)

# Frame the data
C70_di_fr_an = pd.DataFrame({"r": C70_di_an_pimd_shift, "System": f'$\delta_{{\\text{{iso}}}}[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm'})
C70_mono_fr_an = pd.DataFrame({"r": C70_mono_an_pimd_shift, "System": f'$\delta_{{\\text{{iso}}}}[\\text{{mono}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm'})
C70_di_fr_an_nhc_1b = pd.DataFrame({"r": C70_di_an_nhc_1b_shift, "System": f'$\delta_{{\\text{{iso}}}}[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an_nhc_1b:.3f} $\pm$ {dimer_sem_an_nhc_1b:.3f} ppm'})
C70_mono_fr_an_nhc_1b = pd.DataFrame({"r": C70_mono_an_nhc_1b_shift, "System": f'$\delta_{{\\text{{iso}}}}[\\text{{mono}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an_nhc_1b:.3f} $\pm$ {mono_sem_an_nhc_1b:.3f} ppm'})
# Concat the frames
C70_all_an = pd.concat([C70_mono_fr_an, C70_di_fr_an, C70_mono_fr_an_nhc_1b, C70_di_fr_an_nhc_1b])

# Plot the monomer kdeplots
sns.kdeplot(data=C70_all_an, x="r", hue="System", common_norm=False, palette=['red', 'blue'], clip=(-5, 30), bw_adjust=1.2, fill=False, linewidth=2, alpha=0.8, ax=ax1, hue_order=
            [f'$\delta_{{\\text{{iso}}}}[\\text{{mono}}]$ (P=4, PIGLET) = {SIGMA_HE-mono_mean_an:.3f} $\pm$ {mono_sem_an:.3f} ppm',
             f'$\delta_{{\\text{{iso}}}}[\\text{{mono}}]$ (P=1, PILE-G) = {SIGMA_HE-mono_mean_an_nhc_1b:.3f} $\pm$ {mono_sem_an_nhc_1b:.3f} ppm'])

# Plot the dimer kdeplots
sns.kdeplot(data=C70_all_an, x="r", hue="System", common_norm=False, palette=['red', 'blue'], clip=(-5, 30), bw_adjust=1.2, linestyle="--", fill=False, linewidth=2, alpha=0.8, ax=ax1, hue_order=
            [f'$\delta_{{\\text{{iso}}}}[\\text{{dimer}}]$ (P=4, PIGLET) = {SIGMA_HE-dimer_mean_an:.3f} $\pm$ {dimer_sem_an:.3f} ppm',
             f'$\delta_{{\\text{{iso}}}}[\\text{{dimer}}]$ (P=1, PILE-G) = {SIGMA_HE-dimer_mean_an_nhc_1b:.3f} $\pm$ {dimer_sem_an_nhc_1b:.3f} ppm'])

# Add vertical lines of exp.erimental and geometry-optimized chemical shifts
exp_mono = ax1.vlines(8.20, 0, 0.20, color='black', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}} [\\text{{mono}}]$ (exp.)')
exp_di = ax1.vlines(8.04, 0, 0.20, color='black',  linestyle='--', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}} [\\text{{dimer}}]$ (exp.)')
eq_mono = ax1.vlines(SIGMA_HE-47.9842, 0, 0.20, color='orange', linestyle='solid', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (eq. geom.)')
eq_di = ax1.vlines(SIGMA_HE-48.1447, 0, 0.20, color='orange', linestyle='--', linewidth=1.5, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (eq. geom.)')

# Add vertical lines of average chemical shift from data
mono_an_pimd_line = ax1.vlines(SIGMA_HE - mono_mean_an, 0, 0.20, color='red', linewidth=1.2)
dimer_an_pimd_line = ax1.vlines(SIGMA_HE - dimer_mean_an, 0, 0.20, color='red', linewidth=1.2, linestyle='--')
mono_an_line_nhc_1b = ax1.vlines(SIGMA_HE - mono_mean_an_nhc_1b, 0, 0.20, color='blue', linewidth=1.2)
dimer_an_line_nhc_1b = ax1.vlines(SIGMA_HE - dimer_mean_an_nhc_1b, 0, 0.20, color='blue', linewidth=1.2, linestyle='--')


# Plot labels and ticks
ax1.set_xlabel(f'$^{3}\\text{{He}}\ \delta_{{\\text{{iso}}}}$ (ppm)', fontsize=16)
ax1.set_ylabel("Probability density", fontsize=16)
ax1.set_ylim(0, 0.15)
ax1.set_xlim(-3, 24)
ax1.set_yticks([0, 0.05, 0.1, 0.15])
ax1.tick_params(axis='x', labelsize=18)
ax1.xaxis.set_major_locator(MultipleLocator(2))
ax1.xaxis.set_major_formatter('{x:.0f}')
ax1.xaxis.set_minor_locator(MultipleLocator(1))
ax1.tick_params(axis='y', labelsize=18)
ax1.xaxis.set_inverted(True)

# Remove the automatic legend
ax1.get_legend().remove()

# Manually create desired legends
handles = [
    Line2D([0], [0], color='red', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=4)'),
    Line2D([0], [0], color='red', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=4)'),
    Line2D([0], [0], color='blue', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (P=1)'),
    Line2D([0], [0], color='blue', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (P=1)'),
    Line2D([0], [0], color='orange', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (eq. geom.)'), 
    Line2D([0], [0], color='orange', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (eq. geom.)'), 
    Line2D([0], [0], color='black', lw=2, label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{mono}}]$ (exp.)'),
    Line2D([0], [0], color='black', lw=2, ls='--', label=f'$\delta_{{\\text{{iso}}}}\ [\\text{{dimer}}]$ (exp.)'),
]
ax1.legend(handles=handles)
plt.setp(ax1.get_legend().get_texts(), fontsize='12') # for legend text
plt.setp(ax1.get_legend().get_title(), fontsize='12') # for legend title

# Save the figure as png
plt.savefig('figure_7.png', dpi=300)
plt.show()
