from schedule import Schedule


class GenePool:
    """!
    class to store generated schedules
    """

    # TODO culling of worst schedules
    # TODO Generation of new schedules to fill the pool
    # TODO test the best size to use

    def __init__(self):
        self.schedules = []
        self.size = 100  # test default size

    def addSchedule(self, schedule):
        assert isinstance(schedule, Schedule)
        self.schedules.append(schedule)

    def printPool(self):
        for schedule in self.schedules:
            schedule.printSchedule()

    def getSchedules(self):
        return self.schedules
