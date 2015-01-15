from random import randrange
from genepool import GenePool


class FitnessTest:
	@staticmethod
	def testPool(genePool):
		"""! tests every schedule in the genePool that is passed to it
		:param genePool: genepool containing the schedules to be tested
		"""
		assert isinstance(genePool, GenePool)
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
		# print("Testing schedule ", schedule.id)

		fitness = 0.0

		# TODO non random number
		# currently just added for testing

		fitness = randrange(-100, 100)  # actual test may produce numbers outside this range

		schedule.fitness = fitness
