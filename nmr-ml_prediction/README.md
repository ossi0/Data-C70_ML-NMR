# Prediction of NMR Magnetic Shielding from the Pre-Trained NMR-ML MatTen Model  

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This sub-repository contains code and workflows for predicting NMR magnetic shielding tensor for helium atoms using the pre-trained MatTen model. The workflow is specifically designed to handle Path Integral Molecular Dynamics (PIMD) simulation data with any number of beads.

## Overview

The prediction workflow processes PIMD simulation data across the beads, splitting large trajectory files into chunks of structures (the size of the chunk depending on the simulation length). The chunk trajectory files are given as input for the NMR-ML model to predict (using CPU) the NMR magnetic shielding tensor.

## Directory Structure

The workflow uses the following directory structure:

```
./0/
    script_predict.job           # Main prediction job script
    predict_atomic_tensor.py     # Python prediction script
    PREFIX.pos_0.xyz             # Trajectory file from the PIMD simulation for bead with index P=0
...
./<p-1>/
    script_predict.job           # Main prediction job script
    predict_atomic_tensor.py     # Python prediction script
    PREFIX.pos_<p-1>.xyz         # Trajectory file from the PIMD simulation for bead with index P=p-1

./calc_avg.py       # Auxiliary Python script calculating the bead-averaged isotropic NMR magnetic shielding afterwards
./config_final.yaml    # MatTen model configuration file
./model.ckpt           # The trained NMR-ML model file
```

Alternatively, the prediction of the NMR magnetic shielding tensor from the chunk trajectory files can be parallelized, as is the case in the example input directories [NMR-P1_dimer](./NMR-P1_dimer) and [NMR-P1_monomer](./NMR-P1_monomer). In this case, the directory structure in as follows: 

```
./0/
    script_predict0.job           # Main prediction job script with parallelisation
    script_predict1.job           # Main prediction job script with parallelisation
    ...
    script_predict<N>.job         # Main prediction job script with parallelisation
    predict_atomic_tensor.py      # Python prediction script
    PREFIX.pos_0.xyz              # Trajectory file from the PIMD simulation for bead with index P=0
...
./<P-1>/
    script_predict0.job           # Main prediction job script with parallelisation
    script_predict1.job           # Main prediction job script with parallelisation
    ...
    script_predict<N>.job         # Main prediction job script with parallelisation
    predict_atomic_tensor.py      # Python prediction script
    PREFIX.pos_<p-1>.xyz          # Trajectory file from the PIMD simulation for bead with index P=p-1

./calc_avg.py       # Auxiliary Python script calculating the bead-averaged isotropic NMR magnetic shielding afterwards
./config_final.yaml    # MatTen model configuration file
./model.ckpt           # The trained NMR-ML model file
```

## Workflow Steps


### 1. Copy XYZ Files to Bead Directories

Copy the corresponding trajectory files to each bead directory:

```bash
for i in $(seq 0 1 <P-1>); do 
  cp ./path/to/simulation/dir/PREFIX.pos_${i}.xyz ${i}/
done
```

### 2. Split Trajectories into Chunks

Split the trajectory files PREFIX.pos_<P-1>.xyz into chunks of 100 structures in order to prevent memory issues during the prediction. Replace `<P-1>` in the following command with the bead number `P` of the simulation subtracted by one, and <LEN(structure)> by the length of an .xyz file corresponding to the simulated structure (for example, in the case of He@C<sub>70</sub><sup>6-</sup>, the length of a single structure in .xyz format is 73). Preforming the command will generate a maximum of 1000 chunks called `seg<ID>`, with <ID> in the range `0000, 0999`, including the leading zeros.

```bash
for i in $(seq 0 1 <P-1>); do 
  cd ${i}
     split -l <LEN(structure)>00 -a 4 -d PREFIX.pos_${i}.xyz seg
  cd ../
done
```
- Note that this step can be included in the `script_predict.job` script (example found [here](./NMR-P1_monomer/0/script_predict.job)), if doing no parallel prediction calculations


### 3. Run Prediction Job

Submit the prediction jobs to the HPC cluster:

- (1) Without parallel predictions:
```bash
for i in $(seq 0 1 <P-1>); do 
  cd ${i}
     sbatch script_predict.job
  cd ../
done
```

- (2) With parallel predictions (with `N` being the parallelisation index):
```bash
for i in $(seq 0 1 <P-1>); do 
  cd ${i}
     for j in $(seq 0 1 <N>); do 
        sbatch script_predict${j}.job
     done
  cd ../
done
```

**IMPORTANT**: Before running the job, ensure that the loop indices in the job script match your folder structure (number of beads and chunks), and that the chunk files are generated with the `split` command either as in **step 2**, or in the `script_predict.job` script.

### 4. Monitor Prediction Progress

Check the prediction status:

```bash
grep 'Output saved to:' nmr-ml_matten-output_<JOB-ID>.txt
```

### 5. Output files and Concatenating the Results

