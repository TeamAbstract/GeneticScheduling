

class Product:
    """!
    unscheduled product that needs to be scheduled
    """

    def __init__(self, name="Generic Booze", dueDate=None):
        self.name = name
        self.dueDate = dueDate