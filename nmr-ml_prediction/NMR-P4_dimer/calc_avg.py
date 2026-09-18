import numpy as np
import os

writefilepath = "sig_avg.txt"
beads = 4

# Calculates the average over the beads for every sample point

full_results = []
for i in range(beads):
    full_results.append(np.loadtxt(str(i) + '/sig.txt'))

with open(writefilepath, 'w') as f:
    for j in range(len(full_results[0])):
        sum = 0
        for i in range(beads):
            sum += full_results[i][j]
        f.write(str(sum/beads) + '\n')
        sum = 0
