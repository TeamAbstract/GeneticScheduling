from datetime import time as Time


class TimeUtil:
    @staticmethod
    def getTimeObject(time=None):
        """!create a datetime.time object from various means"""
        if time is None:  # create empty object
            return Time()

        if isinstance(time, str):  # create from str
                                   # syntax = "hr:min" seconds probably aren't needed
            timeSignature = time.split(":")
            if len(timeSignature) == 1:
                return Time(int(timeSignature[0]))
            if len(timeSignature) == 2:
                return Time(int(timeSignature[0]),
                            int(timeSignature[1]))