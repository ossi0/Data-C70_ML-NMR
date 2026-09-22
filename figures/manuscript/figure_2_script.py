from ase.io import db
import math
import ase.db
from ase.db import connect
from ase.io import read as read
from ase import Atoms
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup plot parameters and format
plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

# Load the energy data MAYBE CHANGE THIS TO READ THE DATA FROM .db AS IN THE CASE OF FORCES
energies = []

C70_He_di = np.loadtxt('../../data/dft/dimer/C70_di_an_energy.txt')
C70_He_mono = np.loadtxt('../../data/dft/monomer/C70_mono_an_energy.txt')

# Convert energies from Hartree to eV
C70_He_di = [C70_He_di[i]*27.2114079527 for i in range(len(C70_He_di))]
C70_He_mono = [C70_He_mono[i]*27.2114079527 for i in range(len(C70_He_mono))]

# Print energy ranges
print("C70 He di range: " + str(min(C70_He_di)) + ", " + str(max(C70_He_di)))
print("C70 He mono range: " + str(min(C70_He_mono)) + ", " + str(max(C70_He_mono)))

# Create Pandas data frames
C70_He_di = pd.DataFrame({"Energy": np.concatenate((np.array(C70_He_di), np.array(C70_He_di), np.array(C70_He_di)), axis=None), "Structure": r'He_2@$\text{C}_{70}^{6-}$'})
C70_He_mono = pd.DataFrame({"Energy": np.concatenate((np.array(C70_He_mono), np.array(C70_He_mono), np.array(C70_He_mono)), axis=None), "Structure": r'He@$\text{C}_{70}^{6-}$'})

# Concat the data frames
e_all = pd.concat([C70_He_mono, C70_He_di])


# Force data

# Helium
atom_id = -1   # Use -1 for helium and 1 for carbon

C70_He_di_forces_x = []
C70_He_mono_forces_x = []

C70_He_di_forces_y = []
C70_He_mono_forces_y = []

C70_He_di_forces_z = []
C70_He_mono_forces_z = []

#READ DATABASE

database = ase.db.core.connect('../../data/dft/molecules_train.db')
for i in range(1, len(database)):
    row = database.get(id=i)
    if (row.get('natoms') == 71):
        C70_He_mono_forces_x.append(row.get('forces')[atom_id][0])
        C70_He_mono_forces_y.append(row.get('forces')[atom_id][1])
        C70_He_mono_forces_z.append(row.get('forces')[atom_id][2])
    if (row.get('natoms') == 72):
        C70_He_di_forces_x.append(row.get('forces')[atom_id][0])
        C70_He_di_forces_y.append(row.get('forces')[atom_id][1])
        C70_He_di_forces_z.append(row.get('forces')[atom_id][2])

# Create Pandas data frames
C70_He_di_forces = pd.DataFrame({"Force": np.concatenate((np.array(C70_He_di_forces_x), np.array(C70_He_di_forces_y), np.array(C70_He_di_forces_z)), axis=None), "Structure": r'He$_2$@$\text{C}_{70}^{6-}$'})
C70_He_mono_forces = pd.DataFrame({"Force": np.concatenate((np.array(C70_He_mono_forces_x), np.array(C70_He_mono_forces_y), np.array(C70_He_mono_forces_z)), axis=None), "Structure": r'He@$\text{C}_{70}^{6-}$'})

# Concat the data frames
f_He_all = pd.concat([C70_He_mono_forces, C70_He_di_forces])
#--------------------------------------------------------------#
# Carbon
C70_C_di_forces_x = []
C70_C_mono_forces_x = []

C70_C_di_forces_y = []
C70_C_mono_forces_y = []

C70_C_di_forces_z = []
C70_C_mono_forces_z = []


for i in range(1, len(database)):
    row = database.get(id=i)
    if (row.get('natoms') == 71):
        for j in range(0, 69):
            C70_C_mono_forces_x.append(row.get('forces')[j][0])
            C70_C_mono_forces_y.append(row.get('forces')[j][1])
            C70_C_mono_forces_z.append(row.get('forces')[j][2])
    if (row.get('natoms') == 72):
        for j in range(0, 69):
            C70_C_di_forces_x.append(row.get('forces')[j][0])
            C70_C_di_forces_y.append(row.get('forces')[j][1])
            C70_C_di_forces_z.append(row.get('forces')[j][2])

