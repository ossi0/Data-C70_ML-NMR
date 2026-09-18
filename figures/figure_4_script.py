import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the monomer data
iso_fr_C70_mono_an = pd.DataFrame({"Sigma": np.loadtxt('./data/dft/sigma/C70_mono_an_sigma_iso_DFT2.txt', usecols=0)})
mean_C70_mono_an = float(iso_fr_C70_mono_an.mean())
sem_C70_mono_an = float(iso_fr_C70_mono_an.sem(axis=0))
std_C70_mono_an = float(iso_fr_C70_mono_an.std(axis=0))

# Load the dimer data
iso_fr_C70_di_an = pd.DataFrame({"Sigma": np.loadtxt('./data/dft/sigma/C70_di_an_sigma_iso_DFT2.txt', usecols=0)})
mean_C70_di_an = float(iso_fr_C70_di_an.mean())
sem_C70_di_an = float(iso_fr_C70_di_an.sem(axis=0))
std_C70_di_an = float(iso_fr_C70_di_an.std(axis=0))

# Print statistics
print(f'monomer mean sigma: {mean_C70_mono_an:.2f} pm {sem_C70_mono_an:.2f} ppm')
print(f'dimer mean sigma: {mean_C70_di_an:.2f} pm {sem_C70_di_an:.2f} ppm')
print(f'monomer-dimer shift: {(mean_C70_mono_an-mean_C70_di_an):.3f} pm {(np.sqrt(sem_C70_mono_an**2+sem_C70_di_an**2)):.3f} ppm')

print("C70_He_mono_an range: " + str(min(np.loadtxt('./data/dft/sigma/C70_mono_an_sigma_iso_DFT2.txt', usecols=0))) + ", " + str(max(np.loadtxt('./data/dft/sigma/C70_mono_an_sigma_iso_DFT2.txt', usecols=0))))
print("C70_He_di_an range: " + str(min(np.loadtxt('./data/dft/sigma/C70_di_an_sigma_iso_DFT2.txt', usecols=0))) + ", " + str(max(np.loadtxt('./data/dft/sigma/C70_di_an_sigma_iso_DFT2.txt', usecols=0))))

# Initialize the plot area
fig, (ax1, ax2) = plt.subplots(1, 2, layout='none', figsize=(10, 5))
fig.subplots_adjust(left=0.101, right=0.977, wspace=0.312, top=0.924, bottom=0.146, hspace=0.268)

bin_edges = np.linspace(25, 70, 41)  # 40 bins → 41 edges

# Plot monomer histogram
sns.histplot(data=iso_fr_C70_mono_an, x="Sigma", kde=True, common_norm=True, stat='probability', bins=bin_edges, kde_kws = {'clip': (25, 70), 'bw_adjust': 1}, color='green', ax=ax1)
ax1.set_xlim(25, 70)
ax1.set_ylabel('Density', fontsize=19)
ax1.set_xlabel(r'$\sigma^{\text{DFT}}_{\text{iso}}$ (ppm)', fontsize=19)
ax1.tick_params(axis='x', labelsize=19)
ax1.tick_params(axis='y', labelsize=19)
ax1.set_xticks([30, 40, 50, 60])
ax1.legend([r'He@$\text{C}_{70}^{6-}$'], loc="upper left", fontsize=16)

# Plot dimer histogram
sns.histplot(data=iso_fr_C70_di_an, x="Sigma", kde=True, common_norm=True, stat='probability', bins=bin_edges, kde_kws = {'clip': (25, 70), 'bw_adjust': 1}, color='blue', ax=ax2)
ax2.set_xlim(25, 70)
ax2.set_ylabel('Density', fontsize=19)
ax2.set_xlabel(r'$\sigma^{\text{DFT}}_{\text{iso}}$ (ppm)', fontsize=19)
ax2.tick_params(axis='x', labelsize=19)
ax2.tick_params(axis='y', labelsize=19)
ax2.set_xticks([30, 40, 50, 60])
ax2.legend([r'$\text{He}_2$@$\text{C}_{70}^{6-}$'], loc="upper left", fontsize=16)

# Save the figure
plt.savefig('C70_He_an_sigma_dft.png', dpi=300)
plt.show()
