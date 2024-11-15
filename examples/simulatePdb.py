import time
from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout

print("Hello!")
print("OpenMM version: ", Platform.getOpenMMVersion())
start_time = time.time()
pdb = PDBFile('input.pdb')
forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME, nonbondedCutoff=1*nanometer, constraints=HBonds)
integrator = LangevinMiddleIntegrator(300*kelvin, 1/picosecond, 0.004*picoseconds)
simulation = Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)
minimize_start = time.time()
simulation.minimizeEnergy()
minimize_end = time.time()
simulation.reporters.append(PDBReporter('output.pdb', 1000))
simulation.reporters.append(StateDataReporter(stdout, 1000, step=True, potentialEnergy=True, temperature=True))
simulate_start = time.time()
simulation.step(2000)
simulate_end = time.time()
end_time = time.time()


print(f"Energy minimization took {minimize_end - minimize_start:.2f} seconds")
print(f"Simulation steps took {simulate_end - simulate_start:.2f} seconds")
print(f"Total time for the script: {end_time - start_time:.2f} seconds")
