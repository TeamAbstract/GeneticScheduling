from schedule.task import Task
from datetime import timedelta as TimeDelta
import settings
import util

from copy import deepcopy

from decimal import *


class Schedule:
	"""!
	Class that is used to interface with a generated schedule
	"""

	id = 0  # static variable for giving each vessel a new id

	@staticmethod
	def getNextID():
		"""! returns the static variable id and increments it
		:return: current value of id
		"""
		currentID = Schedule.id
		Schedule.id += 1
		return currentID

	def __init__(self):
		self.fitness = Decimal(0)
		self.tasks = []

		self.id = Schedule.getNextID()
		self.setCleanTime()
		self.flags = set()

	def getTask(self, index):
		"""Returns a specific task or if id==None then all tasks as a tuple
		:param index: task to return default = None
		:return: task or list of tasks
		"""
		assert index < len(self.tasks), index
		assert index >= 0, index
		return self.tasks[index]

	def print(self, printDetails=True):
		print("Schedule:", self.id, " fitness ", self.fitness, self.flags if len(self.flags) > 0 else "")
		self.sortByStartTime()
		if printDetails:
			for task in self.tasks:
				print("Task: ", task.product.name)
				task.print()
		print()

	def addTask(self, task):
		assert isinstance(task, Task)
		self.tasks.append(task)
		self.setCleanTime()

	def sortByStartTime(self):
		self.tasks.sort(key=lambda task: task.startTime)
		pass

	def setCleanTime(self):
		"""! iterates through schedule and sets clean time depending on next schedule

		needs to be called every time a schedule is changed
		"""

		self.sortByStartTime()

		for index, task in enumerate(self.tasks):
			if index == len(self.tasks) - 1:  # if last task
				task.cleanTime = settings.longerCleanTime  # TODO decide if this should be default clean time
				return

			nextTask = self.tasks[index + 1]
			if task.product == nextTask.product:
				task.cleanTime = settings.defaultCleanTime
			else:  # products are different
				task.cleanTime = settings.longerCleanTime

	def splitTask(self, task):
		"""! splits up two tasks so they can be put into separate vessels

		maintains every other aspect between the two tasks including volume
		"""
		if task not in self.tasks:
			raise AttributeError("task not in this schedule")
		task.volume /= 2
		newTask = deepcopy(task)
		self.tasks.append(newTask)

	def getTotalTime(self):
		"""! gets the total number of hours that the schedule is operating for
		:return: total time
		:rtype: TimeDelta
		"""

		totalTime = util.getTimeDeltaObject()

		for task in self.tasks:
			totalTime += task.product.brewTime + task.cleanTime
		return totalTime

	def __repr__(self):
		return str(self.fitness)
