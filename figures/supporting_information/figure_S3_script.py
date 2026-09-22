import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

# Load the data
C70_an_train = np.loadtxt('../../data/nequip_training_data/C70_an_train.csv', delimiter=",", dtype=float, skiprows=1)
C70_an_val = np.loadtxt('../../data/nequip_training_data/C70_an_val.csv', delimiter=",", dtype=float, skiprows=1)


C70_an_energy_train = C70_an_train[:, 2]
C70_an_energy_val = C70_an_val[:, 2]

C70_an_force_train = C70_an_train[:, 1]
C70_an_force_val = C70_an_val[:, 1]

#Plot
plt.rcParams.update({'font.size': 16})
fig, (ax1, ax2) = plt.subplots(1, 2, layout='none', figsize=(10, 4))
fig.subplots_adjust(left=0.11, right=0.968, wspace=0.367, top=0.921, bottom=0.162, hspace=0.2)

#Energy train+val anion model
ax1.loglog(C70_an_energy_train, color='blue', label=r'training')
ax1.loglog(C70_an_energy_val, color='green', label=r'validation', linestyle='dashed')
ax1.set_ylabel(r'$E_{\text{RMSE}}^{\text{Loss}}$ (eV)', fontsize=18)
ax1.set_xlabel('Epoch', fontsize=18)
ax1.set_xticks([1, 10, 100, 1000])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.set_xlim([1, 1200])
ax1.set_ylim([0, 15])
ax1.legend(loc="upper right", fontsize=16)
ax1.grid(True, which="both", axis="both", ls="-", alpha=0.4)

#Force train+val anion model
ax2.loglog(C70_an_force_train, color='blue', label=r'training')
ax2.loglog(C70_an_force_val, color='green', label=r'validation', linestyle='dashed')
ax2.set_ylabel(r'$\vec{f}_{\text{RMSE}}^{\ \text{Loss}}$ (eV/Å)', fontsize=18)
ax2.set_xlabel('Epoch', fontsize=18)
ax2.set_yticks([0.07, 0.1, 0.2, 0.3, 0.5])
ax2.set_xticks([1, 10, 100, 1000])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)
ax2.set_xlim([1, 1200])
ax2.set_ylim([0.07, 0.35])
ax2.legend(loc="upper right", fontsize=16)
ax2.grid(True, which="both", axis="both", ls="-", alpha=0.4)

# Save the figure
plt.savefig('figure_S3.png', dpi=300)
plt.show()
