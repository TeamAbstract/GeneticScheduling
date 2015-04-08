from datetime import datetime as DateTime  # done to fit in with caps = class
import datetime

import util
from product import Product
from vessels import Vessel


class Task:
	"""!
	Class that represents a single scheduled task
	"""

	def __init__(self, product, vessel, startTime=None, volume=None):
		assert isinstance(product, Product), type(product)
		self.product = product
		if volume is None:
			self.volume = product.amount
		else:
			self.volume = volume

		self.cleanTime = util.getTimeDeltaObject("1")

		if startTime is None:
			startTime = datetime.datetime.now()
			startTime = startTime.replace(second=0, microsecond=0)

		if isinstance(startTime, DateTime):
			self.startTime = startTime
		elif isinstance(startTime, str):
			self.startTime = util.getDateTimeObject(startTime)
		else:
			raise TypeError("Task requires a datetime.datetime or str parameter not ", type(startTime))

		assert isinstance(vessel, Vessel)
		self.vessel = vessel

	def getEndTime(self):
		"""!
		Adds the duration to the time to get the finish time
		:return: datetime.time for when the task finishes
		"""
		return self.startTime + self.product.brewTime

	def getDuration(self):
		"""! gets total time for process (brewing + cleaning)
		:return: datetime object
		"""
		return self.cleanTime + self.product.brewTime

	def print(self):
		print("  ", self.startTime, " ", self.product.brewTime, "+", self.cleanTime, " ", self.volume, "kegs")
		print("   in vessels", str(self.vessel.id), "(" + str(self.vessel.size) + " kegs)")

	def __repr__(self):
		return self.product.name + " " + str(self.startTime) + "-" + str(self.getDuration())