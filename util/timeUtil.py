from datetime import time as Time
from datetime import datetime as DateTime
import datetime


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

    else:
        raise TypeError("Time object requires no parameter or a datetime.time object")


def getDateTimeObject(date=None):
    """!create a datetime.date object from various means"""
    if date is None:  # create empty object
        return DateTime()

    if isinstance(date, str):  # create from str
                               # syntax = "year:month:day:hr:min" seconds probably aren't needed
        dateSignature = date.split(":")
        assert len(dateSignature) >= 5, "DateTime object creation requires more parameters than " + repr(dateSignature)

        if len(dateSignature) == 1:
            return DateTime(int(dateSignature[0]), int(dateSignature[1]))
        if len(dateSignature) == 2:
            return DateTime(int(dateSignature[0]),
                        int(dateSignature[1]))

    else:
        raise TypeError("Date object requires no parameter or a datetime.time object")


def addDateAndTime(date, time):
    """
    Add a datetime and a time object together
    :param date: datetime object
    :param time: time object
    :return: added datetime object
    """
    assert isinstance(date, datetime.date), type(date)
    assert isinstance(time, Time), type(time)
    hour = date.hour + time.hour
    minute = date.minute + time.minute
    second = date.second + time.second  # for completeness

    return DateTime.combine(date, Time(hour, minute, second))
