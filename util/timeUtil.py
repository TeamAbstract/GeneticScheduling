from datetime import time as Time
from datetime import datetime as DateTime
import datetime
import traceback


def getTimeObject(time=None):
	"""!create a datetime.time object from various means"""
	if time is None:  # create empty object
		return Time()

	assert isinstance(time, str)  # create from str
	# syntax = "hr:min" seconds probably aren't needed
	timeSignature = time.split(":")

	timeObject = None
	if len(timeSignature) == 1:
		timeObject = Time(int(timeSignature[0]) % 24)
	if len(timeSignature) == 2:
		timeObject = Time(int(timeSignature[0]) % 24,
						  int(timeSignature[1]) % 60)
	return timeObject


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


def addTimes(time1, time2):
	"""!
	:param time1: Time object
	:param time2: Time object
	:return: Combined time object
	"""

	assert isinstance(time1, Time)
	assert isinstance(time2, Time)


def getTotalHours(time):
	assert isinstance(time, DateTime)
	return time.days * 24 + time.hour
