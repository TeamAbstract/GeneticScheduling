from genepool import GenePool


class FitnessTest:

    @staticmethod
    def testPool(genePool):
        assert isinstance(genePool, GenePool)
        iterable = genePool.getIterable()
        for schedule in iterable:
            FitnessTest.testSchedule(schedule)

    @staticmethod
    def testSchedule(schedule):
        # TODO add more requirements
        # TODO fitness test function
        """
        Tests a single schedule for it's fitness
        :param schedule: schedule to be tested

        Schedule Requirements:
        No conflicts
        Minimal cleaning time(same products in each vessel)
        Products completed before due date
        Nothing starts/finishes after hours
        """
        print("Testing schedule ", schedule.id)

        fitness = 0.0



        schedule.fitness = fitness
