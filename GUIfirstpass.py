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


class interface(QtGui.QWidget):
	def __init__(self):
		super(interface, self).__init__()
		self.initUI()

	def initUI(self):
		self.setStyleSheet("background:rgb(0,104,95);")

# Buttons
		newOrderBtn = CustomButton('New Order', (0, 0), self, self.newOrder)
		scheduleBtn = CustomButton('Schedule', (608, 0), self, self.schedule)
		submitBtn = CustomButton('Submit', (310, 325), self, self.submitProduct)
		removeBtn = CustomButton('Remove', (540, 325), self, self.remove)

# Labels
		productLabel = CustomLabel('Product', (75, 40), self)
		quantityLabel = CustomLabel('Quantity', (75, 250), self)
		timeLabel = CustomLabel('Time', (310, 40), self)
		dateLabel = CustomLabel('Date', (310, 110), self)
		ordersLabel = CustomLabel('Orders', (550, 40), self)


# Lists
		productList = QtGui.QListWidget(self)
		productList.move(0, 75)
		productList.setFixedWidth(227)
		productList.setMaximumHeight(175)
		productList.setStyleSheet(mainStyle)

# TODO Rename at some point
		productList.addItem("Beer 1")
		productList.addItem("Beer 2")
		productList.addItem("Beer 3")
		productList.addItem("Beer 4")
		productList.addItem("Beer 5")
		productList.addItem("Beer 6")
		productList.addItem("Beer 7")
		productList.addItem("Beer 8")
		productList.addItem("Beer 9")
		productList.addItem("Beer 10")

		orderList = QtGui.QListWidget(self)
		orderList.move(self.width() / 3 * 2 + 33, 75)
		orderList.setFixedWidth(227)
		orderList.setFixedHeight(200)
		orderList.setStyleSheet(mainStyle)

#example orders
		orderList.addItem("Carlsberg  12/09/15 12:00")

#TextBoxes

		quantityTextBox = QtGui.QLineEdit(self)
		quantityTextBox.move(0, 280)
		quantityTextBox.setText("0")
		quantityTextBox.setFixedWidth(228)
		quantityTextBox.setStyleSheet("color : white;"
		                              "background:rgb(0,104,95)")


#Time and Date Selection

		hourSelect = QtGui.QComboBox(self)
		hourSelect.move(270, 70)
		hourSelect.setStyleSheet(mainStyle)
		hourSelect.setFixedWidth(150)
		for hour in range(0, 23):
			hourSelect.addItem(str(hour).zfill(2) + ":00")

		datePicker = QtGui.QCalendarWidget(self)
		datePicker.move(228, 150)
		datePicker.setHorizontalHeaderFormat(0)
		datePicker.setVerticalHeaderFormat(0)
		datePicker.setGridVisible(1)


#Set Interface size and title

		self.setGeometry(50, 50, 683, 384)
		self.setWindowTitle('UI Test')
		self.show()


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
		qp.drawLine(0, 22, 683, 22)
		qp.drawLine(self.width() / 3, 22, self.width() / 3, self.height())
		qp.drawLine(self.width() / 3 * 2 + 5, 22, self.width() / 3 * 2 + 5, self.height())

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
	sys.exit(app.exec_())


if __name__ == '__main__':
	startGUI()
