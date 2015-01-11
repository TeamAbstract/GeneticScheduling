from schedule.task import Task
from schedule.vessel import Vessel


class Schedule:
    """!
    Class that is used to interface with a generated schedule
    """

    id = 0  # static variable for giving each vessel a new id

    def __init__(self, numOfVessels):
        self.vessels = []
        self.fitness = 0.0

        for x in range(numOfVessels):
            self.vessels.append(Vessel(x))
        self.id = Schedule.id
        Schedule.id += 1

    def getVesselCount(self):
        """Returns the number of vessels currently defined"""
        return len(self.vessels)

    def printSchedule(self):
        print("Schedule:", self.id)
        for vessel in self.vessels:
            print("Vessel: ", vessel.number)
            vessel.printVessel()

    def addTask(self, vesselID, task):
        assert vesselID < self.getVesselCount()
        assert vesselID >= 0
        assert isinstance(task, Task)
        # print("Adding ", task.name, " to vessel ", vesselID)
        if isinstance(task, Task):
            self.vessels[vesselID].addTask(task)
