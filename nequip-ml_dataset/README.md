# He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> Dataset Preparation for Training the NequIP Architecture

📄 Author: **Ossi Laurila**

---

👤 Corresponding Author: **Ossi Laurila**  
- 📧 Email: [Ossi.Laurila@oulu.fi](mailto:Ossi.Laurila@oulu.fi)  
- 🔗 ORCID: [0009-0002-7642-1269](https://orcid.org/0009-0002-7642-1269)  
---

This document describes the dataset preparation for the training of NequIP MLIP architecture.

## Directory Contents

The `DFT-1_dataset` directory in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0) contains the dataset necessary for training machine learning models to predict energy and forces from molecular structures. The dataset contains He@C<sub>70</sub><sup>6-</sup> and He<sub>2</sub>@C<sub>70</sub><sup>6-</sup> endohedral fullerene structures obtained from the [semi-empirical MD simulations](../dftb-md), with their corresponding energy and force components acting on each atom calculated using `ORCA`.

## Dataset Files

The dataset is provided in .xyz and .db file formats:

1. **molecules.xyz**: Contains structural information for all structures assigned to the dataset in plain xyz-format
2. **molecules.db**: Contains structural information for all structures assigned to the dataset in db-format

The molecules.xyz file has standard xyz file structure
   - `energy` : Gives the target energy of the structure in units of eV
   - `Lattice`: Gives the cell vectors  
     **a** = a<sub>x</sub>**e**<sub>x</sub> + a<sub>y</sub>**e**<sub>y</sub> + a<sub>z</sub>**e**<sub>z</sub>  
     **b** = b<sub>x</sub>**e**<sub>x</sub> + b<sub>y</sub>**e**<sub>y</sub> + b<sub>z</sub>**e**<sub>z</sub>  
     **c** = c<sub>x</sub>**e**<sub>x</sub> + c<sub>y</sub>**e**<sub>y</sub> + c<sub>z</sub>**e**<sub>z</sub>  
   - `Properties`: Provide the structural properties in the form of `properties=property_name:data_type:number_of_columns`  
     but only the following items are read
     - `species:S:1` chemical symbol of the element
     - `pos:R:3` position vector of an atom
     - `force:R:3` target (DFT) force vector acting on an atom

## File Structure Example

An example of dataset file **train.xyz** structure:
```
71
Lattice="50.0 0.0 0.0 0.0 50.0 0.0 0.0 0.0 50.0" Properties=species:S:1:pos:R:3:forces:R:3 energy=-10886.382689310209 pbc="F F F"
C -0.90388099 3.28138679 0.93121823 -2.718522162591028 -1.1844457895808127 -1.0067518538199323
C -2.10528135 2.86841803 0.22678107 -0.3410666034649885 1.4558032040403475 0.5716066883599463
...
He 0.72728959 -0.05933568 0.91509826 -0.032533775576327736 -0.0025703847088674615 -0.0395668550373232
72
Lattice="50.0 0.0 0.0 0.0 50.0 0.0 0.0 0.0 50.0" Properties=species:S:1:pos:R:3:forces:R:3 energy=-10959.816447522751 pbc="F F F"
C 3.37893772 -1.07374787 0.32066633 -0.9704594435884307 -0.27619106001675364 -0.5893267227548175
C 2.82117665 -2.38118101 0.22454359 1.2771617996292226 0.996297547470655 3.677239572315476
...
He -0.74684644 -0.91460710 0.63982196 0.08157922756005838 -0.05677704993771783 -0.0022365364302036
```


## Dataset Preparation

The dataset **molecules.xyz** was prepared using a Python script (`createxyz.py`) that process the output files from a single ORCA calculation and produces an xyz-file containing the structural data with the target energy and gradients.  

### Scripts

### `createxyz.py`

1. Extracts atomic coordinates from `coordinates.xyz` file
2. Reads DFT energy and forces from ORCA output file `opt.engrad`
3. Creates xyz file (`ref.xyz`) of the structure with DFT target energy and forces

### `create_db.py`

1. Reads the `molecules.xyz` file
2. Writes the structures to the `molecules.db` file one by one

### Running the Script

To generate the reference structure xyz-files, copy and run the Python script independently in all ORCA calculation directories (`cluster_<ID>`) each containing a single reference structure:

```bash
python3 createxyz.py
```

This can be automated to go through all directories `cluster_<ID>` with a simple bash script 

### Generating the Dataset

To generate the full **molecules.xyz** dataset, collect the individual xyz-files and merge them together with the following bash command:

```bash
awk '{print $0}' cluster_*/ref.xyz >> molecules.xyz
```

### Convert to .db format

Run the following python code to convert the `molecules.xyz`file to `molecules.db`format:

```bash
python3 create_db.py
```

## Notes

- The dataset is suitable for training NequIP or similar neural network architectures for predicting molecular energy and forces
- The dataset files are available in the [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).

---

For further details, please refer to the respective folders or contact the author via the provided email.
