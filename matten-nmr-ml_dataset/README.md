# He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> Dataset Preparation for Training the MatTen Architecture

📄 Author: **Ossi Laurila**

---

👤 Corresponding Author: **Ossi Laurila**  
- 📧 Email: [Ossi.Laurila@oulu.fi](mailto:Ossi.Laurila@oulu.fi)  
- 🔗 ORCID: [0009-0002-7642-1269](https://orcid.org/0009-0002-7642-1269)  

---
The DATA-2 dataset contains sample structures with reference NMR magnetic shielding tensors calculated at the [DFT-2 level](../dft-2_calculations).

The dataset preparation for the training of MatTen NMR-ML architecture, starting from finished `TURBOMOLE`NMR shielding calculations is comprehensively described in [this](https://github.com/ozakary/NMR-MatTen) GitHub repository, maintained by Ouail Zakary.


## Dataset Files

Performing the dataset preparation produces the following files:
```
matten_dataset_output/
├── dataset_train.json              # Training set
├── dataset_val.json                # Validation set
├── dataset_test.json               # Test set
├── dataset_test_structures.xyz     # Test structures (XYZ format)
├── structures_with_sigma_iso_and_tensors.csv  # Test data (CSV)
└── config.txt                      # Configuration used
```

- The files `dataset_train.json`, `dataset_val.json`, and `dataset_test.json` are the final dataset files used in the [training](../matten-nmr-ml_model) of the MatTen NMR-ML model

The `DATA-2_dataset` directory in the [Fairdata repository](https://doi.org/TBA) contains the dataset files for training the NMR-ML model used to predict NMR magnetic shielding tensor for He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> structures.
