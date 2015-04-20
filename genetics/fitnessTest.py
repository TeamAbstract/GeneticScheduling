from datetime import datetime as DateTime

from genetics.genepool import GenePool
from vessels import Vessels
from schedule import Schedule
import util
import settings


class FitnessTest:
	# Weighting  #TODO fine tune weighting
	bonusPerHourTillDeadline = 5
	penaltyPerHourOverDeadline = -10
	penaltyPerHourOverlapping = -5
	penaltyPerHourIdle = -2
	totalTimeWeight = -1
	penaltyForOutOfHours = -10
	percentageTimeUsedWeight = 5

	startTime = DateTime.now()

	@staticmethod
	def testPool(genepool):
		"""! tests every schedule in the genePool that is passed to it
		:param genepool: genepool containing the schedules to be tested
		:type genepool: GenePool
		"""
		assert isinstance(genepool, GenePool)
		# print("Testing ", len(genepool.schedules), " schedules")

		for schedule in genepool.schedules:
			FitnessTest.testSchedule(schedule)

	@staticmethod
	def testSchedule(schedule):
		# TODO more requirements
		"""
		Tests a single schedule for it's fitness
		:param schedule: schedule to be tested
		:type schedule: Schedule
		"""
		# print("Testing schedule ", schedule.id)

		fitness = 100

		schedule.flags = set()

		fitness += FitnessTest.timeToDeadline(schedule)
		fitness += FitnessTest.isOverDeadline(schedule)
		fitness += FitnessTest.isOverlapping(schedule)
		fitness += FitnessTest.checkIdleVessels(schedule)
		fitness += FitnessTest.testTotalTime(schedule)
		fitness += FitnessTest.testOutOfHours(schedule)
		fitness += FitnessTest.testPercentageUsed(schedule)

		# print("score of ", fitness)

		schedule.fitness = fitness

	@staticmethod
	def timeToDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue
			dTime = util.addDateTimeAndTime(task.getEndTime(), task.coolDown) - task.product.dueDate
			score += util.getTotalHours(dTime) * FitnessTest.bonusPerHourTillDeadline
		return score

	@staticmethod
	def isOverDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue

			dTime = util.addDateTimeAndTime(task.getEndTime(), task.coolDown) - task.product.dueDate
			partialScore = util.getTotalHours(dTime) * FitnessTest.penaltyPerHourOverDeadline
			if partialScore > 0:
				score += partialScore
		return score

	@staticmethod
	def isOverlapping(schedule):
		"""! Tests if tasks on a schedule are overlapping
		:param schedule: schedule to test
		:type schedule: Schedule
		:return: score
		"""
		score = 0

		for index, task in enumerate(schedule.tasks[:-1]):
			for otherTask in schedule.tasks[index:]:
				if task.getEndTime() <= otherTask.startTime:  # if no overlap
					continue

				schedule.flags.add("Olap")
				hoursOverlapping = otherTask.getEndTime() - task.startTime
				score += util.getTotalHours(hoursOverlapping) * FitnessTest.penaltyPerHourOverlapping
		return score

	@staticmethod
	def checkIdleVessels(schedule):
		score = 0
		for vessel in Vessels.vessels:
			timeCurrent = None
			for task in schedule.tasks:
				if task.vessel == vessel:
					if timeCurrent is None:
						timeCurrent = task.getEndTime() + task.cleanTime
					else:
						score += util.getTotalHours(task.startTime - timeCurrent) * FitnessTest.penaltyPerHourIdle
		return score

	@staticmethod
	def testTotalTime(schedule):
		"""! return total time that the schedule uses including brewtime and cleaning
		:param schedule: schedule to test
		:type schedule: Schedule
		:return: score from test
		"""

		assert isinstance(schedule, Schedule)

		return util.getTotalHours(schedule.getTotalTime()) * FitnessTest.totalTimeWeight

	@staticmethod
	def testPercentageUsed(schedule):
		"""! checks what percentage of each vessel's time is spent idle
		:param schedule: schedule to test
		:type schedule: Schedule
		:return: score from test
		"""

		lastTask = schedule.tasks[0]
		for task in schedule.tasks[1:]:
			if task.getEndTime() > lastTask.getEndTime():
				lastTask = task

		totalTime = util.getTotalHours(schedule.getTotalTime())/len(Vessels.vessels)
		timeToEnd = util.getTotalHours(lastTask.getEndTime() - FitnessTest.startTime)
		return (timeToEnd/totalTime) * FitnessTest.percentageTimeUsedWeight

	@staticmethod
	def testOutOfHours(schedule):
		"""! Check if the schedule has anything finishing out of hours
		:param schedule: schedule to test
		:type schedule: Schedule
		:return: score from test
		"""
		assert isinstance(schedule, Schedule)

		score = 0

		for task in schedule.tasks:
			if not settings.openingTime < task.startTime.time() < settings.closingTime:
				score += FitnessTest.penaltyForOutOfHours
				schedule.flags.add("outHs")  # out of hours start
			if not settings.openingTime < task.getEndTime().time() < settings.closingTime:
				score += FitnessTest.penaltyForOutOfHours
				schedule.flags.add("outHe")  # out of hours end
		return score
