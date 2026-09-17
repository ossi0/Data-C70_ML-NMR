# He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> NMR magnetic shielding DFT Calculations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This repository contains the structure generation conditions for the DATA-2 dataset, and calculation conditions used in the DFT reference data computations for the NMR-ML model of He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> endohedral fullerene systems described in the paper “***Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects***”.

ADD LINK

[![DOI](https://img.shields.io/badge/DOI-10.1021%2Facs.jpca.6c00238-yellow.svg)](https://doi.org/10.1021/acs.jpca.6c00238)

## Overview of the Data

This project contains the computational conditions for He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> structures. Each structure was computed using the computational conditions described in the sections below.  

The reference DFT values are calculated for all structures in the reference dataset at the DFT-2 theory level with TURBOMOLE as described in the paper.

Here we provide one example calculation folder `cluster_<ID>`. The input files for this example DFT calculation data files can be found in the corresponding subdirectories in this GitHub page.

The output files and the calculation results of the example provided here can be found in this [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0). The reference energy and force values from all of the ORCA calculations are available in the data set files in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).

Calculation directory structure example:
```
./cluster_<ID>/
    basis 
    auxbasis 
    control
    coord
    coordinates_<ID>.xyz
    tm_puhti.job 
```
The `coord` file is the coordinate file used by TURBOMOLE, and can be created from the `coordinates_<ID>.xyz` file by running the TURBOMOLE command
```bash
x2t coordinates_<ID>.xyz > coord
```
To start the calculation, all the necessary TURBOMOLE input files should be included in the desired directory. The calculation produces the following output files:
```
    energy 
    gradient 
    jobfile.err<JOB_ID> 
    jobfile.out<JOB_ID> 
    mpshift.out 
    rdgard.out
    ridft.out 
    shieldings 
    statistics 
```
    

## Computational Details

### General Settings
- **Program Package**: `TURBOMOLE V7.8`
- **Systems**: He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> endohedral fullerenes
