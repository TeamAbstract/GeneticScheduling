from gui.gui import *


class SchedulingWindow(QtGui.QWidget):
	def __init__(self):
		super(SchedulingWindow, self).__init__()
		self.initUI()

	def initUI(self):
		self.setStyleSheet(mainStyle)

		self.stopBtn = CustomButton("Stop", None, self)

		self.layout = QtGui.QGridLayout(self.stopBtn)
