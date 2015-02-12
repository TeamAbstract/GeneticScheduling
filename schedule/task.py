from datetime import datetime as DateTime  # done to fit in with caps = class
from datetime import datetime
import datetime

import util
from product import Product


class Task:
	"""!
	Class that represents a single scheduled task
	"""

	def __init__(self, product, vessels, startTime=None):
		assert isinstance(product, Product), type(product)
		self.product = product
		self.vessels = []

		self.cooldown = 1  # TODO handle cooldown properly, needs to consider change of product

		if startTime is None:
			startTime = datetime.datetime.now()
			assert isinstance(startTime, DateTime)
			startTime = startTime.replace(second=0, microsecond=0)

		if isinstance(startTime, DateTime):
			self.startTime = startTime
		elif isinstance(startTime, str):
			self.startTime = util.getDateTimeObject(startTime)
		else:
			raise TypeError("Task requires a datetime.datetime or str parameter not ", type(startTime))

		if isinstance(vessels, int):
			self.vessels.insert(0, vessels)
		elif isinstance(vessels, (list, tuple)):
			self.vessels = vessels
		elif vessels is None:  # TODO add None type handling
			pass
		else:
			raise TypeError("Task requires vessel or int parameter not ", type(vessels))

	def setDate(self, date):
		"""
		:param date: datetime date object or a string
		:return: None
		"""
		if isinstance(date, datetime.date):
			self.startTime = date
		elif isinstance(date, str):
			self.startTime = datetime.date(date)
		else:
			raise TypeError("setDate requires a datetime.datetime object or a string not", type(date))

	def getEndTime(self):
		"""
		Adds the duration to the time to get the finish time
		:return: datetime.time for when the task finishes
		"""
		return DateTime.combine(self.startTime, self.product.brewTime)

	def printTask(self):
		print("  ", self.startTime, " ", self.product.brewTime, " ", self.product.amount, "kegs")
		print("   in vessels", str(self.vessels).strip("[]"))

	def getVessel(self):
		return self.vessels
