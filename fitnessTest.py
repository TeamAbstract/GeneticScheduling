from random import randrange

from genepool import GenePool
from vessels import Vessels
from schedule import Schedule

from datetime import datetime

import util
import settings


class FitnessTest:
	# Weighting  #TODO setup weighting
	bonusPerHourTillDeadline = 5
	penaltyPerHourOverDeadline = -10
	penaltyPerHourOverlapping = -10
	penaltyPerHourIdle = -2
	totalTimeWeight = -1
	penaltyForOutOfHours = -20

	@staticmethod
	def testPool(genepool):
		"""! tests every schedule in the genePool that is passed to it
		:param genepool: genepool containing the schedules to be tested
		"""
		assert isinstance(genepool, GenePool)
		print("Testing ", len(genepool.schedules), " schedules")
		for schedule in genepool.getSchedules():
			FitnessTest.testSchedule(schedule)

	@staticmethod
	def testSchedule(schedule):
		# TODO more requirements
		"""
		Tests a single schedule for it's fitness
		:param schedule: schedule to be tested
		"""
		# print("Testing schedule ", schedule.id)

		fitness = 0.0

		schedule.flags = set()

		fitness += FitnessTest.timeToDeadline(schedule)
		fitness += FitnessTest.isOverDeadline(schedule)
		fitness += FitnessTest.isOverlapping(schedule)
		fitness += FitnessTest.checkIdleVessels(schedule)
		fitness += FitnessTest.testTotalTime(schedule)
		fitness += FitnessTest.testOutOfHours(schedule)

		# print("score of ", fitness)

		schedule.fitness = fitness

	@staticmethod
	def timeToDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue
			dTime = datetime.combine(task.getEndTime(), task.coolDown) - task.product.dueDate
			score += util.getTotalHours(dTime) * FitnessTest.bonusPerHourTillDeadline
		return score

	@staticmethod
	def isOverDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue

			dTime = datetime.combine(task.getEndTime(), task.coolDown) - task.product.dueDate
			partialScore = util.getTotalHours(dTime) * FitnessTest.penaltyPerHourOverDeadline
			if partialScore > 0:
				score += partialScore
		return score

	@staticmethod
	def isOverlapping(schedule):
		score = 0
		taskList = schedule.tasks
		taskList.sort(key=lambda task: task.startTime)

		for index, task in enumerate(taskList[:-1]):
			nextTask = taskList[index+1]
			if task.getEndTime() < nextTask.startTime:  # if no overlap
				continue
			schedule.flags.add("Olap")
			hoursOverlapping = nextTask.getEndTime() - task.startTime
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
						timeCurrent = datetime.combine(task.getEndTime(), task.cleanTime)
					else:
						score += util.getTotalHours(task.startTime - timeCurrent) * FitnessTest.penaltyPerHourIdle
		return score

	@staticmethod
	def testTotalTime(schedule):
		"""! return total time that the schedule uses including brewtime and cleaning
		:param schedule: schedule to test
		:return: score from test
		"""

		assert isinstance(schedule, Schedule)

		totalTime = util.getDateTimeObject()
		for task in schedule.tasks:
			taskTime = util.addTimes(task.product.brewTime, task.cleanTime)
			totalTime = totalTime.combine(totalTime, taskTime)
		return util.getTotalHours(totalTime) * FitnessTest.totalTimeWeight

	@staticmethod
	def testOutOfHours(schedule):
		"""! Check if the schedule has anything finishing out of hours
		:param schedule: schedule to test
		:return: score from test
		"""
		assert isinstance(schedule, Schedule)

		score = 0

		for task in schedule.tasks:
			if task.startTime.time < settings.openingTime:
				score += FitnessTest.penaltyForOutOfHours
			if task.getEndTime() > settings.closingTime:
				score += FitnessTest.penaltyForOutOfHours
		return score