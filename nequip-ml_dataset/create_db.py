from ase.io import db
import ase.db
from ase.db import connect
from ase.io import read as read
from ase import Atoms
import numpy as np

#WRITE TO DATABASE

atomspath = './molecules.xyz'
atoms = read(atomspath, index=':')
pos = [atom.get_positions() for atom in atoms]
db.write_db('molecules.db', atoms)
