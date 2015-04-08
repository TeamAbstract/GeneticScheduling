from copy import deepcopy
from random import randint

import settings

import util

from schedule.schedule import Schedule
from schedule.task import Task
from vessels import Vessels


class Mutator:
	"""!
	class responsible for mutating the schedule and creating the next generation
	"""

	# static variables for settings
	percentageChange = 50  # chance of a variable being changed(0-100)

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
		newSchedule.fitness = None
		assert isinstance(newSchedule, Schedule)

		for index, task in enumerate(newSchedule.tasks):
			if randint(0, 100) >= Mutator.percentageChange:
				continue
			Mutator.mutateTask(newSchedule.getTask(index))

		newSchedule.setCleanTime()
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
			task.startTime = task.startTime + util.getTimeDeltaObject(str(randint(-12, 12)))
			while not settings.openingTime < task.startTime.time() < util.addTimeAndTimeDelta(settings.closingTime, task.getDuration()):
				task.startTime = task.startTime + util.getTimeDeltaObject(str(randint(-12, 12)))

			# print("Added ", hoursAdded, " hours to task", task.product.name)
