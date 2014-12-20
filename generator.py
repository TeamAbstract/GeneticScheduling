from schedule import *


class Generator:
    """!
    Class responsible for generating schedules
    """

    @staticmethod
    def getNewSchedule():
        """quick algorithm for testing"""
        schedule = Schedule(3)
        schedule.addTask(0, Task())
        return schedule
