#!/bin/bash

for i in $(seq -f "%05g" 50000 2000 500000); do
    mkdir cluster_${i}
    grep -B 1 "iter: ${i}$" geo_end.xyz > coord_${i}.xyz
    grep -A 71 "iter: ${i}$" geo_end.xyz | grep -v iter | awk '{print $1,$2,$3,$4}' >> coord_${i}.xyz
    mv -f coord_${i}.xyz ./cluster_${i}
    echo "${i}"
done
