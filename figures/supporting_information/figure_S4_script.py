import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

#DATA

data_size_x = [1000, 2000, 3000, 4000, 6000]
data_size_y = [2.09521, 1.4586, 1.4021, 1.3985, 0.9521]

numlay_x = [2, 3, 4, 5]
numlay_y = [1.6803, 0.9521, 0.7550, 0.7060]

rlay_x = [2, 3, 4]
rlay_y = [0.9521, 0.9587, 0.9654]

irrep_x = [8, 15, 30, 45]
irrep_y = [1.1033, 0.9521, 0.9495, 0.8928]

#Plot
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, layout='none', figsize=(10, 7))
fig.subplots_adjust(left=0.142, right=0.987, wspace=0.306, top=0.974, bottom=0.1, hspace=0.277)

ax1.plot(data_size_x, data_size_y, color='seagreen', label=r'test. dataset', marker='o', markersize=10, linestyle='solid')
ax1.set_ylabel(r'$\sigma_{\text{MAE}}^{\text{Loss}}$ (ppm)', fontsize=18)
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.set_xlabel('Dataset size', fontsize=18)
ax1.legend(loc="upper right", fontsize=16)

ax2.plot(rlay_x, rlay_y, color='goldenrod', label=r'test. dataset', marker='*', markersize=10, linestyle='solid')
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)
ax2.set_xlabel('Number of radial layers', fontsize=18)
ax2.legend(loc="upper left", fontsize=16)

ax3.plot(irrep_x, irrep_y, color='royalblue', label=r'test. dataset', marker='P', markersize=10, linestyle='solid')
ax3.set_ylabel(r'$\sigma_{\text{MAE}}^{\text{Loss}}$ (ppm)', fontsize=18)
ax3.set_xticks([10, 20, 30, 40])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.tick_params(axis='x', labelsize=18)
ax3.tick_params(axis='y', labelsize=18)
ax3.set_xlabel('Number of tensorial irreps', fontsize=18)
ax3.legend(loc="upper right", fontsize=16)

ax4.plot(numlay_x, numlay_y, color='firebrick', label=r'test. dataset', marker='v', markersize=10, linestyle='solid')
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.tick_params(axis='x', labelsize=18)
ax4.tick_params(axis='y', labelsize=18)
ax4.set_xlabel('Number of convolution layers', fontsize=18)
ax4.legend(loc="upper right", fontsize=16)

# Save the figure
plt.savefig('matten_param_testing_an.png', dpi=300)
plt.show()
