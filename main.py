from datetime import *

from genetics.generator import Generator
from genetics.genepool import GenePool
from genetics.fitnessTest import FitnessTest
from vessels import Vessels
from gui.GUI import startGUI


vessels = Vessels()
vessels.addVessel(20)
vessels.addVessel(30)
vessels.addVessel(50)

startGUI()

startTime = datetime.now()

generator = Generator()

genepool = GenePool()
genepool.addSchedule(generator.getNewSchedule())

for _count in range(200):  # temp loop to run algorithm
	genepool.refreshSchedules()
	FitnessTest.testPool(genepool)
	print("Best result", genepool.getBestSchedule().fitness)
	genepool.removeSchedules()

# genepool.printPool()

print("Best Schedule")
genepool.getBestSchedule().print()

print("Ran in ", round((datetime.now() - startTime).total_seconds(), 2), " seconds")
