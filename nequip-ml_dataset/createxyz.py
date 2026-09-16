# This code produces an xyz file of He@C70 or He2@C70 configuration with reference DFT energy and forces to be used in the training of NequIP ML model.

import os

# Force conversion coefficient.
C = -51.42208619083232 # Ha/Bohr to eV/<C3><85>
path = os.getcwd()
xyzfile = "coordinates.xyz"

r = open("opt.engrad", "r")
lines = r.readlines()
energy = float(lines[7].strip())*27.2114079527 # Ha to eV
num_atoms = int(lines[3].strip())
firstline = "Lattice=\"50.0 0.0 0.0 0.0 50.0 0.0 0.0 0.0 50.0\" Properties=species:S:1:pos:R:3:forces:R:3 energy={} pbc=\"F F F\"\n".format(energy)
r.close()

w = open("ref.xyz", "w")
w.write("{}\n".format(num_atoms))
w.write(firstline)

#def read_gradient(i):
#    print(lines)
#    x = lines[11+3*i].strip()
#    y = lines[11+3*i+1].strip()
#    z = lines[11+3*i+2].strip()

#    gradient = [float(x)*C, float(y)*C, float(z)*C]
#    return " {} {} {}".format(gradient[0], gradient[1], gradient[2])

g = open("opt.engrad", "r")
gradlines = g.readlines()
g.close()

lines = open(xyzfile, "r")
for i, val in enumerate(lines.readlines()):
    if (i > 1):
        x = gradlines[11+3*(i-2)].strip()
        y = gradlines[11+3*(i-2)+1].strip()
        z = gradlines[11+3*(i-2)+2].strip()
        gradient = [float(x)*C, float(y)*C, float(z)*C]
        w.write(val.strip("\n") + str(" {} {} {}".format(gradient[0], gradient[1], gradient[2])) + "\n")
w.close()
