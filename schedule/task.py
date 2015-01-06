from datetime import time as Time  # done to fit in with caps = class
from datetime import datetime as DateTime
import datetime
import util
from product import Product


class Task:
    """!
    Class that represents a single scheduled task
    """

    def __init__(self, name="NoName", time="2014:1:1", duration="1"):
        self.name = name

        if isinstance(time, DateTime):
            self.startTime = time
        elif isinstance(time, str):
            self.startTime = util.getDateTimeObject(time)
        else:
            raise TypeError("Task requires a datetime.datetime or str parameter not ", type(time))

        if isinstance(duration, Time):
            self.duration = duration
        elif isinstance(duration, str):
            self.duration = util.getTimeObject(duration)
        else:
            raise TypeError("Task requires a datetime.time or str parameter not ", type(time))

    @classmethod
    def fromProduct(cls, product, startTime):
        """
        Create a task from a product object
        :param product: product to create the object from
        :param startTime: start time of the task
        :return:
        """
        assert isinstance(product, Product)
        return cls(product.name, startTime, product.brewTime)

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

    def setDuration(self, duration):
        """
        :param duration: datetime object or a string
        :return: None
        """
        if isinstance(duration, datetime.time):
            self.duration = duration
        elif isinstance(duration, str):
            self.duration = datetime.time(duration)
        else:
            raise TypeError("setDuration requires a datetime.time object or a string not", type(duration))

    def getEndTime(self):
        """
        Adds the duration to the time to get the finish time
        :return: datetime.time for when the task finishes
        """
        util.addDateAndTime(self.startTime, self.duration)

    def printTask(self):
        print(self.name.rjust(8, " "), ":", self.startTime, " ", self.duration)

