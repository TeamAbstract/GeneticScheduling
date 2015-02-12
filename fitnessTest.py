from random import randrange

import genepool
from vessels import Vessels

from datetime import datetime

import util

class FitnessTest:
	@staticmethod
	def testPool(genePool):
		"""! tests every schedule in the genePool that is passed to it
		:param genePool: genepool containing the schedules to be tested
		"""
		assert isinstance(genePool, genepool.GenePool)
		for schedule in genePool.getSchedules():
			FitnessTest.testSchedule(schedule)

	@staticmethod
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
		print("Testing schedule ", schedule.id)

		fitness = 0.0

		# TODO non random number
		# currently just added for testing

		fitness = randrange(-100, 100)  # actual test may produce numbers outside this range

		fitness += FitnessTest.timeToDeadline(schedule)
		fitness += FitnessTest.isOverDeadline(schedule)
		fitness += FitnessTest.isOverlapping(schedule)
		fitness += FitnessTest.checkIdleVessels(schedule)

		schedule.fitness = fitness

	@staticmethod
	def timeToDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue
			dTime = datetime.combine(task.getEndTime(), task.coolDown) - task.product.dueDate
			score += util.getTotalHours(dTime) * schedule.bonusPerHourTillDeadline
		return score

	@staticmethod
	def isOverDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			if task.product.dueDate is None:
				continue

			dTime = datetime.combine(task.getEndTime(), task.coolDown) - task.product.dueDate
			partialScore = util.getTotalHours(dTime) * schedule.penaltyPerHourOverDeadline
			if partialScore > 0:
				score += partialScore
		return score

	@staticmethod
	def isOverlapping(schedule):
		score = 0
		for x in range(len(schedule.tasks)):
			for y in (x + 1, len(schedule.tasks)):
				taskX = schedule.getTask(x)
				taskY = schedule.getTask(y)
				hoursOverlapping = taskX.startTime - datetime.combine(taskX.getEndTime(), taskX.coolDown)
				if taskX.getVessel == taskY.getVessel and hoursOverlapping > 0:
					score += hoursOverlapping * schedule.penaltyPerHourOverlapping
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
						score += (task.getStartTime() - timeCurrent).getTotalHours() * schedule.penaltyPerHourIdle
		return score





