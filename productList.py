from schedule import Task


class ProductList:
    """!
    General storage for products that need to be added to a schedule
    """

    def __init__(self):
        self.products = []

    def addProduct(self, task):
        if isinstance(task, Task):
            self.products.append(task1)