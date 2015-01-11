from datetime import datetime as DateTime  # done to fit in with caps = class
import datetime
import util
from product import Product


class Task:
    """!
    Class that represents a single scheduled task
    """

    def __init__(self, product, startTime="2014:1:1"):
        assert isinstance(product, Product), type(product)
        self.product = product
        self.vessels = []  # list of vessels that the task will use

        if isinstance(startTime, DateTime):
            self.startTime = startTime
        elif isinstance(startTime, str):
            self.startTime = util.getDateTimeObject(startTime)
        else:
            raise TypeError("Task requires a datetime.datetime or str parameter not ", type(startTime))

    def setDate(self, date):
        """
        :param date: datetime date object or a string
        :return: None
        """
        if isinstance(date, datetime.date):
            self.startTime = date
        elif isinstance(date, str):
            self.startTime = datetime.date(date)
        else:
            raise TypeError("setDate requires a datetime.datetime object or a string not", type(date))

    def getEndTime(self):
        """
        Adds the duration to the time to get the finish time
        :return: datetime.time for when the task finishes
        """
        util.addDateAndTime(self.startTime, self.duration)

    def printTask(self):
        print("  ", self.startTime, " ", self.product.brewTime)
        print("   in vessels", str(self.vessels).strip("[]"))

