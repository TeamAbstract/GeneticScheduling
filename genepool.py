from schedule import Schedule
from mutator import Mutator
from fitnessTest import FitnessTest


class GenePool:
	testlist = []
	"""!
	class to store generated schedules
	"""

	# """
	# class should maintain the list of schedules
	# fill out the list of schedules to be the max and then after the fitness test has run, remove the worst to be equal with the minimum number
	# """

	# settings variables
	minNumOfSchedules = 50
	maxNumOfSchedules = 100

	# TODO culling of worst schedules
	# TODO Generation of new schedules to fill the pool
	# TODO test the best size to use



	def __init__(self):
		self.schedules = []
		self.size = 100  # test default size


	def addSchedule(self, schedule):
		"""! Adds a single schedule to the list
		:param schedule: schedule to add
		"""
		assert isinstance(schedule, Schedule)

	self.schedules.append(schedule)


	def printPool(self):
		for schedule in self.schedules:
			schedule.printSchedule()


	def getSchedules(self):
		return self.schedules


	def removeSchedules(self, scheduleFitness, numberOfSchedules):  # removes the lowest fitness from the list of fitnesses
		"""!cull schedules to keep them to a minimum"""
		self.testlist.append(scheduleFitness)
		while numberOfSchedules > 50:
			testlist.remove(min.testlist)  #this bit is not working yet


	def refreshSchedules(self):
		"""!add schedules to get the genepool to a maximum"""

		# get new schedules from the Mutator.mutateSchedule function(WIP
		for i in range(0, 10):
			self.schedules.append(Mutator.mutateSchedule(
				self.schedules[i]))  # this should mutate the schedule and add it to the end of a list