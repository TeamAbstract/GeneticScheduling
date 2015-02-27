from datetime import time as Time

import util.timeUtil


class Product:
	"""!
	unscheduled product that needs to be scheduled
	"""

	def __init__(self, name, brewTime, amount, dueDate=None):
		self.name = name
		self.dueDate = dueDate
		self.amount = amount

		if isinstance(brewTime, Time):
			self.brewTime = brewTime
		elif isinstance(brewTime, str):
			self.brewTime = util.timeUtil.getTimeObject(brewTime)
		else:
			raise TypeError("Product parameter brewTime requires str or Time object not", type(brewTime))

	def __eq__(self, other):
		"""! checks for product equivalence returns True if they are the same
		currently only checks on product name, nothing more may be required
		:param other: other product to check
		:return: True if the same otherwise False
		"""

		assert isinstance(other, Product), " right operand must also be product"

		if self.name == other.name:
			return True

	def __str__(self):
		return self.name + str(self.brewTime)
