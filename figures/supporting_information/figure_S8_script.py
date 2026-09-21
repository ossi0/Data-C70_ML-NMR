import numpy as np
from ase.io import read
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import gaussian_kde
from matplotlib.lines import Line2D


# Plot setup
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
    2, 2, layout="none", figsize=(12, 8)
)
fig.subplots_adjust(
    left=0.076,
    right=0.956,
    wspace=0.23,
    top=0.925,
    bottom=0.11,
    hspace=0.36,
)
sns.set_theme(style="whitegrid")


# Function to make the dataframes
def make_distribution_dataframe(data, labels):
    """Build the DataFrame used by seaborn for a set of distributions."""
    return pd.concat(
        [
            pd.DataFrame({"r": values, "Simulation": label})
            for values, label in zip(data, labels)
        ]
    )


# Function to plot the distributions
def plot_distribution(
    ax, data, labels, bins, kde_class, kde_pimd, legend_loc, legend_labels=None
):
    """Plot the distributions and the PIMD-minus-classical KDE difference."""
    legend_labels = labels if legend_labels is None else legend_labels
    sns.kdeplot(
        data=make_distribution_dataframe(data, labels),
        x="r",
        hue="Simulation",
        ax=ax,
        common_norm=False,
        palette=["blue", "green", "orange"],
    )

    ax.plot(
        bins,
        kde_pimd(bins) - kde_class(bins),
        label="PIMD − MD",
        color="black",
        ls="--",
    )
    ax.hlines(0, 0, 6, color="black", linestyle="solid", linewidth=1.5)
    ax.get_legend().remove()

    handles = [
        Line2D([0], [0], color="blue", lw=2, label=legend_labels[0]),
        Line2D([0], [0], color="green", lw=2, label=legend_labels[1]),
        Line2D([0], [0], color="orange", lw=2, label=legend_labels[2]),
        Line2D(
            [0],
            [0],
            color="black",
            lw=2,
            ls="--",
            label=r"PIMD - Classical (PILE-G)",
        ),
    ]
    ax.legend(handles=handles, loc=legend_loc)


# Function to plot the distribution without legend
def plot_distribution_nolegend(
    ax, data, labels, bins, kde_class, kde_pimd
):
    """Plot the distributions and the PIMD-minus-classical KDE difference."""
    sns.kdeplot(
        data=make_distribution_dataframe(data, labels),
        x="r",
        hue="Simulation",
        ax=ax,
        common_norm=False,
        palette=["blue", "green", "orange"],
    )

    ax.plot(
        bins,
        kde_pimd(bins) - kde_class(bins),
        label="PIMD − MD",
        color="black",
        ls="--",
    )
    ax.hlines(0, 0, 6, color="black", linestyle="solid", linewidth=1.5)
    ax.get_legend().remove()



# Common labels

SIMULATION_LABELS = [
    "MD (P=1, PILE-G)",
    "MD (P=1, GLE)",
    "PIMD (P=4, PIGLET)",
]

AXIS_1_DATA_LABELS = [
    "MD (P=1, PILE-G)",
    "MD (P=1, GLE)",
    "PIMD (P=4, PIGLET)",
]


# ---------------------------------------------------------------------------
# AXIS 1 — He-He RDF
# ---------------------------------------------------------------------------
he_he_class_pileg = np.loadtxt('./data/position_distributions/dimer/1b_pileg/he_he_distances.txt')
he_he_class_gle = np.loadtxt('./data/position_distributions/dimer/1b_gle/he_he_distances.txt')
he_he_pimd = np.loadtxt('./data/position_distributions/dimer/4b_piglet/he_he_distances.txt')

# Print some average He-He distances
print(
    "Classical (PILE-G) He-He average distance: "
    + str(np.round(np.mean(he_he_class_pileg), 4))
    + " ± "
    + str(np.round(np.std(he_he_class_pileg) / (len(he_he_class_pileg) ** (1 / 2)), 4))
)
print(
    "Classical (PI+GLE) He-He average distance: "
    + str(np.round(np.mean(he_he_class_gle), 4))
    + " ± "
    + str(
        np.round(
            np.std(he_he_class_gle) / (len(he_he_class_gle) ** (1 / 2)), 4
        )
    )
)
print(
    "PIMD (PIGLET, P=4) He-He average distance: "
    + str(np.round(np.mean(he_he_pimd), 4))
    + " ± "
    + str(np.round(np.std(he_he_pimd) / (len(he_he_pimd) ** (1 / 2)), 4))
)

bins_1 = np.linspace(1.5, 3.5, 500)
kde_class_1 = gaussian_kde(he_he_class_pileg)
kde_pimd_1 = gaussian_kde(he_he_pimd)

plot_distribution_nolegend(
    ax1,
    [he_he_class_pileg, he_he_class_gle, he_he_pimd],
    AXIS_1_DATA_LABELS,
    bins_1,
    kde_class_1,
    kde_pimd_1,
)


