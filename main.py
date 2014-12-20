import sys

from generator import Generator
from genepool import Genepool
from taskList import TaskList

if sys.version_info < (3, 0):
    raise EnvironmentError("Outdated version update to V3")
else:
    print("System check fine")

taskList = TaskList()

genepool = Genepool()
genepool.addSchedule(Generator.getNewSchedule())
genepool.addSchedule(Generator.getNewSchedule())
genepool.addSchedule(Generator.getNewSchedule())
genepool.printPool()