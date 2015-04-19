from gui.guiLib import *


class ScheduleRenderer(QtGui.QListWidget):
	def __init__(self, instance):
		super().__init__(instance)

	def colour(self):
		for x in range(self.count()):
			task = self.item(x)
			# TODO colour tasks e.g. if they overlap
