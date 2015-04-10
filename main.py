from datetime import *

import genetics
from vessels import Vessels
from gui.mainWindow import startGUI


vessels = Vessels()
vessels.addVessel(20)
vessels.addVessel(30)
vessels.addVessel(50)

startGUI()

startTime = datetime.now()


# genepool.addSchedule(genetics.getNewSchedule())
#
# for _count in range(200):  # temp loop to run algorithm
# 	genepool.refreshSchedules()
# 	genetics.FitnessTest.testPool(genepool)
# 	print("Best result", genepool.getBestSchedule().fitness)
# 	genepool.removeSchedules()

# genepool.printPool()

# print("Best Schedule")
# genepool.getBestSchedule().print()
#
# print("Ran in ", round((datetime.now() - startTime).total_seconds(), 2), " seconds")
