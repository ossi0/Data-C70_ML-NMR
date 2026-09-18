import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

# Load the data
C70_an_train = np.loadtxt('./data/matten_training_data/C70_anion_train_loss.csv', delimiter=",", dtype=float, skiprows=1)
C70_an_val = np.loadtxt('./data/matten_training_data/C70_anion_val_loss.csv', delimiter=",", dtype=float, skiprows=1)
C70_an_val_mae = np.loadtxt('./data/matten_training_data/C70_anion_val_mae.csv', delimiter=",", dtype=float, skiprows=1)


C70_an_sigma_train = C70_an_train[:, 1]
C70_an_sigma_val = C70_an_val[:, 1]
C70_an_sigma_val_mae = C70_an_val_mae[:, 1]

#Plot
plt.rcParams.update({'font.size': 16})
fig, (ax1) = plt.subplots(1, 1, layout='none', figsize=(7, 6))
fig.subplots_adjust(left=0.15, right=0.94, wspace=0.25, top=0.921, bottom=0.117, hspace=0.2)

#Sigma train+val neutral model
ax1.loglog(C70_an_sigma_train, color='blue', label=r'$\sigma_{\text{Loss}}^{\text{train.}}$')
ax1.loglog(C70_an_sigma_val, color='green', label=r'$\sigma_{\text{Loss}}^{\text{val.}}$', linestyle='dashed')
ax1.loglog(C70_an_sigma_val_mae, color='firebrick', label=r'$\sigma_{\text{MAE}}^{\text{val.}}$')
ax1.set_ylabel('Error', fontsize=18)
ax1.set_yticks([0.1, 1, 10, 100])
ax1.set_xticks([1, 10, 100, 1000])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=18)
ax1.tick_params(axis='y', labelsize=18)
ax1.set_xlim([1, 1200])
ax1.set_xlabel('Epoch', fontsize=18)
ax1.set_ylim([0.03, 100])
ax1.legend(loc="upper right", fontsize=16)
ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:g}'))
ax1.grid(True, which="both", axis="both", ls="-", alpha=0.4)

# Save the figure
plt.savefig('matten_anion.png', dpi=300)
plt.show()
