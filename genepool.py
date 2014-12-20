from schedule import Schedule


class Genepool:
    """!
    class to store generated schedules
    """

    schedules = []

    def addSchedule(self, schedule):
        if isinstance(schedule, Schedule):
            self.schedules.append(schedule)

    def printPool(self):
        for schedule in self.schedules:
            schedule.printSchedule()
