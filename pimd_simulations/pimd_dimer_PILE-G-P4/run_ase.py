from ase.calculators.socketio import SocketClient, SocketIOCalculator
from ase.io import read

from nequip.ase import NequIPCalculator

# ###### Define geometry to initialize   ################

atoms = read('init.xyz')

# ################# Set calculator ######################

calc = NequIPCalculator.from_compiled_model(
    compile_path="gpumodel.nequip.pt2",
    device="cuda",  # "cuda" for GPUs, etc
)

atoms.set_calculator(calc)

# ################# Create Client ############################
# inet
port_ipi = 30110
host_ipi = "localhost"
client = SocketClient(host=host_ipi, port=port_ipi)

client.run(atoms)
