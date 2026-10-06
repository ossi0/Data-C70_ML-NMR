import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

#DATA

data_dist_x = [1, 2, 4, 8, 16]
data_dist_y = [2.3127, 2.3286, 2.33, 2.3298, 2.3294]
data_dist_err = [0.0005, 0.0005, 0.0004, 0.0006, 0.0008]

data_sigma_x = [1, 2, 4, 8]
data_sigma_y = [51.074, 50.739, 50.640, 50.632]
data_sigma_err = [0.009, 0.0154, 0.0203, 0.0197]

#Plot
plt.rcParams.update({'font.size': 16})
fig, ax1 = plt.subplots(figsize=(7, 5))
fig.subplots_adjust(left=0.17, right=0.856, wspace=0.2, top=0.925, bottom=0.132, hspace=0.22)

ax1.errorbar(data_dist_x, data_dist_y, yerr=data_dist_err, capsize=2.0, color='black', label=r'd(He-He)', marker='o', markersize=8, linestyle='solid')
ax1.set_ylabel('d(He-He) (Å)')
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.set_xlabel(r'Number of beads ($\mathit{P}$)', fontsize=14)
ax1.set_ylim(2.31, 2.335)
ax1.set_xlim(0, 17)
ax1.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
ax1.legend(loc="upper left", fontsize=12)

ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

ax2.errorbar(data_sigma_x, data_sigma_y, yerr=data_sigma_err, capsize=2.0, color='orange', label=r'${^3}\text{He} \ \sigma_{\text{iso}}$ (ppm)', marker='o', markersize=8, linestyle='solid')
ax2.set_ylabel(r'${^3}\text{He} \ \sigma_{\text{iso}}$ (ppm)')
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(loc="upper right", fontsize=12)
ax2.set_ylim(50.5, 51.2)
ax2.set_xlim(0, 17)
ax2.set_yticks([50.6, 50.8, 51, 51.2])

# Save the figure
plt.savefig('figure_S7.png', dpi=300)
plt.show()
