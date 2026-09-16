# He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> energy and gradient DFT Calculations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This repository contains the calculation conditions used in the DFT reference data computations for the MLIP machine learning interatomic potential of He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> endohedral fullerene systems described in the paper “***Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects***”.

ADD LINK

[![DOI](https://img.shields.io/badge/DOI-10.1021%2Facs.jpca.6c00238-yellow.svg)](https://doi.org/10.1021/acs.jpca.6c00238)

## Overview of the Data

This project contains computational data for He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> structures. Each structure was computed using the computational conditions described in the sections below.  

The reference DFT values are calculated for all structures in the reference dataset at the DFT-1 theory level with ORCA as described in the paper.

Here we provide one example calculation folder `cluster_<ID>`. The input files for this example DFT calculation data files can be found in the corresponding subdirectories in this GitHub page.

The output files and the calculation results of the example provided here can be found in this [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0). The reference energy and force values from all of the ORCA calculations are available in the data set files in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).

Calculation directory structure example:
```
./cluster_<ID>/
    opt.inp 
    coordinates.xyz 
    mahti_orca.job 
```
To start the calculation, all the necessary ORCA input files should be included in the desired directory. The calculation produces the following output files:
```
    energy 
    opt.engrad 
    jobfile.err<JOB_ID> 
    jobfile.out<JOB_ID> 
    Jobid_is_<JOB_ID> 
    opt_atom6.bibtex 
    opt_atom6.densities 
    opt_atom6.densitiesinfo 
    opt_atom6.out 
    opt_atom6.property.txt 
    opt_bibtex 
    opt_densities 
    opt_densitiesinfo 
    opt_gbw 
    opt_out 
    opt_property.txt 
    opt.xyz 
```
    

## Computational Details

### General Settings
- **Program Package**: `ORCA V6.1.1`
- **Systems**: He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> endohedral fullerenes
- **Calculation Type**: DFT optimization

### DFT Methods
- **DFT level**: `ωB97X-3c` composite hybrid method
- **Basis Set**:  
- `vDZP` for both helium and carbon atoms
- **Auxiliary basis set**:
- `def2/J` for both helium and carbon atoms
- **Dispersion Correction**:  
- `D4` dispersion parametrisation specifically adapted by the composite hybrid method

### SCF Parameters
ORCA `**TightSCF**` criteria used:
- **energy change between two cycles (TolE)**: 10<sup>-8</sup>
- **RMS density change (TolRMSP)**: 5.0<sup>-9</sup>
- **maximum density change (TolMaxP)**: 1.0<sup>-7</sup>
- **DIIS error convergence (TolErr)**: 5.0<sup>-7</sup>
- **orbital gradient convergence (TolG)**: 1.0<sup>-5</sup>
- **orbital rotation angle convergence (TolX)**: 1.0<sup>-5</sup>
- **ConvCheckMode = 2**: check change in total energy and in one-electron energy; converged if Δ(Etot) < TolE and Δ(E1) < 1.0<sup>-3</sup>*TolE

### System Properties
- **Number of Atoms**: 71/72
- **Basis set**: 
  - 915/920 basis functions
  - 353/356 number of shells
- **Auxiliary Coulomb fitting Basis**: 
  - 3441/3452 basis functions in Aux-J
  - 1055/1060 number of shells in Aux-J

## Requirements to Reproduce This Data
- **Package**: [ORCA V6.1.1](https://www.faccts.de/docs#orca)
- **Input files**:
  - [opt.inp](./cluster_1000/opt.inp): Orca input file
  - [coordinates.xyz](./cluster_1000/coordinates.xyz): Coordinate file in xyz format
- **Additional scripts**:
  - [mahti_orca.job](./cluster_1000/mahti_orca.job): Script to call ORCA DFT optimisation calculation in supercomputer Mahti ([https://www.mahti.csc.fi/public](https://www.mahti.csc.fi/public/)/)
 
### Workflow of DFT calculations

1. Call the job script to start the calculation
2. Extract and analyse the results

---

- **Computational Resource**: [CSC](https://csc.fi/) Supercomputer [MAHTI](https://www.mahti.csc.fi/public/)

  
- For details, please refer to the respective folders or contact the author via the provided email.
