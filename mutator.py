from copy import deepcopy
from random import randint
from datetime import datetime

import util

import schedule
from schedule.schedule import Schedule
from schedule.task import Task
from vessels import Vessels


class Mutator:
	"""!
	class responsible for mutating the schedule and creating the next generation
	"""

	# static variables for settings
	percentageChange = 100  # chance of a variable being changed(0-100)

	@staticmethod
	def mutateSchedule(schedule):
		"""! randomly modifies a schedule and returns the changed version
			:rtype : object
			:param schedule: schedule to be mutated
			:return: modified schedule
			"""
		assert isinstance(schedule, Schedule)
		newSchedule = deepcopy(schedule)
		newSchedule.id = Schedule.getNextID()
		assert isinstance(newSchedule, Schedule)

		for index, task in enumerate(newSchedule.getTask()):
			if randint(0, 100) >= Mutator.percentageChange:
				continue
			Mutator.mutateTask(newSchedule.getTask(index))

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
		for index, vessel in enumerate(task.vessels):
			if randint(0, 100) <= Mutator.percentageChange:
				task.vessels[index] = randint(0, Vessels.getVesselNum())
				print("changed ", task.product.name, "vessel to", vessel)

			if randint(0, 100) <= Mutator.percentageChange:
				hoursAdded = str(randint(-12, 12))
				task.startTime = datetime.combine(task.startTime, util.getTimeObject(hoursAdded))
				print("Added ", hoursAdded, " hours to task", task.product.name)
