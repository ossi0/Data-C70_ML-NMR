import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

#DATA

#d(He-He)
data_hehe_x_piglet = [1, 2, 4, 8, 16]
data_hehe_y_piglet = [2.3148, 2.3289, 2.3293, 2.3297, 2.3294]
data_hehe_err_piglet = [0.0003, 0.0004, 0.0003, 0.0004, 0.0008]

data_hehe_x_pileg = [1, 4, 16]
data_hehe_y_pileg = [2.3148, 2.3262, 2.3264]
data_hehe_err_pileg = [0.0003, 0.0007, 0.0008]

#d(C-He)
data_che_x_piglet = [1, 2, 4, 8, 16]
data_che_y_piglet = [3.9629, 3.9731, 3.9732, 3.9731, 3.9732]
data_che_err_piglet = [0.0005, 0.0002, 0.0002, 0.0003, 0.0003]

data_che_x_pileg = [1, 4, 16]
data_che_y_pileg = [3.9629, 3.9696, 3.9732]
data_che_err_pileg = [0.0005, 0.0003, 0.0003]

#d(He-COM)
data_hecom_x_piglet = [1, 2, 4, 8, 16]
data_hecom_y_piglet = [1.2091, 1.2172, 1.2181, 1.2182, 1.2186]
data_hecom_err_piglet = [0.0002, 0.0003, 0.0002, 0.0003, 0.0005]

data_hecom_x_pileg = [1, 4, 16]
data_hecom_y_pileg = [1.2091, 1.2140, 1.2182]
data_hecom_err_pileg = [0.0002, 0.0004, 0.0007]

#3He sigma_iso
data_sigma_x_piglet = [1, 2, 4, 8, 16]
data_sigma_y_piglet = [51.074, 50.7383, 50.6398, 50.632, 50.636]
data_sigma_err_piglet = [0.009, 0.0154, 0.0203, 0.0197, 0.025]

data_sigma_x_pileg = [1, 4, 16]
data_sigma_y_pileg = [51.074, 50.892, 50.654]
data_sigma_err_pileg = [0.009, 0.009, 0.013]

#Plot
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 8))
fig.subplots_adjust(left=0.11, right=0.97, wspace=0.31, top=0.95, bottom=0.09, hspace=0.22)

ax1.errorbar(data_hehe_x_piglet, data_hehe_y_piglet, yerr=data_hehe_err_piglet, capsize=2.0, color='black', label=r'PIGLET', marker='d', markersize=6, linestyle='solid')
ax1.errorbar(data_hehe_x_pileg, data_hehe_y_pileg, yerr=data_hehe_err_pileg, capsize=2.0, color='orange', label=r'PILE-G', marker='o', markersize=6, linestyle='dashed')
ax1.set_ylabel(r'$\langle d\text{(He-He)} \rangle$ (Å)')
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.set_ylim(2.31, 2.335)
ax1.set_xlim(0, 17)
ax1.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
ax1.yaxis.set_major_locator(MultipleLocator(0.005))
ax1.yaxis.set_major_formatter('{x:.3f}')
ax1.yaxis.set_minor_locator(MultipleLocator(0.001))
ax1.legend(loc="lower right", fontsize=12)
ax1.grid(True)

ax2.errorbar(data_che_x_piglet, data_che_y_piglet, yerr=data_che_err_piglet, capsize=2.0, color='black', label=r'PIGLET', marker='d', markersize=6, linestyle='solid')
ax2.errorbar(data_che_x_pileg, data_che_y_pileg, yerr=data_che_err_pileg, capsize=2.0, color='orange', label=r'PILE-G', marker='o', markersize=6, linestyle='dashed')
ax2.set_ylabel(r'$\langle d\text{(C-He)} \rangle$ (Å)')
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)
#ax2.set_ylim(2.31, 2.335)
ax2.set_xlim(0, 17)
ax2.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
ax2.yaxis.set_major_locator(MultipleLocator(0.002))
ax2.yaxis.set_major_formatter('{x:.3f}')
ax2.yaxis.set_minor_locator(MultipleLocator(0.001))
ax2.legend(loc="lower right", fontsize=12)
ax2.grid(True)

ax3.errorbar(data_hecom_x_piglet, data_hecom_y_piglet, yerr=data_hecom_err_piglet, capsize=2.0, color='black', label=r'PIGLET', marker='d', markersize=6, linestyle='solid')
ax3.errorbar(data_hecom_x_pileg, data_hecom_y_pileg, yerr=data_hecom_err_pileg, capsize=2.0, color='orange', label=r'PILE-G', marker='o', markersize=6, linestyle='dashed')
ax3.set_ylabel(r'$\langle d\text{(He-COM)} \rangle$ (Å)')
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.tick_params(axis='x', labelsize=14)
ax3.tick_params(axis='y', labelsize=14)
ax3.set_xlabel(r'Number of beads ($\mathit{P}$)', fontsize=14)
#ax3.set_ylim(2.31, 2.335)
ax3.set_xlim(0, 17)
ax3.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
ax3.yaxis.set_major_locator(MultipleLocator(0.002))
ax3.yaxis.set_major_formatter('{x:.3f}')
ax3.yaxis.set_minor_locator(MultipleLocator(0.001))
ax3.legend(loc="lower right", fontsize=12)
ax3.grid(True)

ax4.errorbar(data_sigma_x_piglet, data_sigma_y_piglet, yerr=data_sigma_err_piglet, capsize=2.0, color='black', label=r'PIGLET', marker='d', markersize=6, linestyle='solid')
ax4.errorbar(data_sigma_x_pileg, data_sigma_y_pileg, yerr=data_sigma_err_pileg, capsize=2.0, color='orange', label=r'PILE-G', marker='o', markersize=6, linestyle='dashed')
ax4.set_ylabel(r'${^3}\text{He} \ \langle \sigma_{\text{iso}} \rangle$ (ppm)')
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.tick_params(axis='x', labelsize=14)
ax4.tick_params(axis='y', labelsize=14)
ax4.set_xlabel(r'Number of beads ($\mathit{P}$)', fontsize=14)
ax4.legend(loc="upper right", fontsize=12)
ax4.set_ylim(50.5, 51.2)
ax4.set_xlim(0, 17)
ax4.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
ax4.yaxis.set_major_locator(MultipleLocator(0.1))
ax4.yaxis.set_major_formatter('{x:.1f}')
ax4.yaxis.set_minor_locator(MultipleLocator(0.02))
ax4.grid(True)

# Save the figure
plt.savefig('figure_S7.png', dpi=300)
plt.show()
