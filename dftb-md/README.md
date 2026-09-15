# He<sub>n</sub>@C<sub>70</sub> (n = 1,2) Semi-Empirical MD Using DFTB+ Code

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

## Producing the reference dataset structures of C<sub>60</sub>

This directory contains the necessary input files to reproduce the semi-empirical MD data with DFTB+ software. The configurations of the output MD trajectory are used as reference data in the training of NequIP MLIP model. The output files, including the snapshots taken from the semi-empirical MD simulation can be found in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0) of this project.

### DFTB+ input files

All the necessary files needed to start the MD simulation with DFTB+ are provided here. The structure of the directory is as follows:
```
./
     dftb_in.hsd        # The main input file for DFTB+
     dftb_pin.hsd       # Processed and parsed input file created by the DFTB+ software, preferred over dftb_in.hsd to repeat the simulation
     geom.out.gen       # The initial He@C70/He2@C70 configuration in the generic format
     geom.out.xyz       # The initial He@C70/He2@C70 configuration in the xyz format
     puhti_dftb.job     # Job script to run DFTB+ in Puhti HPC
     prepare.sh         # Shell script for preparing DFT calculations, not used in DFTB+ simulation
```

- Note that if you want to exactly repeat the calculation, you are strongly suggested to remove the `dftb_in.hsd`, and then rename the file `dftb_pin.hsd` as `dftb_in.hsd`  
- The additional script file `prepare.sh` is used after the DFTB+ simulation has finished to extract snapshot structures from the simulation trajectory.


### Scripts

Scripts used to analyze the MD trajectory and to initialize the [DFT calculations](../dft-1_calculations) for the structures produced in the MD simulation are presented below.  

### `prepare.sh`

After the DFTB+ calculation has been completed this shell script prepares the results for the DFT calculations of the reference He@C<sub>70</sub>/He<sub>2</sub>@C<sub>70</sub> configurations.  
Running the script with the command `./prepare.sh` creates the following file structure:
```
./cluster_50000
    coord_50000.xyz
./cluster_52000
    coord_52000.xyz
./cluster_54000
    coord_54000.xyz
...
```
Note that the first selected configuration is `cluster_50000`, since the beginning of the semi-empirical MD simulation is discarded due to the equilibration stage of the simulation.

Follow the instruction in [dft-1_calculations](../dft-1_calculations) or [dft-2_calculations](../dft-2_calculations) to run the DFT calculations for the He@C<sub>70</sub>/He<sub>2</sub>@C<sub>70</sub> configurations.


---

For further details, please refer to the original [DFTB+]([https://github.com/brucefan1983/GPUMD](https://github.com/dftbplus/dftbplus)) documentation or contact the author via the provided email.
