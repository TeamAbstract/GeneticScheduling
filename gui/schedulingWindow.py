from PyQt4 import QtGui, QtCore
import genetics.controller as controller
from gui.guiLib import *
from schedule.schedule import Schedule
from gui.scheduleRenderer import ScheduleRenderer


class SchedulingWindow(QtGui.QWidget):
	updateSignal = QtCore.pyqtSignal()

	def __init__(self):
		super(SchedulingWindow, self).__init__()

		self.bestSchedule = None

		self.updateSignal.connect(self.updateGUIWithValues)

		self.setStyleSheet("background:rgb(0,104,95); color:white;")

		self.stopBtn = CustomButton("Stop", (0, 50), self, self.onStopButtonClicked)
		self.startBtn = CustomButton("Start", (0, 50), self, self.onStartButtonClicked)
		self.progressLabel = CustomLabel("Current fitness", None, self)
		self.progressText = CustomLabel("0", None, self)
		self.progressBar = CustomProgressBar(None, self)

		self.schedule = ScheduleRenderer(self)

		self.targetLabel = CustomLabel("Target fitness", None, self)
		self.targetSpinBox = CustomSpinBox(None, self)
		self.targetSpinBox.setValue(80)


		self.layout = QtGui.QGridLayout()

		self.targetSpinBox.connect(self, QtCore.SIGNAL("clicked()"), self.onSpinBoxClick)

		# row 0
		self.layout.addWidget(self.stopBtn, 0, 0)
		self.layout.addWidget(self.startBtn, 0, 1)

		# row 1
		self.layout.addWidget(self.progressLabel, 1, 0)
		self.layout.addWidget(self.progressText, 1, 1)

		# row 2
		self.layout.addWidget(self.targetLabel, 2, 0)
		self.layout.addWidget(self.targetSpinBox, 2, 1)

		# row 3
		self.layout.addWidget(self.schedule)

		# row 4
		self.layout.addWidget(self.progressBar, 4, 0, 3, 1)

		self.setLayout(self.layout)

	def setSchedule(self, schedule):
		assert isinstance(schedule, Schedule)
		controller.genepool.addSchedule(schedule)

	def onSpinBoxClick(self):
		self.progressBar.setMaximum(self.targetSpinBox.value())

	def onStartButtonClicked(self):
		self.thread = self.ProcessingThread()
		self.thread.giveInstance(self)
		self.thread.start()

	def onStopButtonClicked(self):
		controller.running = False

	def updateGUIWithValues(self):
		self.progressBar.setMaximum(self.targetSpinBox.value())
		self.progressText.setText(str(round(self.bestSchedule.fitness, 2)))
		self.progressBar.setValue(int(self.bestSchedule.fitness))

		self.schedule.clear()
		if self.bestSchedule is not None:
			for task in self.bestSchedule.tasks:
				self.schedule.addItem(str(task))

	class ProcessingThread(QtCore.QThread):
		def giveInstance(self, instance):
			self.updateCounter = 0
			self.guiInstance = instance

		def run(self):
			while controller.genepool.getBestSchedule().fitness < self.guiInstance.targetSpinBox.value() and controller.running:
				controller.tick()
				self.updateCounter += 1
				# only update every 5th time
				# more frequent updates freeze the gui
				if self.updateCounter % 5 == 0:
					self.guiInstance.updateSignal.emit()
				self.guiInstance.bestSchedule = controller.genepool.getBestSchedule()