After all predictions are complete, the output files from the predictions are produced as follows:
```
./0/
    matten.log
    nmr-ml_matten-output_<JOB-ID>.txt  # General output file
    nmr-ml_matten-errors_<JOB-ID>.txt  # Errors output file
    output_prediction0000.csv          # Predictions from the first chunk corresponding to file seg0000
    output_prediction0001.csv          # Predictions from the second chunk corresponding to file seg0001
    ...
    output_prediction<M>.csv           # Predictions from the last chunk corresponding to file seg<M>
...
./<p-1>/
    matten.log
    nmr-ml_matten-output_<JOB-ID>.txt  # General output file
    nmr-ml_matten-errors_<JOB-ID>.txt  # Errors output file
    output_prediction0000.csv          # Predictions from the first chunk corresponding to file seg0000
    output_prediction0001.csv          # Predictions from the second chunk corresponding to file seg0001
    ...
    output_prediction<M>.csv           # Predictions from the last chunk corresponding to file seg<M>
```

Concatenate the CSV files for each bead to produce a single `predictions.csv` file:

```bash
for i in $(seq 0 1 <P-1>); do 
  cd ${i}
  for i in {0000..<M>}; do
     awk -v i="$i" 'NR>1 {print i$0}' output_prediction"$i".csv >> predictions.csv
  done
  cd ..
done
```
- Note that in the place of `<P-1>` and `<M>` in the command, you have to use the number of beads, and the maximum chunk index, respectively, where the maximum chunk index depends on the length of the PIMD simulation
- With no parallel predictions (only one prediction script per bead) the previous command can be included as the last command of the `script_predict.job` script

This creates consolidated CSV files for further analysis, with one file per bead, each line containing a single NMR magnetic shielding tensor prediction as well as its isotropic value:
- - `./0/predictions.csv`
- - `./1/predictions.csv`
- - ...
- - `./<P-1>/predictions.csv`

- You may now delete the chunked prediction files `output_prediction<ID>.csv`, as well as the chunked trajectory files `seg<ID>`

### 6. Calculating the bead-averaged isotropic NMR magnetic shielding

You can now extract the bead-specific isotropic NMR magnetic shielding values from the `predictions.csv` files with the command

```bash
for i in $(seq 0 1 <P-1>); do 
  cd ${i}
     grep '70,He' predictions.csv | awk -F',' '{print $7}' >> sig.txt
  cd ..
done
```

Now you can calculate the bead-averaged isotropic NMR magnetic shielding values by running the script

```bash
python3 calc_avg.py
```
- Note that you should change the variable called `beads` in the script to the correct value

The script produces a file `sig_avg.txt` containing the bead-averaged isotropic NMR magnetic shielding values with one value per line


## Script Functions

### `code_seperate.py`

This script reads a trajectory XYZ file and splits it into chunks of 1001 structures. It identifies structure boundaries in the XYZ file by looking for the "60" marker (corresponding to the number of atoms in C60) and creates separate files with the specified number of structures.

### `code_convert.py`

This script converts XYZ files to the CSV format required by SchNet. It creates a CSV file with the following columns:
- molecule_name (e.g., "empty_fullerene_100000")
- atom_index (0-59 for each atom in C60)
- atom (always "C" for carbon)
- x, y, z (atomic coordinates)

### `ml-predict.py`

This script loads the pre-trained SchNet model and predicts NMR isotropic shielding values for the provided structures. It:
1. Creates a SchNetPack-compatible database from the CSV file
2. Loads the pre-trained model
3. Makes predictions for each structure
4. Saves the results with the original structural information

### `concat_csvs.py`

This script concatenates the prediction results from each chunk into a single file per bead. It collects all `sigma_iso_new_predictions_with_structures.csv` files from each chunk directory and combines them into a single CSV file in the parent bead directory.

## Job Script Details

The `nmr-ml_predict_schnet_carpo2.job` script:
- Allocates 4 NVIDIA V100 GPUs
- Uses 16 CPU cores (4 tasks × 4 CPUs per task)
- Runs for up to 3 days
- Activates the SchNet virtual environment
- Processes each chunk of each bead sequentially, running the prediction script with appropriate parameters

## Output Files

After running the complete workflow, you will have the following output files:

1. In each bead folder (from 0 to 31):
   - `./0/predicted_sigma_iso_beads_0.csv`
   - `./1/predicted_sigma_iso_beads_1.csv`
   - ...
   - `./31/predicted_sigma_iso_beads_31.csv`

2. In each chunk folder (for all beads and chunks):
   - `./0/1/split_beads_dump_0_1.xyz` (Split trajectory chunk)
   - `./0/1/converted_split_beads_dump_0_1.csv` (Converted data for SchNet)
   - `./0/1/CHAMPS_new_test.db` (Database file for SchNet)
   - `./0/1/sigma_iso_new_predictions_with_structures.csv` (Prediction results)
   - ...
   - `./31/5/sigma_iso_new_predictions_with_structures.csv`

---

For further details, please refer to the respective folders or contact the author via the provided email.
