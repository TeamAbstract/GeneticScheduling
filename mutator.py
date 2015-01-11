import schedule

from schedule.schedule import Schedule
from schedule.task import Task

from vessels import Vessels

from copy import deepcopy
from random import randint


class Mutator:
    """!
    class responsible for mutating the schedule and creating the next generation
    """

    # static variables for settings
    percentageChange = 10  # chance of a variable being changed(0-100)

    @staticmethod
    def mutateSchedule(schedule):
        """! randomly modifies a schedule and returns the changed version
        :param schedule: schedule to be mutated
        :return: modified schedule
        """
        assert isinstance(schedule, Schedule)
        newSchedule = deepcopy(schedule)
        assert isinstance(newSchedule, Schedule)
        for task in newSchedule.getTask():
            if randint(0, 100) <= Mutator.percentageChange:
                continue
            Mutator.mutateTask(task)
        return newSchedule

    @staticmethod
    def mutateTask(task):
        """! mutates a single task

        Currently a purely random mutate, more efficient ones can be implemented in the future

        :param task: task to be mutated
        """

        # TODO more efficient mutate i.e. not mostly random
        # TODO add order splitting i.e. one task over two vessels

        assert isinstance(task, Task)
        for vessel in task.vessels:
            if randint(0, 100) <= Mutator.percentageChange:
                continue
            vessel = randint(0, Vessels.getVesselNum())
            print("changed ", task.product.name, "vessel to", vessel)



    @staticmethod
    def combineSchedules(schedule1, schedule2):
        """! Create a new schedule that is a combination of the two schedules
        :param schedule1:
        :param schedule2:
        :return: new schedule
        """
        assert isinstance(schedule1, schedule.Schedule)
        assert isinstance(schedule2, schedule.Schedule)

        # TODO implement
        # temporary just returns the first schedule

        """
        I'm wondering if this is necessary, it would be hard to implement without losing data, whereas mutating one schedule(see above)would be easier with no problems of data loss

        """
        return schedule1
