import sys
import multiprocessing


class system:
    @staticmethod
    def getCpuCores():
        """get number of available virtual or physical cpu cores
        :return: int number of cores
        """
        return multiprocessing.cpu_count()