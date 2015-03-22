from copy import deepcopy
from random import randint
from datetime import datetime

import util

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
			:param schedule: schedule to be mutated
			:type schedule: Schedule
			:return: modified schedule
			"""
		assert isinstance(schedule, Schedule)
		newSchedule = deepcopy(schedule)
		newSchedule.id = Schedule.getNextID()
		assert isinstance(newSchedule, Schedule)

		for index, task in enumerate(newSchedule.tasks):
			if randint(0, 100) >= Mutator.percentageChange:
				continue
			Mutator.mutateTask(newSchedule.getTask(index))

		return newSchedule

	@staticmethod
	def mutateTask(task):
		"""! mutates a single task
		Currently a purely random mutate, more efficient ones can be implemented in the future
		:param task: task to be mutated
		:type task: Task
		"""

		# TODO more efficient mutate i.e. not mostly random
		# TODO add order splitting i.e. one task over two vessels

		assert isinstance(task, Task)

		# change vessel
		if randint(0, 100) <= Mutator.percentageChange:
			task.vessel = Vessels.getRandomVessel(task.volume)
			# print("changed ", task.product.name, "vessel to", vessel)

		# change start time
		if randint(0, 100) <= Mutator.percentageChange:
			hoursAdded = str(randint(-12, 12))
			task.startTime = util.addDateTimeAndTime(task.startTime, util.getTimeObject(hoursAdded))
			# print("Added ", hoursAdded, " hours to task", task.product.name)
