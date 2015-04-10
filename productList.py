from product import Product


masterProductList = [
	Product("Booze", "1", 10),
	Product("Hooch", "2", 30),
	Product("Brew", "4", 15),
	Product("Beer", "4", 60)]


def getByName(search):
	assert isinstance(search, str), "search term is type" + str(type(search)) + str(search)
	for item in masterProductList:
		if item.name == search:
			return item
	raise RuntimeError("Product name, " + search + " not found (productList.getByName)")
