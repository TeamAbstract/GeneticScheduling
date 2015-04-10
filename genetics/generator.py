from schedule import *
from vessels import Vessels
import productList
from product import Product


def getNewSchedule():
	"""quick algorithm for testing
	Randomly assigns products to the schedule, doesn't check for conflicts
	or add them in any optimal way, cleaning the vessels also need to be handled
	"""
	schedule = Schedule()
	for product in productList.masterProductList:
		schedule.addTask(Task(product, Vessels.getFit(product.amount)))

	return schedule


def getNewScheduleFromList(products):
	"""! format should be [[Product, quantity], [Product, quantity]]
	:param products:
	:return:
	"""
	assert isinstance(products, list), type(products) + " " + str(products)
	schedule = Schedule()
	for product in products:
		assert isinstance(product[0], Product)
		assert isinstance(product[1], int)
		task = Task(product[0], Vessels.getFit(product[1]), None, product[1])
		schedule.addTask(task)

	return schedule
