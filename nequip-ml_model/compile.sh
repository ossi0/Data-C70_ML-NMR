#!/bin/bash

#--------------------------------------------------------------------------------------------------------------------------------
#SBATCH --job-name=compile
#SBATCH --partition=gpu
#SBATCH --account=plantto # !!it is mandatory to specify the account (project) as precised in the CSC rules!!
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=01:00:00
#SBATCH --gres=gpu:v100:1,nvme:25
#SBATCH --output=model_compile-out.txt
#SBATCH --error=model_compile-errors.txt
#--------------------------------------------------------------------------------------------------------------------------------

# Record start time
start_time=$(date +"%Y-%m-%d %H:%M:%S")
echo "Job started at $start_time"

# Activate virtual environment
module load gcc/13.2.0
module load cuda/12.6.0
module load pytorch/2.6
source /scratch/plantto/olaurila/allegro/allegro-venv/bin/activate
nequip-compile ./best.ckpt ./model_gpu.nequip.pt2 --device cuda --mode aotinductor --target ase
