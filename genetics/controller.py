from genetics.fitnessTest import FitnessTest
from genetics.genepool import GenePool

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
