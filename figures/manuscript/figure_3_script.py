
import numpy as np

import matplotlib.pyplot as plt

import ase.io
from sklearn.metrics import mean_squared_error
import sklearn
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

# Load the dft data and model predicted data
forces = []
true_forces = []
energies = []
true_energies = []
for i, frame in enumerate(ase.io.iread('../../data/dft/test_dataset0.xyz')):
    forces.append(frame.get_forces().flatten())
    true_forces.append(frame.arrays["original_dataset_forces"].flatten())
    energies.append(frame.get_potential_energy())
    true_energies.append(frame.info["original_dataset_energy"])
forces = np.concatenate(forces, axis=0)
true_forces = np.concatenate(true_forces, axis=0)
energies = np.asarray(energies)
true_energies = np.asarray(true_energies)

# Seperate the energies data of monomer and dimer
true_energies_mono = [x for x in true_energies if x > -10900]
true_energies_dimer = [x for x in true_energies if x < -10900]
energies_mono = [x for x in energies if x > -10900]
energies_dimer = [x for x in energies if x < -10900]

# Create Pandas DataFrames
energy_fr_mono = pd.DataFrame({r'$E_{\text{DFT}}$ (eV/structure)': true_energies_mono, r'$E_{\text{ML}}$ (eV/structure)': energies_mono, "index":"energy"})
energy_fr_di = pd.DataFrame({r'$E_{\text{DFT}}$ (eV/structure)': true_energies_dimer, r'$E_{\text{ML}}$ (eV/structure)': energies_dimer, "index":"energy"})
energy_fr_both = pd.DataFrame({r'$E_{\text{DFT}}$ (eV/structure)': true_energies, r'$E_{\text{ML}}$ (eV/structure)': energies, "index":"energy"})

force_fr = pd.DataFrame({'DFT': true_forces, 'ML': forces, "index":"force"})

# Initialize the plot area
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 8))
fig.subplots_adjust(left=0.149, right=0.943, wspace=0.62, top=0.957, bottom=0.094, hspace=0.375)

#Calculate statistics for the energies
r2_0 = sklearn.metrics.r2_score(energies, true_energies)
rmse_0 = sklearn.metrics.root_mean_squared_error(energies, true_energies)
mae_0 = sklearn.metrics.mean_absolute_error(energies, true_energies)

r2_0_mono = sklearn.metrics.r2_score(energies_mono, true_energies_mono)
rmse_0_mono = sklearn.metrics.root_mean_squared_error(energies_mono, true_energies_mono)
mae_0_mono = sklearn.metrics.mean_absolute_error(energies_mono, true_energies_mono)

r2_0_dimer = sklearn.metrics.r2_score(energies_dimer, true_energies_dimer)
rmse_0_dimer = sklearn.metrics.root_mean_squared_error(energies_dimer, true_energies_dimer)
mae_0_dimer = sklearn.metrics.mean_absolute_error(energies_dimer, true_energies_dimer)

