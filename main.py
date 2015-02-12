from generator import Generator
from genepool import GenePool
from productList import ProductList
from product import Product
from fitnessTest import FitnessTest
from vessels import Vessels

from datetime import *

startTime = datetime.now()

vessels = Vessels()
vessels.addVessel(20)
vessels.addVessel(30)
vessels.addVessel(50)


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
    #GenePool.removeSchedules(10, 60, 60)

genepool.printPool()

print("Ran in ", (datetime.now() - startTime).microseconds/1000000, " seconds")
