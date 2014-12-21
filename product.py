from datetime import time as Time
import util.timeUtil


class Product:
    """!
    unscheduled product that needs to be scheduled
    """

    def __init__(self, name, brewTime, dueDate=None):
        self.name = name
        self.dueDate = dueDate

        if isinstance(brewTime, Time):
            self.brewTime = brewTime
        elif isinstance(brewTime, str):
            self.brewTime = util.timeUtil.getTimeObject(brewTime)
        else:
            raise TypeError("Product parameter brewTime requires str or Time object not", type(brewTime))
