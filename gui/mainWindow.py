import productList
from gui.guiLib import *

from gui.schedulingWindow import SchedulingWindow

import genetics.controller
import genetics.generator

import threading


class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()

	def initUI(self):
		self.setStyleSheet("background:rgb(0,104,95); color:white;")

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
		for product in productList.masterProductList:
			self.productList.addItem(product.name)

		width = self.width() / 3 * 2 + 33
		self.orderList = CustomList((width, 75), (227, 200), self)


#TextBoxes

		self.quantityTextBox = QtGui.QLineEdit(self)
		self.quantityTextBox.move(0, 280)
		self.quantityTextBox.setText("0")
		self.quantityTextBox.setFixedWidth(self.orderList.width())
		self.quantityTextBox.setStyleSheet(mainStyle)


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
		quantity = int(self.quantityTextBox.text())
		for productIndex in self.productList.selectedItems():
			product = productList.getByName(productIndex.text())
			line = product.name + "-" + str(quantity) + " barrels-" + str(product.brewTime) + " hours"
			self.orderList.addItem(line)

	def newOrder(self):
		"""deletes all items in the order list and resets state
		"""
		for x in reversed(range(self.orderList.count())):
			self.orderList.takeItem(x)

	def schedule(self):
		if self.orderList.count() == 0:
			show_message_box("No orders added", self)
			return

		items = []
		for x in range(self.orderList.count()):
			# taken from qt order list so has to be formatted
			item = self.orderList.item(x)
			if item is None:
				continue
			name = item.text().split("-")
			amount = int(name[1].split(" ")[0])

			assert isinstance(amount, int), "amount must be integer not " + str(type(amount))
			items.append([productList.getByName(name[0]), amount])

		schedule = genetics.generator.getNewScheduleFromList(items)
		genetics.controller.addSchedule(schedule)

		sWin.show()
		mWIn.close()

	def remove(self):
		for x in reversed(range(self.orderList.count())):
			item = self.orderList.item(x)
			assert isinstance(item, QtGui.QListWidgetItem)
			if item.isSelected():
				self.orderList.takeItem(x)

mWIn = MainWindow()
sWin = SchedulingWindow()


def startGUI():
	mWIn.show()
	app.exec_()

if __name__ == '__main__':
	startGUI()
