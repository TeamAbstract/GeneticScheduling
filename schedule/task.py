from datetime import time as Time  # done to fit in with caps = class
from util.timeUtil import TimeUtil
from product import Product


class Task:
    """!
    Class that represents a single scheduled task
    """
    name = ""
    time = None  # time that the product production should start
    duration = None  # time that the product production will take

    def __init__(self, time="1", name="NoName", duration="1"):
        self.name = name

        if isinstance(time, Time):
            self.time = time
        elif isinstance(time, str):
            self.time = TimeUtil.getTimeObject(time)

        if isinstance(duration, Time):
            self.duration = duration
        elif isinstance(duration, str):
            self.duration = TimeUtil.getTimeObject(duration)

    @classmethod
    def fromProduct(cls, product):
        assert isinstance(product, Product)
        return cls()

    def setDate(self, time):
        """
        :param time: datetime date object or a string
        :return: None
        """
        if isinstance(time, datetime.datetime):
            self.time = time
        elif isinstance(time, str):
            self.time = datetime.date(time)
        else:
            raise TypeError("setDate requires a datetime.datetime object or a string")

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
            raise TypeError("setDuration requires a datetime.time object or a string")

    def printTask(self):
        print(self.name, ":", self.time, " ", self.duration)

