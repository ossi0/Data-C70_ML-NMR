import numpy as np
import matplotlib.pyplot as plt


def load_data():
    paths = {
        "class": (
            "data/sigma_predicted_dimer/1b_gle/sig_di_avg.txt",
            "data/sigma_predicted_monomer/1b_gle/sig_mono_avg.txt",
            800000,
        ),
        "pileg": (
            "data/sigma_predicted_dimer/1b_pileg/sig_di_avg.txt",
            "data/sigma_predicted_monomer/1b_pileg/sig_mono_avg.txt",
            800000,
        ),
        "pimd": (
            "data/sigma_predicted_dimer/4b_piglet/sig_di_avg.txt",
            "data/sigma_predicted_monomer/4b_piglet/sig_mono_avg.txt",
            800000,
        ),
        "8b": (
            "data/sigma_predicted_dimer/8b_piglet/sig_di_avg.txt",
            "data/sigma_predicted_monomer/8b_piglet/sig_mono_avg.txt",
            250000,
        ),
    }

    return {
        name: (
            np.loadtxt(dimer, max_rows=max_rows),
            np.loadtxt(monomer, max_rows=max_rows),
        )
        for name, (dimer, monomer, max_rows) in paths.items()
    }

# Function to calculate the statistics at given intervals
def running_stats(data, interval=50000):
    means = []
    sems = []
    intervals = range(interval, len(data) + interval, interval)

    for i in intervals:
        chunk = data[:i]
        means.append(np.round(np.mean(chunk), 3))
        sems.append(np.round(np.std(chunk) / np.sqrt(len(chunk)), 4))

    return list(intervals), means, sems

# Functions to calculate the monomer-dimer shift with other data
def process(dimer, monomer, interval=50000):
    intervals, dimer_avg, dimer_sem = running_stats(dimer, interval)
    _, mono_avg, mono_sem = running_stats(monomer, interval)

    diff = [d - m for d, m in zip(dimer_avg, mono_avg)]
    diff_sem = [
        np.sqrt(m**2 + d**2)
        for m, d in zip(mono_sem, dimer_sem)
    ]

    return intervals, mono_avg, dimer_avg, mono_sem, dimer_sem, diff, diff_sem


data = load_data()
results = {
    name: process(dimer, monomer)
    for name, (dimer, monomer) in data.items()
}

# Initialize the plot area
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(
    left=0.123, right=0.943, wspace=0.417,
    top=0.932, bottom=0.13, hspace=0.375
)

# Shielding of a free He atom
shift = 59.874

# Plot markers, linestyles and colors
styles = {
    "class": ("o", 8, "#78add2", "#ffb26e"),
    "pileg": ("*", 10, "#78add2", "#ffb26e"),
    "pimd": ("v", 8, "#78add2", "#ffb26e"),
    "8b": ("d", 8, "#78add2", "#ffb26e"),
}

handles = {}
for name, (intervals, mono, dimer, mono_sem, dimer_sem, diff, diff_sem) in results.items():
    marker, size, mono_color, dimer_color = styles[name]
    x = np.array(intervals) / 1000

    handles[name] = (
        ax1.errorbar(
            x, [shift - a for a in mono], yerr=mono_sem,
            capsize=2.0, marker=marker, ms=size, color=mono_color
        ),
        ax1.errorbar(
            x, [shift - a for a in dimer], yerr=mono_sem,
            capsize=2.0, marker=marker, ms=size, color=dimer_color
        ),
    )

# Plot the chemical shift data
ax1.set_xlabel("Number of snapshots (x1000)", fontsize=14)
ax1.set_ylabel(r'$^{3}\text{He}\ \delta_{\text{iso}}$ (ppm)', fontsize=14)
ax1.tick_params(axis="both", labelsize=14)
ax1.set_ylim(8.65, 9.35)
ax1.set_xlim(0, 820)
ax1.set_xticks([0, 200, 400, 600, 800])
ax1.legend(
    [
        handles["8b"][0], handles["8b"][1],
        handles["pimd"][0], handles["pimd"][1],
        handles["class"][0], handles["class"][1],
        handles["pileg"][0], handles["pileg"][1],
    ],
    [
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=8, PIGLET)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=8, PIGLET)',
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=4, PIGLET)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=4, PIGLET)',
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=1, GLE)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=1, GLE)',
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=1, PILE-G)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=1, PILE-G)',
    ],
    fontsize=10, loc="center right", bbox_to_anchor=(0.9, 0.59)
)

diff_styles = {
    "class": ("o", "tomato"),
    "pileg": ("*", "orange"),
    "pimd": ("v", "slateblue"),
    "8b": ("d", "limegreen"),
}

diff_handles = {}
for name, (intervals, _, _, _, _, diff, diff_sem) in results.items():
    marker, color = diff_styles[name]
    diff_handles[name] = ax2.errorbar(
        np.array(intervals) / 1000, diff, yerr=diff_sem,
        capsize=2.0, marker=marker, color=color
    )

# Plot the monomer-dimer shift data
ax2.set_xlabel("Number of snapshots (x1000)", fontsize=14)
ax2.set_ylabel(r'$^{3}\text{He}\ \Delta\delta_{\text{iso}}$ (ppm)', fontsize=14)
ax2.tick_params(axis="both", labelsize=14)
ax2.set_xlim(0, 820)
ax2.set_xticks([0, 200, 400, 600, 800])
ax2.set_yticks([0, 0.05, 0.1, 0.15, 0.2])
ax2.set_ylim(0, 0.20)

exp = ax2.axline(
    xy1=(0, 0.154), slope=0,
    color="brown", linestyle="--", linewidth=3
)

ax2.legend(
    [exp, diff_handles["8b"], diff_handles["pimd"],
     diff_handles["class"], diff_handles["pileg"]],
    [r'${^a}$exp', "P=8, PIGLET", "P=4, PIGLET",
     "P=1, GLE", "P=1, PILE-G"],
    fontsize=10, loc="lower left"
)

# Save the figure
plt.savefig("sigma_nplot_anion.png", dpi=300)
plt.show()
