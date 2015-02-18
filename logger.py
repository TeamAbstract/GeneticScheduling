def saveHigh(whatyouwant):
    highSave=open('HighPriorityIssues.txt', 'a')
    highSave.write(whatyouwant)
    highSave.close()

def saveMedium():
    mediumSave=open('MediumPriorityIssues.txt', 'a')


def saveLow():
    lowSave=open('LowPriorityIssues.txt', 'a')