# ---------------------------------------------------------------------------
# AXIS 2 — C-He RDF
# ---------------------------------------------------------------------------
c_he_class_pileg = np.loadtxt('./data/position_distributions/dimer/1b_pileg/c_he_distances.txt')
c_he_class_gle = np.loadtxt('./data/position_distributions/dimer/1b_gle/c_he_distances.txt')
c_he_pimd = np.loadtxt('./data/position_distributions/dimer/4b_piglet/c_he_distances.txt')

bins_2 = np.linspace(2, 6, 1000)
kde_class_2 = gaussian_kde(c_he_class_pileg)
kde_pimd_2 = gaussian_kde(c_he_pimd)

plot_distribution(
    ax2,
    [c_he_class_pileg, c_he_class_gle, c_he_pimd],
    SIMULATION_LABELS,
    bins_2,
    kde_class_2,
    kde_pimd_2,
    "upper right",
)


# ---------------------------------------------------------------------------
# AXIS 3 — He distance from cage COM
# ---------------------------------------------------------------------------
he_com_class_pileg = np.loadtxt('./data/position_distributions/dimer/1b_pileg/he_COM_distances.txt')
he_com_class_gle = np.loadtxt('./data/position_distributions/dimer/1b_gle/he_COM_distances.txt')
he_com_pimd = np.loadtxt('./data/position_distributions/dimer/4b_piglet/he_COM_distances.txt')

bins_3 = np.linspace(0, 2, 500)
kde_class_3 = gaussian_kde(he_com_class_pileg)
kde_pimd_3 = gaussian_kde(he_com_pimd)

plot_distribution_nolegend(
    ax3,
    [he_com_class_pileg, he_com_class_gle, he_com_pimd],
    SIMULATION_LABELS,
    bins_3,
    kde_class_3,
    kde_pimd_3,
)

# ---------------------------------------------------------------------------
# AXIS 4 — Monomer He distance from cage COM
# ---------------------------------------------------------------------------
he_com_class_pileg_mono = np.loadtxt('./data/position_distributions/monomer/1b_pileg/he_COM_distances.txt')
he_com_class_gle_mono = np.loadtxt('./data/position_distributions/monomer/1b_gle/he_COM_distances.txt')
he_com_pimd_mono = np.loadtxt('./data/position_distributions/monomer/4b_piglet/he_COM_distances.txt')

bins_4 = np.linspace(0, 2, 500)
kde_class_4_mono = gaussian_kde(he_com_class_pileg_mono)
kde_pimd_4_mono = gaussian_kde(he_com_pimd_mono)

plot_distribution_nolegend(
    ax4,
    [he_com_class_pileg_mono, he_com_class_gle_mono, he_com_pimd_mono],
    SIMULATION_LABELS,
    bins_4,
    kde_class_4_mono,
    kde_pimd_4_mono,
)


# ---------------------------------------------------------------------------
# Axes formatting
# ---------------------------------------------------------------------------
ax1.set_title(r'He-He RDF of $\text{He}_2$@$\text{C}_{70}^{6-}$', fontsize=16)
ax2.set_title(r'C-He RDF of $\text{He}_2$@$\text{C}_{70}^{6-}$', fontsize=16)
ax3.set_title(r'He-COM RDF of $\text{He}_2$@$\text{C}_{70}^{6-}$', fontsize=16)
ax4.set_title(r'He-COM RDF of $\text{He}$@$\text{C}_{70}^{6-}$', fontsize=16)

ax1.set_xlabel("r [Å]", fontsize=16)
ax1.set_ylabel("Probability density", fontsize=16)
ax2.set_xlabel("r [Å]", fontsize=16)
ax2.set_ylabel("Probability density", fontsize=16)
ax3.set_xlabel(r"He distance from cage COM [Å]", fontsize=16)
ax3.set_ylabel("Probability density", fontsize=16)
ax4.set_xlabel(r"He distance from cage COM [Å]", fontsize=16)
ax4.set_ylabel("Probability density", fontsize=16)

ax1.set_xlim([1.5, 3.5])
ax2.set_xlim([2, 6])
ax2.set_ylim([-0.05, 0.68])
ax3.set_xlim([0, 2])
ax4.set_xlim([0, 2])

ax1.tick_params(axis='x', labelsize=16)
ax1.tick_params(axis='y', labelsize=16)
ax2.tick_params(axis='x', labelsize=16)
ax2.tick_params(axis='y', labelsize=16)
ax3.tick_params(axis='x', labelsize=16)
ax3.tick_params(axis='y', labelsize=16)
ax4.tick_params(axis='x', labelsize=16)
ax4.tick_params(axis='y', labelsize=16)

plt.savefig("positions_dist.png", dpi=300)
plt.show()
