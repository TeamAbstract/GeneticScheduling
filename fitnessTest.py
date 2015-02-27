from random import randrange

from genepool import GenePool
from vessels import Vessels

from datetime import datetime

import util


class FitnessTest:
	# Weighting  #TODO setup weighting
	bonusPerHourTillDeadline = 5
	penaltyPerHourOverDeadline = 10
	penaltyPerHourOverlapping = 10
	penaltyPerHourIdle = 2
	totalTimeWeight = -1

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
		# TODO maybe add more requirements
		"""
		Tests a single schedule for it's fitness
		:param schedule: schedule to be tested
		"""
		# print("Testing schedule ", schedule.id)

		fitness = 0.0

		# TODO non random number
		# currently just added for testing

		# fitness = randrange(-100, 100)  # actual test may produce numbers outside this range

		fitness += FitnessTest.timeToDeadline(schedule)
		fitness += FitnessTest.isOverDeadline(schedule)
		fitness += FitnessTest.isOverlapping(schedule)
		fitness += FitnessTest.checkIdleVessels(schedule)
		fitness += util.getTotalHours(FitnessTest.getTotalTime(schedule)) * FitnessTest.totalTimeWeight

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
		for index1, task in enumerate(schedule.tasks):
			for nextTask in schedule.tasks[index1+1:]:
				hoursOverlapping = task.startTime - datetime.combine(task.getEndTime(), task.cleanTime)
				if task.getVessel == nextTask.getVessel and hoursOverlapping > 0:
					score += hoursOverlapping * FitnessTest.penaltyPerHourOverlapping
		return score

	@staticmethod
	def checkIdleVessels(schedule):
		score = 0
		for vessel in Vessels.vessels:
			timeCurrent = None
			for task in schedule.tasks:
				if task.getVessel() == vessel:
					if timeCurrent is None:
						timeCurrent = task.getEndTime() + task.Cooldown
					else:
						score += (task.getStartTime() - timeCurrent).getTotalHours() * FitnessTest.penaltyPerHourIdle
		return score

	@staticmethod
	def getTotalTime(schedule):
		time = util.getDateTimeObject()
		for Vessel in Vessels.vessels:
			for task in schedule.tasks:
				time = time.combine(time, util.addTimes(task.product.brewTime, task.cleanTime))
		return time
