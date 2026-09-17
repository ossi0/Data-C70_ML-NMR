# He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> Dataset Preparation for Training the MatTen Architecture

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---
The DATA-2 dataset contains sample structures with reference NMR magnetic shielding tensors calculated at the [DFT-2 level](../dft-2_calculations).

The dataset preparation for the training of MatTen NMR-ML architecture is comprehensively described in [this](https://github.com/ozakary/NMR-MatTen) GitHub repository, maintained by Ouail Zakary.


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

- The files `dataset_train.json`, `dataset_val.json`, and `dataset_test.json` are the final dataset files used in the [training](../nmr-ml_model) of the MatTen NMR-ML model

The `DATA-2_dataset` directory in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0) contains the dataset files for training the NMR-ML model used to predict NMR magnetic shielding tensor for He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> structures.
