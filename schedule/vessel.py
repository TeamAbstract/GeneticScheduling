class Vessel:
    """!
    Class that stores the information and schedule on a per vessel basis
    """

    def __init__(self, number):
        self.number = number
        self.tasks = []

    def addTask(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    def printVessel(self):
        for task in self.tasks:
            task.printTask()
