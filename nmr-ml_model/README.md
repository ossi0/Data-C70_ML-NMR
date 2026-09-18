# MatTen NMR-ML model for He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup>

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

## Training process of MatTen model

The training process of a MatTen model is briefly described here.

### Input files

Training of a MatTen model requires the input file `atomic_tensor.yaml` in which the training protocol is specified, and the dataset files `dataset_train.json`, `dataset_val.json`, and `dataset_test.json`, as well as the training script file ´train_atomic_tensor.py´.

```
training_run/                      # Training directory
│   ├── configs/
│   │   └── atomic_tensor.yaml
│   ├── datasets/
│   │   ├── dataset_train.json
│   │   ├── dataset_val.json
│   │   └── dataset_test.json
│   ├── train_atomic_tensor.py
│   └── script_train.job
```

The internal hyperparameters of the model and the training process are controlled through the `config.yaml` input file.

### Starting the training

With MatTen and PyTorch 2.0.0+ installed (with Python >=3.8, <3.12), the training process of a MatTen model may be started simply with the command
```python3 train_atomic_tensor.py```

Performing the training on a HPC can be started by running the script

```bash
sbatch script_train.job
```
- Note that the job script `script_train.job` must always be configured according to the specific HPC cluster or environment in which it is intended to be used

### Output files

The training process creates the following output files:
```
training_run/
│   ├── wandb/                 # Weights & Biases (wandb) output directory, if wandb package is used used
│   ├── matten_logs/           # Output directory containing the model files in .ckpt format
│   │   └── checkpoints/
│   │       ├── last.ckpt      # Parameters of the model from the latest training step
│   │       └── best.ckpt      # Parameters of the so far best model from the training process
│   ├── matten.log             # General log file of the training
│   ├── nmr-ml_matten-errors_<JOB-ID>.txt     # Errors output file of the job script
│   └──  nmr-ml_matten-output_<JOB_ID>.txt    # Output file of the job script
```

### Compiling the model

Compilation is not required, and the trained model file `best.ckpt` is ready to be used in the [predictions](../nmr-ml_prediction).


- The trained MatTen model file can be found in the external [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0)
- The dataset files `dataset_train.json`, `dataset_val.json`, and `dataset_test.json` can also be found in the external [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).
