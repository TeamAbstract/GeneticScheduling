from schedule import *
from vessels import Vessels
import productList


class Generator:
    """!
    Class responsible for generating schedules
    """

    # TODO more sophisticated generation algorithm
    # Put products into smallest vessel possible
    # group similar products to reduce cleaning time
    def getNewSchedule(self):
        """quick algorithm for testing
        Randomly assigns products to the schedule, doesn't check for conflicts
        or add them in any optimal way, cleaning the vessels also need to be handled
        """
        schedule = Schedule()
        for product in productList.masterProductList:
            schedule.addTask(Task(product, Vessels.getFit(product.amount)))

        return schedule
