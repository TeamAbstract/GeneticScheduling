from product import Product


masterProductList = [
	Product("Porter", "1", 10),
	Product("Mild", "2", 30),
	Product("Kölsch", "4", 15),
	Product("Pilsener", "4", 60),
	Product("Lager", "3", 40),
	Product("Bitter", "4", 45),
	Product("Stout", "5", 20),
	Product("Brown Ale", "2", 25),
	Product("Blonde Ale", "1", 35),
	Product("Golden Ale", "2", 15),
	Product("Red Ale", "2", 37),
	Product("Light Ale", "3", 50)]


def getByName(search):
	assert isinstance(search, str), "search term is type" + str(type(search)) + str(search)
	for item in masterProductList:
		if item.name == search:
			return item
	raise RuntimeError("Product name, " + search + " not found (productList.getByName)")
