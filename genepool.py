from schedule import Schedule
from mutator import Mutator


class GenePool:
	testlist = []
	"""!
	class to store generated schedules
	"""

	# settings variables
	minNumOfSchedules = 50
	maxNumOfSchedules = 100

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

	def printPool(self, printDetails=True):
		for schedule in self.schedules:
			schedule.print(printDetails)

	def getSchedules(self):
		return self.schedules

	def removeSchedules(self):  # removes the lowest fitness from the list of fitnesses
		"""!cull schedules to keep them to a minimum"""
		self.schedules.sort(key=lambda schedule: schedule.fitness, reverse=True)  # sorts schedules
		self.schedules = self.schedules[:50 - 1]  # should leave 50 best schedules

	def refreshSchedules(self):
		"""!add schedules to get the genepool to a maximum"""

		print("Refreshing pool contains ", len(self.schedules), "/", GenePool.maxNumOfSchedules)

		# get new schedules from the Mutator.mutateSchedule function(WIP)
		while len(self.schedules) < GenePool.maxNumOfSchedules:
			self.schedules.append(Mutator.mutateSchedule(self.schedules[0]))  # this should mutate the schedule and add it to the end of a list

	def getBestSchedule(self):
		"""Return highest rated schedule
		:return: highest rated schedule
		"""
		self.schedules.sort(key=lambda schedule: schedule.fitness, reverse=True)
		return self.schedules[0]
