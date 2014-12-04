class Schedule:
	""" Class that is used to interface with a generated schedule"""

	vessels = []

	def __init__(self, numOfVessels):
		self.vessels = [Vessel() for x in range(numOfVessels)]

	"""Returns the number of vessels currently defined"""
	def getVesselCount(self):
		return len(self.vessels)


class Vessel:
	""" Class that stores the information and schedule on a per vessel basis"""
	def __init__(self):
		pass


class Task:
	""" Class that represents a single task"""
	name = ""

	def __init__(self):
		pass
