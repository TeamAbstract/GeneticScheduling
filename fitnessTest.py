from random import randrange

import genepool
from vessels import Vessels


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
			score += (task.getEndTime() + task.cooldown - task.getDeadline()).getTotalHours() * schedule.bonusPerHourTillDeadline
		return score

	@staticmethod
	def isOverDeadline(schedule):
		score = 0
		for task in schedule.tasks:
			partialScore = (task.getEndTime() + task.cooldown - task.getDeadline()).getTotalHours() * schedule.penaltyPerHourOverDeadline
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
				hoursOverlapping = taskX.getStartTime - (taskX.getEndTime + taskX.Cooldown)
				if taskX.getVessele == taskY.getVessele and hoursOverlapping > 0:
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