# Create Pandas data frames
C70_C_di_forces = pd.DataFrame({"Force": np.concatenate((np.array(C70_C_di_forces_x), np.array(C70_C_di_forces_y), np.array(C70_C_di_forces_z)), axis=None), "Structure": r'He$_2$@$\text{C}_{70}^{6-}$'})
C70_C_mono_forces = pd.DataFrame({"Force": np.concatenate((np.array(C70_C_mono_forces_x), np.array(C70_C_mono_forces_y), np.array(C70_C_mono_forces_z)), axis=None), "Structure": r'He@$\text{C}_{70}^{6-}$'})

# Concat the data frames
f_C_all = pd.concat([C70_C_mono_forces, C70_C_di_forces])


# Draw the subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout='none', figsize=(11, 8))

fig.subplots_adjust(left=0.092, right=0.97, wspace=0.37, top=0.973, bottom=0.094, hspace=0.274)

ax1.set_ylabel('Density', fontsize=20)
ax1.set_xlabel(r'$E_{\text{DFT}}$ (eV/structure)', fontsize=20)
ax1.set_xlim(-10890, -10890+15)
ax1.set_ylim(0, 0.11)
ax1.set_yticks([0, 0.05, 0.1])
ax1.tick_params(axis='x', labelsize=19)
ax1.tick_params(axis='y', labelsize=19)

ax2.set_ylabel('Density', fontsize=20)
ax2.set_xlabel(r'Helium $\vec f_{\text{DFT}}$ (eV/Å)', fontsize=20)
ax2.set_xlim(-1, 1)
ax2.set_xticks([-1, -0.5, 0, 0.5, 1])
ax2.tick_params(axis='x', labelsize=19)
ax2.tick_params(axis='y', labelsize=19)

# Plot the figures
ax3.set_ylabel('Density', fontsize=20)
ax3.set_xlabel(r'$E_{\text{DFT}}$ (eV/structure)', fontsize=20)
ax3.set_xlim(-10970, -10970+15)
ax3.set_ylim(0, 0.11)
ax3.set_yticks([0, 0.05, 0.1])
ax3.tick_params(axis='x', labelsize=19)
ax3.tick_params(axis='y', labelsize=19)

ax4.set_ylabel('Density', fontsize=20)
ax4.set_xlabel(r'Carbon $\vec f_{\text{DFT}}$ (eV/Å)', fontsize=20)
ax4.set_xlim(-7.5, 7.5)
ax4.set_yticks([0, 0.05, 0.1, 0.15])
ax4.set_xticks([-5, -2.5, 0, 2.5, 5])
ax4.tick_params(axis='x', labelsize=19)
ax4.tick_params(axis='y', labelsize=19)


sns.histplot(data=C70_He_mono, x="Energy", common_norm=True, stat='probability', ax=ax1, kde=True, color='green', binwidth=0.2, kde_kws={'clip': (-10887.9, -10877.2), 'bw_adjust': 0.6})
sns.kdeplot(data=f_He_all, x="Force", hue="Structure", common_norm=True, palette=['green', 'blue'], ax=ax2)
sns.histplot(data=C70_He_di, x="Energy", common_norm=True, stat='probability', ax=ax3, kde=True, color='blue', binwidth=0.2, kde_kws={'clip': (-10967.4, -10956.1), 'bw_adjust': 0.6})
sns.kdeplot(data=f_C_all, x="Force", hue="Structure", common_norm=True, palette=['green', 'blue'], ax=ax4)

ax1.legend([r'He@$\text{C}_{70}^{6-}$'], loc="upper right", fontsize=18)
plt.setp(ax2.get_legend().get_texts(), fontsize='18') # for legend text
plt.setp(ax2.get_legend().get_title(), fontsize='18') # for legend title
ax3.legend([r'$\text{He}_2$@$\text{C}_{70}^{6-}$'], loc="upper right", fontsize=18)
plt.setp(ax4.get_legend().get_texts(), fontsize='18') # for legend text
plt.setp(ax4.get_legend().get_title(), fontsize='18') # for legend title

# Save the figure
plt.savefig('figure_2.png', dpi=300)
plt.show()
