#!/bin/bash

################################################################
## ******** EXAMPLE SLURM SUBMISSION SCRIPT FOR I-PI ******** ##
################################################################

## These are the usual SLURM specs, not specifically i-PI related
## ^^^ N.B. the job must last a couple of minutes longer 
## than the <total_time> setting inside input.xml

## ^^^ N.B. it is important that all jobs are allocated to the same
## node because Unix domain sockets use the filesystem

## It is good to fix the memory per process, as on some systems
## otherwise the first driver reserves all the RAM

#SBATCH --job-name=mo_an1b
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

## ******* Here starts the actual submission script ******* 

## We assume i-pi (and the driver code) are in the path, otherwise
## you have to set this environment variable
IPI_INPUT=PREFIX.chk

## Driver command
IPI_DRIVER="i-pi-driver -a slurm-one-node -m zundel -u -v"

## Launches i-PI
srun -n 1 i-pi $IPI_INPUT &> log.ipi &

## Gives a few seconds to allow the server to open the Unix socket
## For *very* complicated simulations you may need to increase a bit
sleep 5;

## Launches the driver code
for nbead in $(seq 1 1 1); do
    python3 run_ase.py
done

# Record end time
end_time=$(date +"%Y-%m-%d %H:%M:%S")
echo "Job finished at $end_time"

## Waits for all jobs to be finished
wait

# Record end time
end_time=$(date +"%Y-%m-%d %H:%M:%S")
echo "Job finished at $end_time"

# Calculate and print execution time
start_seconds=$(date -d "$start_time" +"%s")
end_seconds=$(date -d "$end_time" +"%s")
execution_time=$((end_seconds - start_seconds))
echo "Job took $execution_time seconds to complete."
