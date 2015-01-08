from genepool import GenePool


class FitnessTest:

    @staticmethod
    def testPool(genePool):
        assert isinstance(genePool, GenePool)
        iterable = genePool.getIterable()
        try:
            schedule = iterable.next()  # TODO threading?
        except StopIteration:
            pass

    @staticmethod
    def testSchedule(schedule):
        # TODO add more requirements
        """
        Tests a single schedule for it's fitness
        :param schedule: schedule to be tested

        Schedule Requirements:
        No conflicts
        Minimal cleaning time(same products in each vessel)
        Products completed before due date
        Nothing finishes after hours
        """
        print("Testing schedule ", schedule.id)

        fitness = 0.0



        schedule.fitness = fitness
