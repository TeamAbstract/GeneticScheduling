from genetics.fitnessTest import FitnessTest
from genetics.genepool import GenePool

genepool = GenePool()

def addSchedule(schedule):
	genepool.addSchedule(schedule)


def tick():
	genepool.refreshSchedules()
	FitnessTest.testPool(genepool)
	genepool.removeSchedules()
	# print(genepool.getBestSchedule().fitness)
