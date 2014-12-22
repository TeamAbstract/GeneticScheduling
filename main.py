import sys

from generator import Generator
from genepool import GenePool
from productList import ProductList
from product import Product

if sys.version_info < (3, 0):
    raise EnvironmentError("Outdated version update to V3")

productList = ProductList()
productList.addProduct(Product("Stuff", "1"))
productList.addProduct(Product("Other", "2"))
productList.addProduct(Product("Brew", "4"))
productList.addProduct(Product("beer", "4"))

generator = Generator(productList.products)

genepool = GenePool()
genepool.addSchedule(generator.getNewSchedule())
genepool.printPool()