from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import sys


mainStyle = "color: white; background:rgb(0,104,95); border: 2px solid white"
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
		self.move(pos[0], pos[1])
		self.setStyleSheet("color : white;" "font-size: 12pt")


class CustomListItem(QtGui.QListWidget):
	def __init__(self):
		super().__init__()


class CustomList(QtGui.QListWidget):
	def __init__(self, pos, size, instance):
		super().__init__(instance)
		self.move(pos[0], pos[1])
		self.setFixedWidth(size[0])
		self.setMaximumHeight(size[1])
		self.setStyleSheet(mainStyle)
