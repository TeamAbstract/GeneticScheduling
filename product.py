from datetime import time as Time
from datetime import timedelta as TimeDelta

import util.timeUtil


class Product:
	"""!
	unscheduled product that needs to be scheduled
	"""

	def __init__(self, name, brewTime, amount, dueDate=None):
		self.name = name
		self.dueDate = dueDate
		self.amount = amount

		if isinstance(brewTime, TimeDelta):
			self.brewTime = brewTime
		elif isinstance(brewTime, str):
			self.brewTime = util.getTimeDeltaObject(brewTime)
		else:
			raise TypeError("Product parameter brewTime requires str or timedelta object not", type(brewTime))

	def __eq__(self, other):
		"""! checks for product equivalence returns True if they are the same
		currently only checks on product name, nothing more may be required
		:param other: other product to check
		:return: True if the same otherwise False
		"""

		assert isinstance(other, Product), " right operand must be Product"

		if self.name == other.name:
			return True

	def __repr__(self):
		return self.name + " " + str(self.brewTime)
