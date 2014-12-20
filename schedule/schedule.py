from schedule.task import Task


class Schedule:
    """!
    Class that is used to interface with a generated schedule
    """

    vessels = []
    rating = 0.0
    id = 0

    def __init__(self, numOfVessels):
        self.vessels = [Vessel() for x in range(numOfVessels)]
        self.id = Schedule.id
        Schedule.id += 1

    def getVesselCount(self):
        """Returns the number of vessels currently defined"""
        return len(self.vessels)

    def printSchedule(self):
        print("Schedule:", self.id)
        for vessel in self.vessels:
            vessel.printVessel()

    def addTask(self, vesselID, task):
        assert vesselID < self.getVesselCount()
        assert vesselID >= 0
        assert isinstance(task, Task)
        if isinstance(task, Task):
            self.vessels[vesselID].addTask(task)


class Vessel:
    """ !
    Class that stores the information and schedule on a per vessel basis
    """

    tasks = []

    def addTask(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    def printVessel(self):
        for task in self.tasks:
            task.printTask()

