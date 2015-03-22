from datetime import time as Time
from datetime import datetime as DateTime
from datetime import timedelta
import datetime



def getTimeObject(time=None):
	"""!create a datetime.time object from various means
	0:30  = half hour
	1:10 = 1 hour 10
	"""
	if time is None:  # create empty object
		return Time()

	assert isinstance(time, str)  # create from str
	# syntax = "hr:min" seconds probably aren't needed
	timeSignature = time.split(":")

	timeObject = None
	if len(timeSignature) == 1:
		timeObject = Time(int(timeSignature[0]) % 24)
	if len(timeSignature) == 2:
		timeObject = Time(int(timeSignature[0]) % 24, int(timeSignature[1]) % 60)
	return timeObject


def getDateTimeObject(date=None):
	"""!create a datetime.date object from various means"""
	if date is None:  # create empty object
		return DateTime(datetime.MINYEAR, 1, 1)

	if isinstance(date, str):  # create from str
		# syntax = "year:month:day:hr:min" seconds probably aren't needed
		dateSignature = date.split(":")
		assert len(dateSignature) >= 5, "DateTime object creation requires more parameters than " + repr(dateSignature)

		if len(dateSignature) == 1:
			return DateTime(int(dateSignature[0]), int(dateSignature[1]))
		if len(dateSignature) == 2:
			return DateTime(int(dateSignature[0]), int(dateSignature[1]))

	else:
		raise TypeError("Date object requires no parameter or a datetime.time object")


def addTimes(time1, time2):
	"""! add two time objects together
	:param time1: Time object
	:param time2: Time object
	:return: Combined time object
	"""

	assert isinstance(time1, Time)
	assert isinstance(time2, Time)
	# create temporary time1 to add timedelta to it
	tempTime = datetime.datetime(datetime.MINYEAR, 1, 1, time1.hour, time1.minute, time1.second)

	# timedelta object from time 2 to add
	tempTime += datetime.timedelta(0, time2.second, 0, 0, time2.minute, time2.hour)
	return tempTime.time()


def addDateTimeAndTime(date, time):
	assert isinstance(date, DateTime)
	assert isinstance(time, Time)

	return date.combine(date, addTimes(date.time(), time))


def getTotalHours(time):
	"""! Gets the total number of hours in a datetime object doesn't handle years minutes are the decimal
	:param time:
	:return: float for total hours
	"""
	if isinstance(time, DateTime):
		return time.day * 24 + time.hour + time.minute / 60
	elif isinstance(time, timedelta):
		return time.seconds/3600
	else:
		raise TypeError("getTotalHours requires DateTime or timedelta types as a paramater")
