import sys
import multiprocessing


def get_cpu_cores():
    """get number of available virtual or physical cpu cores
    :return: int number of cores
    :rtype: int
    """
    return multiprocessing.cpu_count()