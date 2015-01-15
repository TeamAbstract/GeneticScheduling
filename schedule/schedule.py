from schedule.task import Task


class Schedule:
	"""!
	Class that is used to interface with a generated schedule
	"""

	id = 0  # static variable for giving each vessel a new id

	@staticmethod
	def getNextID():
		currentID = Schedule.id
		Schedule.id += 1
		return currentID

	def __init__(self):
		self.fitness = 0.0
		self.tasks = []

		self.id = Schedule.id
		Schedule.id += 1


	def getTaskCount(self):
		"""Returns the number of tasks that the schedule has defined"""
		return len(self.tasks)


	def getTask(self, index=None):
		"""Returns a specific task or if id==None then all tasks as a tuple
		:param index: task to return default = None
		:return: task or list of tasks
		"""
		if index is not None:
			assert index < len(self.tasks) - 1
			assert index > 0

		if index is None:
			return tuple(self.tasks)
		else:
			return self.tasks[index]


	def printSchedule(self):
		print("Schedule:", self.id)
		for task in self.tasks:
			print("Task: ", task.product.name)
			task.printTask()


	def addTask(self, task):
		assert isinstance(task, Task)
		self.tasks.append(task)
