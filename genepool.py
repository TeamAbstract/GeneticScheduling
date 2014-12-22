from schedule import Schedule


class GenePool:
    """!
    class to store generated schedules
    """
    def __init__(self):
        self.schedules = []

    def addSchedule(self, schedule):
        if isinstance(schedule, Schedule):
            self.schedules.append(schedule)

    def printPool(self):
        for schedule in self.schedules:
            schedule.printSchedule()

    def getIterable(self):
        return iter(self.schedules)
