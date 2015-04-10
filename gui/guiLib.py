from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import sys


mainStyle = "background:rgb(0,104,95); border: 2px solid white"
app = QtGui.QApplication(sys.argv)


class CustomButton(QtGui.QPushButton):
	def __init__(self, text, pos, instance, function=None):
		super().__init__(text, instance)
		self.resize(self.sizeHint())
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setStyleSheet(mainStyle)

		if function is not None:
			self.addCallback(function)

	def addCallback(self, function):
		self.connect(self, QtCore.SIGNAL("clicked()"), function)


class CustomLabel(QtGui.QLabel):
	def __init__(self, text, pos, instance):
		super().__init__(text, instance)
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setStyleSheet("color : white;" "font-size: 12pt")


class CustomList(QtGui.QListWidget):
	def __init__(self, pos, size, instance):
		super().__init__(instance)
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setFixedWidth(size[0])
		self.setMaximumHeight(size[1])
		self.setStyleSheet(mainStyle)


class CustomSpinBox(QtGui.QSpinBox):
	def __init__(self, pos, instance):
		super().__init__(instance)
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setMaximum(1000)


class CustomSlider(QtGui.QSlider):
	def __init__(self, pos, orientation, instance):
		super().__init__(instance)
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setStyleSheet(mainStyle)
		self.setOrientation(orientation)


class CustomProgressBar(QtGui.QProgressBar):
	def __init__(self, pos, instance):
		super().__init__(instance)
		if pos is not None:
			self.move(pos[0], pos[1])
		self.setStyleSheet(mainStyle)


def show_message_box(message, instance, title="Error"):
	QtGui.QMessageBox.about(instance, title, message)

	# assert isinstance(message, str)
	#
	# window = QtGui.QErrorMessage()
	# window.showMessage(message)
	# window.show()
