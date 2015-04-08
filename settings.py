import util

defaultCleanTime = util.getTimeDeltaObject("0:30")  # clean time in hours for schedules of same product
longerCleanTime = util.getTimeDeltaObject("1")  # clean time for schedules of different product

openingTime = util.getTimeObject("9:00")
closingTime = util.getTimeObject("17:00")
