from random import randrange
import genepool




class FitnessTest:
    @staticmethod
    def testPool(genePool):
        """! tests every schedule in the genePool that is passed to it
        :param genePool: genepool containing the schedules to be tested
        """
        assert isinstance(genePool, genepool.GenePool)
        for schedule in genePool.getSchedules():
            testSchedule(schedule)


def testSchedule(schedule):
    # TODO add more requirements
    # TODO fitness test function
    """
    Tests a single schedule for it's fitness
    :param schedule: schedule to be tested

    Schedule Requirements:
    No conflicts
    Minimal cleaning time(same products in each vessel)
    Products completed before due date
    Nothing starts/finishes after hours
    """
    # print("Testing schedule ", schedule.id)

    fitness = 0.0

    # TODO non random number
    # currently just added for testing

    fitness = randrange(-100, 100)  # actual test may produce numbers outside this range

    schedule.fitness = fitness

    return fitness
    
    def TimeToDeadline(schedule):
        score = 0
        for x in (0, schedule.getTaskCount()):
            task = schedule.getTask(x)
            score += (task.getEndTime() + task.Cooldown - task.getDeadline()).getTotalHours() * schedule.bonusPerHourTillDeadline
        return score

    def IsOverDeadline(schedule):
        score = 0
        for x in (0, schedule.getTaskCount()):
            task = schedule.getTask(x)
            partialScore = (task.getEndTime() + task.Cooldown - task.getDeadline()).getTotalHours() * schedule.penaltyPerHourOverDeadline
            if partialScore > 0:
                score += partialScore
        return score

    def IsOverlapping(schedule):
        score = 0
        for x in (0, schedule.getTaskCount() - 1):
            for y in (x + 1, schedule.getTaskCount()):
                taskX = schedule.getTask(x)
                taskY = schedule.getTask(y)
                hoursOverlapping = taskX.getStartTime - (taskX.getEndTime + taskX.Cooldown)
                if taskX.getVessele == taskY.getVessele and hoursOverlapping > 0:
                    score += hoursOverlapping * schedule.penaltyPerHourOverlapping
        return score

    def CheckIdleVessels(schedule):
        score = 0
        for vessel in Vessels.vessels:
            timeCurrent = None
            for i in (0, schedule.getTaskCount() - 1):
                task = schedule.getTask(i)
                if task.getVessel() == vessel:
                    if timeCurrent == None:
                        timeCurrent = task.getEndTime() + task.Cooldown
                    else:
                        score += (task.getStartTime() - timeCurrent).getTotalHours() * schedule.penaltyPerHourIdle
        return score





