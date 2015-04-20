import random


class Vessels:
	"""!
	Class that stores list of vessels as a static variable
	"""
	vessels = list()  # list for total number of vessels
	id = 0  # static variable used for unique id

	def __init__(self):
		pass

	@staticmethod
	def addVessel(size):
		Vessels.vessels.append(Vessel(size, Vessels.id))
		Vessels.id += 1
		Vessels.vessels.sort(key=lambda x: x.size)

	@staticmethod
	def getFit(size):
		"""! get the smallest vessel that will fit the size
		:param size: size of order in kegs
		:return: integer index of the vessel or list of vessel indexes
		"""

		for vessel in Vessels.vessels:
			if size <= vessel.size:
				return vessel
		return Vessels.vessels[-1]

	@staticmethod
	def getRandomVessel(size=None):
		choice = random.randint(0, len(Vessels.vessels)-1)
		vessel = Vessels.vessels[choice]
		if size is None:
			return vessel
		while True:
			if size < vessel.size:
				return vessel
			if choice == len(Vessels.vessels)-1:  # if largest vessel
				return vessel
			choice = random.randint(choice, len(Vessels.vessels)-1)
			vessel = Vessels.vessels[choice]

	def __repr__(self):
		return "Vessel " + self.id


class Vessel():
	"""! internal representation of a vessel
	"""

	def __init__(self, size, id):
		self.size = size
		self.id = id

	def getSize(self):
		return self.size