# Plot axis1
ax = ax1
ax.set_xlabel(r'$E_{\text{DFT}}$ (eV/structure)', fontsize=20)
ax.set_ylabel(r'$E_{\text{ML}}$ (eV/structure)', fontsize=20)
ax.plot([-10980, -10860], [-10980, -10860], linestyle="--", color="gray")
plot1_both = sns.regplot(data=energy_fr_both, x=r'$E_{\text{DFT}}$ (eV/structure)', y=r'$E_{\text{ML}}$ (eV/structure)', ci=99, marker="o", color="white", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax1)
plot1_mono = sns.regplot(data=energy_fr_mono, x=r'$E_{\text{DFT}}$ (eV/structure)', y=r'$E_{\text{ML}}$ (eV/structure)', ci=99, marker="o", color="limegreen", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax1)
plot1_di = sns.regplot(data=energy_fr_di, x=r'$E_{\text{DFT}}$ (eV/structure)', y=r'$E_{\text{ML}}$ (eV/structure)', ci=99, marker="o", color="slateblue", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax1)
ax.set_xlim([-10980, -10860])
ax.set_ylim([-10980, -10860])
ax.set_title('All systems', fontsize=20)
ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)
ax.text(0.05, 0.90, f'R$^2$ = {r2_0:.4f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.81, f'RMSE = {rmse_0:.3f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.72, f'MAE = {mae_0:.3f}', fontsize=20, transform=ax.transAxes)
ax.set_xticks([-10980, -10920, -10860])
ax.set_yticks([-10980, -10920, -10860])

#Calculate statistics for the forces
r2_0 = sklearn.metrics.r2_score(forces, true_forces)
rmse_0 = sklearn.metrics.root_mean_squared_error(forces, true_forces)
mae_0 = sklearn.metrics.mean_absolute_error(forces, true_forces)

# Plot axis2
ax = ax2
ax.set_xlabel(r'$\vec f_{\text{DFT}}$ (eV/Å)', fontsize=20)
ax.set_ylabel(r'$\vec f_{\text{ML}}$ (eV/Å)', fontsize=20)
ax.plot([-15, 15], [-15, 15], linestyle="--", color="gray")
#x.scatter(true_forces, forces, marker = 'o', alpha=0.3, color='orange')
plot2_force = sns.regplot(data=force_fr, x='DFT', y='ML', ci=99, marker="o", color="orange", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax2).set(
    xlabel=r'$\vec f_{\text{DFT}}$ (eV/Å)', 
    ylabel=r'$\vec f_{\text{ML}}$ (eV/Å)'
)
ax.set_title('All systems', fontsize=20)
ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)
ax.text(0.05, 0.90, f'R$^2$ = {r2_0:.4f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.81, f'RMSE = {rmse_0:.3f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.72, f'MAE = {mae_0:.3f}', fontsize=20, transform=ax.transAxes)
ax.set_xticks([-10, 0, 10])
ax.set_yticks([-10, 0, 10])

# Plot axis3
ax = ax3
ax.set_xlabel(r'$E_{\text{DFT}}$ (eV/structure)', fontsize=20)
ax.set_ylabel(r'$E_{\text{ML}}$ (eV/structure)', fontsize=20)
ax.plot([-10890, -10874], [-10890, -10874], linestyle="--", color="gray")
plot3_mono = sns.regplot(data=energy_fr_mono, x=r'$E_{\text{DFT}}$ (eV/structure)', y=r'$E_{\text{ML}}$ (eV/structure)', ci=99, marker="o", color="limegreen", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax3)
ax.set_xlim([-10890, -10875])
ax.set_ylim([-10890, -10875])
ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)
ax.text(0.05, 0.90, f'R$^2$ = {r2_0_mono:.4f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.81, f'RMSE = {rmse_0_mono:.3f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.72, f'MAE = {mae_0_mono:.3f}', fontsize=20, transform=ax.transAxes)
ax.set_xticks([-10890, -10883, -10874])
ax.set_yticks([-10890, -10883, -10874])

# Custom legend handle showing scatter points only
scatter_handle = Line2D(
    [], [],
    color='limegreen',
    marker='o',
    linestyle='None',
    markersize=10,
    alpha=0.5,
    label=r'$\text{He}@\text{C}_{70}^{6-}$'
)
ax.legend(handles=[scatter_handle], loc="lower right", fontsize=20)

# Plot axis4
ax = ax4
ax.set_xlabel(r'$E_{\text{DFT}}$ (eV/structure)', fontsize=20)
ax.set_ylabel(r'$E_{\text{ML}}$ (eV/structure)', fontsize=20)
ax.plot([-10970, -10954], [-10970, -10954], linestyle="--", color="gray")
plot4_di = sns.regplot(data=energy_fr_di, x=r'$E_{\text{DFT}}$ (eV/structure)', y=r'$E_{\text{ML}}$ (eV/structure)', ci=99, marker="o", color="slateblue", line_kws=dict(color="black", lw=2), scatter_kws={'alpha':0.3}, ax=ax4)
ax.set_xlim([-10970, -10955])
ax.set_ylim([-10970, -10955])
ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)
ax.text(0.05, 0.90, f'R$^2$ = {r2_0_dimer:.4f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.81, f'RMSE = {rmse_0_dimer:.3f}', fontsize=20, transform=ax.transAxes)
ax.text(0.05, 0.72, f'MAE = {mae_0_dimer:.3f}', fontsize=20, transform=ax.transAxes)
ax.set_xticks([-10970, -10963, -10954])
ax.set_yticks([-10970, -10963, -10954])

# Custom legend handle showing scatter points only
scatter_handle = Line2D(
    [], [],
    color='slateblue',
    marker='o',
    linestyle='None',
    markersize=10,
    alpha=0.5,
    label=r'$\text{He}_{2}@\text{C}_{70}^{6-}$'
)
ax.legend(handles=[scatter_handle], loc="lower right", fontsize=20)

# Save the figure
plt.savefig('figure_3.png')
plt.show()
