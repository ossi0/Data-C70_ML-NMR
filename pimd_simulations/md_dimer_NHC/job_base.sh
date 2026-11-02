#!/bin/bash

#SBATCH --job-name=di_nhc
#SBATCH --time=36:00:00
#SBATCH --mem-per-cpu=8G
#SBATCH --nodes=1
#SBATCH --output=results.out
#SBATCH --error=error.out
#SBATCH --account=plantto
#SBATCH --partition=gpumedium
#SBATCH --ntasks-per-node=1 --cpus-per-task=72  # The product should be 72 if requesting 1 GPU per node
#SBATCH --gres=gpu:gh200:1  # Corresponds to 1 GPU per node

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

module load cuda/12.9.1

## Needed since SLURM 22.05 so that srun picks up just one CPU per task
export SRUN_CPUS_PER_TASK=1

module load python-data
source /scratch/plantto/olaurila/allegro/allegro-venv/bin/activate

# Record start time
start_time=$(date +"%Y-%m-%d %H:%M:%S")
echo "Job started at $start_time"
sim=${1}
echo ${sim}
## ******* Here starts the actual submission script *******

python3 run_ase.py

# Record end time
end_time=$(date +"%Y-%m-%d %H:%M:%S")
echo "Job finished at $end_time"

# Calculate and print execution time
start_seconds=$(date -d "$start_time" +"%s")
end_seconds=$(date -d "$end_time" +"%s")
execution_time=$((end_seconds - start_seconds))
echo "Job took $execution_time seconds to complete."
