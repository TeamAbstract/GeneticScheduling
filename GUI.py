import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

mainStyle = "color: white; background:rgb(0,104,95); border: 2px solid white"


class CustomButton(QtGui.QPushButton):
	def __init__(self, text, pos, instance, function=None):
		super().__init__(text, instance)
		self.resize(self.sizeHint())
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


class CustomList(QtGui.QListWidget):
	def __init__(self, pos, size, instance):
		super().__init__(instance)
		self.move(pos[0], pos[1])
		self.setFixedWidth(size[0])
		self.setMaximumHeight(size[1])
		self.setStyleSheet(mainStyle)


class interface(QtGui.QWidget):
	def __init__(self):
		super(interface, self).__init__()
		self.initUI()

	def initUI(self):
		self.setStyleSheet("background:rgb(0,104,95);")

# Buttons
		self.newOrderBtn = CustomButton('New Order', (0, 0), self, self.newOrder)
		self.scheduleBtn = CustomButton('Schedule', (608, 0), self, self.schedule)
		self.submitBtn = CustomButton('Submit', (310, 325), self, self.submitProduct)
		self.removeBtn = CustomButton('Remove', (540, 325), self, self.remove)

# Labels
		self.productLabel = CustomLabel('Product', (75, 40), self)
		self.quantityLabel = CustomLabel('Quantity', (75, 250), self)
		self.timeLabel = CustomLabel('Time', (310, 40), self)
		self.dateLabel = CustomLabel('Date', (310, 110), self)
		self.ordersLabel = CustomLabel('Orders', (550, 40), self)


# Lists
		self.productList = CustomList((0, 75), (227, 175), self)

# TODO Rename at some point
		self.productList.addItem("Beer 1")
		self.productList.addItem("Beer 2")
		self.productList.addItem("Beer 3")
		self.productList.addItem("Beer 4")
		self.productList.addItem("Beer 5")
		self.productList.addItem("Beer 6")
		self.productList.addItem("Beer 7")
		self.productList.addItem("Beer 8")
		self.productList.addItem("Beer 9")
		self.productList.addItem("Beer 10")

		width = self.width() / 3 * 2 + 33
		self.orderList = CustomList((width, 75), (227, 200), self)

#example orders
		self.orderList.addItem("Carlsberg  12/09/15 12:00")

#TextBoxes

		quantityTextBox = QtGui.QLineEdit(self)
		quantityTextBox.move(0, 280)
		quantityTextBox.setText("0")
		quantityTextBox.setFixedWidth(self.orderList.width())
		quantityTextBox.setStyleSheet(mainStyle)


#Time and Date Selection

		hourSelect = QtGui.QComboBox(self)
		hourSelect.move(270, 70)
		hourSelect.setStyleSheet(mainStyle)
		hourSelect.setFixedWidth(150)

		for hour in range(0, 23):
			hourSelect.addItem(str(hour).zfill(2) + ":00")

		datePicker = QtGui.QCalendarWidget(self)
		xpos = self.productList.geometry().right() + 10
		datePicker.move(xpos, 150)
		datePicker.setHorizontalHeaderFormat(0)
		datePicker.setVerticalHeaderFormat(0)
		datePicker.setGridVisible(1)


#Set Interface size and title

		# self.setGeometry(50, 50, 683, 384)
		self.setWindowTitle('Brewery Scheduling')


	# Lines

	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QtGui.QPen(Qt.white, 2, Qt.SolidLine)

		qp.setPen(pen)
		pen.setWidth(2)

		topLineYpos = self.newOrderBtn.geometry().bottom() + 3
		qp.drawLine(0, topLineYpos, self.width(), topLineYpos)

		leftLineYpos = self.productList.geometry().right() + 4
		qp.drawLine(leftLineYpos, topLineYpos, leftLineYpos, self.height())

		rightLineYpos = self.orderList.geometry().left() - 3
		qp.drawLine(rightLineYpos, topLineYpos, rightLineYpos, self.height())

	def submitProduct(self):
		print("submitting")

	def newOrder(self):
		print("new order")

	def schedule(self):
		print("scheduling")

	def remove(self):
		print("removing")


def startGUI():
	app = QtGui.QApplication(sys.argv)
	ex = interface()
	ex.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	startGUI()
