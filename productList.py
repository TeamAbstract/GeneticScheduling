from product import Product


class ProductList:
    """!
    General storage for products that need to be added to a schedule may be removed once GUI is added
    """

    def __init__(self):
        self.products = []

    def addProduct(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            print("Add product requires a product")
