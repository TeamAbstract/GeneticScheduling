from schedule import *
from random import randint


class Generator:
    """!
    Class responsible for generating schedules
    """
    def __init__(self, productList):
        self.productList = productList

    #TODO more sophisticated generation algorithm
    def getNewSchedule(self):
        """quick algorithm for testing
        Randomly assigns products to the schedule, doesn't check for conflicts
        or add them in any optimal way, cleaning the vessels also need to be scheduled
        """
        schedule = Schedule(3)
        for product in self.productList:
            schedule.addTask(randint(0, 2), Task.fromProduct(product))
        return schedule
