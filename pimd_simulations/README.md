# Machine Learning-Assisted Path Integral Molecular Dynamics (MLPIMD) Simulations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---
This sub-repository contains example input files and workflow for the PIMD simulations of He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> with [i-PI](https://github.com/i-pi/i-pi) code. 

Example PIMD simulation runs with the resulting output files for the He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> structures are provided in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0) of this project. Unfortunately it is not possible to provide all of the simulation output data in the IDA repository, due to the massive amount of PIMD simulation data.

## Directory Structure


### PIMD simulations of He@C<sub>70</sub><sup>6-</sup>
Four sub-directories are provided, which include the input files to start the equilibrium and production simulation runs
- [pimd_mono_GLE](./pimd_mono_GLE)
- [pimd_mono_PILE-G](./pimd_mono_PILE-G)
- [pimd_mono_PIGLET_P4](./pimd_mono_PIGLET_P4)
- [pimd_mono_PIGLET_P8](./pimd_mono_PIGLET_P8)

The structure of each directory is:

```
./
    init.xyz                # Input structure of the initial configuration used in the simulation
    gpumodel.nequip.pt2     # The compiled NequIP model to be used with GPU
    run_ase.py              # Python script that attaches the NequIP model to ASE calculator for the force predictions during the simulations
    job_base.sh             # Script to launch the simulation on HPC
    input.xml               # Input file for the simulation settings and protocol to start the equilibration simulation
    PREFIX.chk              # Checkpoint file for the simulation settings and protocol to continue the simulation
```

- Note that the MLPIMD simulations of He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> are conducted as are the He@C<sub>70</sub><sup>6-</sup>, with only the initial geometry `init.xyz`, and the checkpoint file `PREFIX.chk` differing from the corresponding files used in the He@C<sub>70</sub><sup>6-</sup> simulations

The `IPI_INPUT`variable in the `job_base.sh` script must be set to
  **input.xml**
- in the case of running an equilibrium simulation

and to **PREFIX.chk**
- if intending to run a production simulation run starting from the equilibrated simulation state, or 
- continuing the simulation in a new simulation run starting from the last simulation state in the previous simulation run 

## Workflow
Necessary files to start PIMD simulation using [i-PI](https://github.com/i-pi/i-pi) with [ASE](https://ase-lib.org) as a client, are `init.xyz`, `input.xml`, `job_base.sh`, `gpumodel.nequip.pt2`, and `run_ase.py`.

1. Install PyTorch >= 2.2, [NequIP](https://github.com/mir-group/nequip), [i-PI](https://github.com/i-pi/i-pi) and [ASE](https://ase-lib.org) with Python >= 3.10
2. Check and define the simulation protocol file `input.xml`, or alternatively the checkpoint file ´PREFIX.chk´ if continuing a simulation from the checkpoint file
3. Change the port number as desired in the `run_ase.py` Python script
4. Check the job_base.sh script and start the simulation by running it with
```bash
sbatch job_base.sh
```

## Output Files

After running the simulation, you will have the following output files:


```
./
    log.ipi               # Simulation log file
    results.out           # Output file printing the simulation starting and ending times, with the total simulation length 
    error.out             # Output file for printing errors occurring during the simulation
    RESTART               # File produced when the simulation finishes cleanly, in order to restart the simulation
    PREFIX.out            # Output file containing energy, temperature, etc. of the system during the simulation
    PREFIX.for_<p>.xyz    # xyz-file containing the forces components acting on the atoms at intervals of simulation steps
    PREFIX.pos_<p>.xyz    # xyz-file containing the positions of the atoms at intervals of simulation steps
    PREFIX.chk            # Checkpoint file produced, containing the exact state of the simulation at given simulation step
```
- `p` is the bead number, and it ranges from `0` to `P-1`, with `P` being the bead number used in the PIMD simulation
---

For further details, please refer to the respective folders or contact the author via the provided email.
