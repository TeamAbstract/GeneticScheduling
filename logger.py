def saveHigh(whatyouwant):
	file = open('HighPriorityIssues.txt', 'a')
	file.write(formatError(whatyouwant))
	file.close()


def saveMedium(whatyouwant):
	file = open('MediumPriorityIssues.txt', 'a')
	file.write(formatError(whatyouwant))
	file.close()


def saveLow(whatyouwant):
	file = open('LowPriorityIssues.txt', 'a')
	file.write(formatError(whatyouwant))
	file.close()


def formatError(input):
	if not isinstance(input, str):
		return repr(input)
	return input
