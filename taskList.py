from schedule import Task


class TaskList:
    """!
    General storage for tasks that need to be added to a schedule
    """

    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        if isinstance(task, Task):
            self.tasks.append(task1)