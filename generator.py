from schedule import *
from random import randint


class Generator:
    """!
    Class responsible for generating schedules
    """
    def __init__(self, productList):
        """
        :param productList:
        """

        self.productList = productList

    def getNewSchedule(self):
        """quick algorithm for testing"""
        schedule = Schedule(3)
        for product in self.productList:
            schedule.addTask(randint(0, 2), Task.fromProduct(product))
        return schedule
