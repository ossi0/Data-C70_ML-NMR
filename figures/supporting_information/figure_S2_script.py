import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

#DATA

data_size_x = [1000, 2000, 3000, 4000]
data_size_y = [0.152556, 0.093124, 0.084381, 0.0851140]

numlay_x = [2, 3, 4]
numlay_y = [0.132661, 0.081895, 0.056711]

feat_x = [32, 64, 128]
feat_y = [0.1326518, 0.111976, 0.103031]

lmax_x = [1, 2, 3]
lmax_y = [0.267671, 0.132852, 0.081863]

#Plot
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, layout='none', figsize=(10, 7))
fig.subplots_adjust(left=0.142, right=0.987, wspace=0.306, top=0.974, bottom=0.1, hspace=0.277)

ax1.plot(data_size_x, data_size_y, color='seagreen', label=r'test. dataset', marker='o', markersize=10, linestyle='solid')
ax1.set_ylabel(r'$\vec{f}_{\text{MAE}}^{\ \text{Loss}}$ (eV/Å)', fontsize=18)
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.set_xlabel('Dataset size', fontsize=18)
ax1.legend(loc="upper right", fontsize=16)

ax2.plot(feat_x, feat_y, color='goldenrod', label=r'test. dataset', marker='*', markersize=10, linestyle='solid')
ax2.set_xticks([32, 64, 96, 128])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)
ax2.set_xlabel('Number of features', fontsize=18)
ax2.legend(loc="upper right", fontsize=16)

ax3.plot(lmax_x, lmax_y, color='royalblue', label=r'test. dataset', marker='P', markersize=10, linestyle='solid')
ax3.set_ylabel(r'$\vec{f}_{\text{MAE}}^{\ \text{Loss}}$ (eV/Å)', fontsize=18)
ax3.set_xticks([1, 2, 3])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.tick_params(axis='x', labelsize=18)
ax3.tick_params(axis='y', labelsize=18)
ax3.set_xlabel(r'Maximum rotation order ($l_{\text{max}}$)', fontsize=18)
ax3.legend(loc="upper right", fontsize=16)

ax4.plot(numlay_x, numlay_y, color='firebrick', label=r'test. dataset', marker='v', markersize=10, linestyle='solid')
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.tick_params(axis='x', labelsize=18)
ax4.tick_params(axis='y', labelsize=18)
ax4.set_xlabel('Number of interaction blocks', fontsize=18)
ax4.legend(loc="upper right", fontsize=16)

# Save the figure
plt.savefig('nequip_param_testing_forces_an.png', dpi=300)
plt.show()
