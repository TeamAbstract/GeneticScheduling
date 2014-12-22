from genepool import GenePool


class FitnessTest:

    @staticmethod
    def testPool(genePool):
        assert isinstance(genePool, GenePool)
        iterable = genePool.getIterable()
        try:
            schedule = iterable.next()  #TODO threading?
        except StopIteration:
            pass

    @staticmethod
    def testSchedule(schedule):
        """
        Tests a single schedule for it's fitness
        :param schedule: schedule to be tested
        """
        print("Testing schedule ", schedule.id)

        fitness = 0.0



        schedule.fitness = fitness