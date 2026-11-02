import numpy as np
import matplotlib.pyplot as plt


def load_data():
    paths = {
        "nhc": (
            "data/sigma_predicted_dimer/1b_nhc/sig_di_avg.txt",
            "data/sigma_predicted_monomer/1b_nhc/sig_mono_avg.txt",
            1100000,
        ),
        "pimd": (
            "data/sigma_predicted_dimer/4b_piglet/sig_di_avg.txt",
            "data/sigma_predicted_monomer/4b_piglet/sig_mono_avg.txt",
            875000,
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
        means.append(np.round(np.mean(chunk), 5))
        sems.append(np.round(np.std(chunk) / np.sqrt(len(chunk)), 5))

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
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
fig.subplots_adjust(
    left=0.151, right=0.957, wspace=0.2,
    top=0.97, bottom=0.077, hspace=0.177
)

# Shielding of a free He atom
shift = 59.8627

# Plot markers, linestyles and colors
styles = {
    "nhc": ("o", 6, "#78add2", "#ffb26e"),
    "pimd": ("v", 6, "#78add2", "#ffb26e"),
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
#ax1.set_xlabel("Number of snapshots (x1000)", fontsize=14)
ax1.set_ylabel(r'$^{3}\text{He}\ \langle \delta_{\text{iso}} \rangle$ (ppm)', fontsize=14)
ax1.tick_params(axis="both", labelsize=14)
ax1.set_ylim(8.7, 9.4)
ax1.set_xlim(0, 1200)
ax1.set_xticks([0, 200, 400, 600, 800, 1000, 1200])
ax1.grid(True)

exp_mono = ax1.axline(
    xy1=(0, 8.198), slope=0,
    color="black", linestyle="solid", linewidth=3
)
exp_di = ax1.axline(
    xy1=(0, 8.044), slope=0,
    color="black", linestyle="--", linewidth=3
)

ax1.legend(
    [
        handles["pimd"][0], handles["pimd"][1],
        handles["nhc"][0], handles["nhc"][1]
    ],
    [
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=4)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=4)',
        r'${\delta}_{\text{iso}}[\text{mono}]$ (P=1)',
        r'${\delta}_{\text{iso}}[\text{dimer}]$ (P=1)'
    ],
    #fontsize=10, loc="upper right", bbox_to_anchor=(0.996, 0.996)
    fontsize=10, loc="best"
)

diff_styles = {
    "nhc": ("o", "blue"),
    "pimd": ("v", "red"),
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
ax2.set_xlim(0, 1200)
ax2.set_xticks([0, 200, 400, 600, 800, 1000, 1200])
ax2.set_yticks([0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18])
ax2.set_ylim(0.04, 0.18)
ax2.grid(True)

exp = ax2.axline(
    xy1=(0, 0.154), slope=0,
    color="black", linestyle="--", linewidth=2
)

eq_geom = ax2.axline(
    xy1=(0, 0.161), slope=0,
    color="brown", linestyle="--", linewidth=2
)

ax2.legend(
     [exp, eq_geom, diff_handles["pimd"],
     diff_handles["nhc"]],
    [r'exp', r'eq. geom.', "P=4", "P=1"],
    fontsize=10, loc="lower right"
)

# Save the figure
plt.savefig("figure_6.png", dpi=300)
plt.show()
