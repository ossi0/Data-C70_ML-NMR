# Supporting Code for “*Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects*”

## Graphical Abstract

![Graphical Abstract](./graphical_abstract.png)

---

📄 Author: **Ossi Laurila**

---

👤 Corresponding Author: **Ossi Laurila**  
- 📧 Email: [Ossi.Laurila@oulu.fi](mailto:Ossi.Laurila@oulu.fi)  
- 🔗 ORCID: [0009-0002-7642-1269](https://orcid.org/0009-0002-7642-1269)  

---

This is the supporting code for the manuscript “***Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects***”. [DOI: https://doi.org/TBA]

The repository comprises the following sections:

1. Dataset preparation for the MLIP model:  
   i. Configuration generation using semi-empirical MD simulations. ([directory](./dftb-md/))  
   ii. DFT calculations of the generated SE-MD configurations for training the MLIP model. ([directory](./dft-1_calculations/))  
   iii. Dataset format of the MLIP models. ([directory](./nequip-ml_dataset/))  
3. Example of training, validation, and testing processes for a MLIP model using NequIP architecture. ([directory](./nequip-ml_model/))  
4. Machine learning-assisted path-integral MD simulations. ([directory](./pimd_simulations/))  
5. Dataset preparation for the NMR-ML model:  
   i. Configuration generation and DFT calculations for the NMR-ML model. ([directory](./dft-2_calculations/))  
   ii. Dataset format for the NMR-ML model. ([directory](./nmr-ml_dataset/))  
6. Training, validation, and testing processes for the NMR-ML model using MatTen architecture on NMR magnetic shielding parameters. ([directory](./nmr-ml_model/))  
7. Prediction of NMR magnetic shielding tensors, *σ*, from the pre-trained NMR-ML model. ([directory](./nmr-ml_prediction/))  
8. Python scripts and raw numerical data for all figures related to the NMR-ML model included in the main manuscript and the Supporting Information. ([directory](./figures/))  

## Citations
If you use this data, please cite the following:

### Paper [![DOI](https://img.shields.io/badge/DOI-10.1021%2Facs.jpca.6c00238-yellow.svg)](https://doi.org/TBA)

```bibtex
@article{laurila_2026_c70_ml_nmr,
  title={Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects},
  author={Laurila, Ossi, and Zakary, Ouail and Lantto, Perttu},
  journal={XXX},
  year={2026},
  volume = {XXX},
  number = {XX},
  pages = {XXXX--XXXX},
  doi={TBA},
  url={TBA}
}
```

### Dataset [![DOI](https://img.shields.io/badge/DOI-10.23729%2Ffd--c64c043e--473e--371d--9586--8fd3d04e2fb0-blueviolet.svg)](https://doi.org/TBA)

```bibtex
@dataset{laurila_2025_data_c70_ml_nmr,
  author = {Laurila, Ossi, and Zakary, Ouail and Lantto, Perttu},
  title = {Supporting Data for "Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects"},
  year = {2026},
  publisher = {Fairdata},
  doi = {TBA},
  url = {TBA}
}
```

### Code [![DOI](https://img.shields.io/badge/GitHub-ossi0%2FData--C70__ML--NMR-blue.svg)](https://github.com/ossi0/Data-C70_ML-NMR)
```bibtex
@misc{laurila_2026_github_c70_ml_nmr,
  author = {Laurila, Ossi, and Zakary, Ouail and Lantto, Perttu},
  title = {Supporting Code for "Machine Learning For NMR Observables Sensitive to Nuclear Quantum Effects"},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ossi0/Data-C70_ML-NMR}},
  url = {https://github.com/ozakary/Data-C70_ML-NMR}
}
```

---
For further details, please refer to the respective folders or contact the author via the provided email.
