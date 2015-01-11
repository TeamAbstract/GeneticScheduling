import sys

from generator import Generator
from genepool import GenePool
from productList import ProductList
from product import Product
from fitnessTest import FitnessTest

if sys.version_info < (3, 0):
    raise EnvironmentError("Outdated version update to V3")

# temporary will later be called from the GUI
productList = ProductList()
productList.addProduct(Product("Stuff", "1"))
productList.addProduct(Product("Other", "2"))
productList.addProduct(Product("Brew", "4"))
productList.addProduct(Product("beer", "4"))

generator = Generator(productList.products)

genepool = GenePool()
genepool.addSchedule(generator.getNewSchedule())

for i in range(20):  # temp loop to run algorithm
    genepool.refreshSchedules()
    FitnessTest.testPool(genepool)
    genepool.removeSchedules()

genepool.printPool()
