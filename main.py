from datetime import *

from generator import Generator
from genepool import GenePool
from productList import ProductList
from product import Product
from fitnessTest import FitnessTest
from vessels import Vessels
from logger import *

from GUIfirstpass import startGUI


startTime = datetime.now()

vessels = Vessels()
vessels.addVessel(20)
vessels.addVessel(30)
vessels.addVessel(50)

# saveHigh('\nlots of issu94des')
# saveHigh('\nlots of other iss7ues')
# saveHigh('\nlots of other iss6ues')
# saveHigh('\nlots of other iss5ues')
# saveHigh('\nlots of other iss1ues')
# saveHigh('\nlots of other issu2es')
# saveHigh('\nlots of other issu3es')
# saveHigh('\nlots of other issu4es')

# startGUI()

# temporary will later be called from the GUI
productList = ProductList()
productList.addProduct(Product("Booze", "1", 10))
productList.addProduct(Product("Hooch", "2", 30))
productList.addProduct(Product("Brew", "4", 15))
productList.addProduct(Product("Beer", "4", 60))

generator = Generator(productList.products)

genepool = GenePool()
genepool.addSchedule(generator.getNewSchedule())

for _count in range(10):  # temp loop to run algorithm
	genepool.refreshSchedules()
	FitnessTest.testPool(genepool)
	print("Best result", genepool.getBestSchedule().fitness)
	genepool.removeSchedules()

genepool.printPool()

print("Best Schedule")
genepool.getBestSchedule().print()

print("Ran in ", round((datetime.now() - startTime).total_seconds(), 2), " seconds")
