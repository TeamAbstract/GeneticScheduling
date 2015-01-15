from generator import Generator
from genepool import GenePool
from productList import ProductList
from product import Product
from fitnessTest import FitnessTest
from vessels import Vessels


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


for _count in range(20):  # temp loop to run algorithm
    genepool.refreshSchedules()
    FitnessTest.testPool(genepool)
    genepool.removeSchedules()

genepool.printPool()
