import unittest

from schedule.schedule import Schedule
from genetics.mutator import Mutator


class MutatorTests(unittest.TestCase):
	def setUp(self):
		self.testSchedule = Schedule()

	def test_mutateNewObject(self):
		# check that the mutator properly creates a new schedule
		self.assertFalse(Mutator.mutateSchedule(self.testSchedule) is self.testSchedule)


if __name__ == '__main__':
	unittest.main()
