import datetime


class Schedule:
	""" Class that is used to interface with a generated schedule"""

	vessels = []
	rating = 0.0

	def __init__(self, numOfVessels):
		self.vessels = [Vessel() for x in range(numOfVessels)]

	def getVesselCount(self):
		"""Returns the number of vessels currently defined"""
		return len(self.vessels)

	def printSchedule(self):
		for vessel in self.vessels:
			vessel.printVessel()


class Vessel:
	""" Class that stores the information and schedule on a per vessel basis"""

	tasks = []

	def addTask(self, task):
		if isinstance(task, Task):
			self.tasks += task

	def printVessel(self):
		for task in self.tasks:
			task.printTask()


class Task:
	""" Class that represents a single task"""
	name = ""
	time = None
	duration = None

	def __init__(self):
		pass

	def setDate(self, time):
		"""
		:param time: datetime date object or a string
		:return: None
		"""
		if isinstance(time, datetime.datetime):
			self.time = time
		elif isinstance(time, str):
			self.time = datetime.date(time)
		else:
			raise TypeError("setDate requires a datetime.datetime object or a string")

	def setDuration(self, duration):
		"""
		:param duration: datetime object or a string
		:return: None
		"""
		if isinstance(duration, datetime.time):
			self.duration = duration
		elif isinstance(duration, str):
			self.duration = datetime.time(duration)
		else:
			raise TypeError("setDuration requires a datetime.time object or a string")

	def printTask(self):
		print(self.name + ":" + self.time.strftime() + " " + self.duration.strftime())

