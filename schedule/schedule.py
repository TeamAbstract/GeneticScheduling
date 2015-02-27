from schedule.task import Task
import settings


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
		self.fitness = 0.0
		self.tasks = []

		self.id = Schedule.id
		Schedule.id += 1
		self.setCleanTime()

	def getTask(self, index):
		"""Returns a specific task or if id==None then all tasks as a tuple
		:param index: task to return default = None
		:return: task or list of tasks
		"""
		assert index < len(self.tasks), index
		assert index >= 0, index
		return self.tasks[index]

	def printSchedule(self, printDetails=True):
		print("Schedule:", self.id, " fitness ", self.fitness)
		self.sortByStartTime()
		if printDetails:
			for task in self.tasks:
				print("Task: ", task.product.name)
				task.printTask()
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
				print("set longer Time")
