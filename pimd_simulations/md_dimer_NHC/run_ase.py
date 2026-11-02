from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nose_hoover_chain import NoseHooverChainNVT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io.trajectory import Trajectory
from ase.constraints import FixCom
from ase import units
import ase.io as i
from nequip.ase import NequIPCalculator

atoms = i.read('init.xyz')

calc = NequIPCalculator.from_compiled_model(
    compile_path="gpumodel.nequip.pt2",
    device="cuda",  # "cuda" for GPUs, etc
)

atoms.set_calculator(calc)
#atoms.calc = calc
#atoms.set_calculator(calc)

atoms.set_constraint(FixCom())
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

temperature_K = 300.0                       # Kohdelämpötila Kelvineinä
timestep = 0.5 * units.fs                   # Aikajakso (1 femtosekunti)
ttime = 100 * units.fs                     # Termostaatin tyypillinen vasteaika (laimeus)

dyn = NoseHooverChainNVT(
    atoms,
    timestep=timestep,
    temperature_K=temperature_K,
    tdamp=100.0 * units.fs,
    tchain=3,             # Number of thermostat variables
    logfile="md_nhc.log",
    loginterval=20
)

# We also want to save the positions of all atoms after every 100th time step.
traj = Trajectory('moldyn.traj', 'w', atoms)
dyn.attach(traj.write, interval=20)

dyn.run(8010000)

# Read all frames from the trajectory
trajectory = i.read("moldyn.traj", index=":")

# Save all frames to a multi-frame XYZ file
i.write("md.xyz", trajectory[500:], format="xyz")
