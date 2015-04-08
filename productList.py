from product import Product


masterProductList = [
	Product("Booze", "1", 10),
	Product("Hooch", "2", 30),
	Product("Brew", "4", 15),
	Product("Beer", "4", 60)]


def getByName(name):
	for item in masterProductList:
		if item.name == name:
			return item
