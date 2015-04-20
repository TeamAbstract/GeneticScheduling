from genetics.fitnessTest import FitnessTest
from genetics.generator import getNewScheduleFromList
from genetics.genepool import GenePool
from product import Product
from schedule import Task
from vessels import Vessels

genepool = GenePool()
running = True
iterationCount = 0


def addSchedule(schedule):
	genepool.addSchedule(schedule)


def tick():
	global iterationCount

	genepool.refreshSchedules()
	FitnessTest.testPool(genepool)
	genepool.removeSchedules()
	iterationCount += 1
	# print(genepool.getBestSchedule().fitness)


if __name__ == "__main__":
	vessels = Vessels()
	vessels.addVessel(20)
	vessels.addVessel(30)
	vessels.addVessel(50)

	genepool.addSchedule(getNewScheduleFromList([
		[Product("1", "2", "10"), 10],
		[Product("2", "2", "10"), 10],
		[Product("3", "2", "10"), 10],
		[Product("4", "2", "10"), 10],
		[Product("5", "2", "10"), 10],
		[Product("6", "2", "10"), 10],
	]))

	for _count in range(100):
		genepool.refreshSchedules()
		FitnessTest.testPool(genepool)
		genepool.removeSchedules()

		print(genepool.getBestSchedule().fitness)
	genepool.getBestSchedule().print()
