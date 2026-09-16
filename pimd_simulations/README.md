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
Two sub-directories are provided  
- [pimd_mono_equil](./pimd_mono_equil)
- [pimd_mono_production](./pimd_mono_production)

The structure of each directory is:

```
./
    init.xyz                # Input structure of the initial configuration used in the simulation
    gpumodel.nequip.pt2     # The compiled NequIP model to be used with GPU
    run_ase.py              # Python script that attaches the NequIP model to a ASE calculator for the force predictions during the simulations
    job_base.sh             # Script to launch the simulation on HPC
    input.xml/PREFIX.chk    # Input/checkpoint file for the simulation settings and protocol to start/continue the simulation
```


## Workflow
Necessary files to start PIMD simulation using [i-PI](https://github.com/i-pi/i-pi) with [ASE](https://ase-lib.org) as a client, are `init.xyz`, `input.xml`, `job_base.sh`, `gpumodel.nequip.pt2`, and `run_ase.py`.

1. Install PyTorch >= 2.2, [NequIP](https://github.com/mir-group/nequip), [i-PI](https://github.com/i-pi/i-pi) and [ASE](https://ase-lib.org) with Python >= 3.10
2. Check and define the simulation protocol file `input.xml`, or alternatively the checkpoint file ´PREFIX.chk´ if continuing a simulation from the checkpoint file
3. Change the port number as desired in the `run_ase.py` Python script
4. Check the job_base.sh script and start the simulation by running it with
```bash
sbatch job_base.sh
```


For further details, please contact the author via the provided email.
