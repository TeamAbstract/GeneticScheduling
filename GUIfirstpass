import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class interface(QtGui.QWidget):

    def __init__(self):
        super(interface, self).__init__()

        self.initUI()

    def initUI(self):


        self.setStyleSheet("background:rgb(0,104,95);")

#Buttons
        newOrderBtn = QtGui.QPushButton('New Order', self)
        newOrderBtn.resize(newOrderBtn.sizeHint())
        newOrderBtn.move(0, 0)

        newOrderBtn.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")


        scheduleBtn = QtGui.QPushButton('Schedule', self)
        scheduleBtn.resize(scheduleBtn.sizeHint())
        scheduleBtn.move(608,0)
        scheduleBtn.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")

        submitBtn = QtGui.QPushButton('Submit', self)
        submitBtn.resize(submitBtn.sizeHint())
        submitBtn.move(310,325)
        submitBtn.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")

        removeBtn = QtGui.QPushButton('Remove', self)
        removeBtn.resize(removeBtn.sizeHint())
        removeBtn.move(540,325)
        removeBtn.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")


#Labels
        productLabel = QtGui.QLabel('Product', self)
        productLabel.move(75,40)
        productLabel.setStyleSheet("color : white;" "font-size: 12pt")

        quantityLabel = QtGui.QLabel('Quantity', self)
        quantityLabel.move(75,250)
        quantityLabel.setStyleSheet("color : white;" "font-size: 12pt")

        timeLabel = QtGui.QLabel('Time',self)
        timeLabel.move(310,40)
        timeLabel.setStyleSheet("color : white;" "font-size: 12pt")

        dateLabel = QtGui.QLabel('Date',self)
        dateLabel.move(310,110)
        dateLabel.setStyleSheet("color : white;" "font-size: 12pt")

        ordersLabel = QtGui.QLabel('Orders',self)
        ordersLabel.move(550,40)
        ordersLabel.setStyleSheet("color : white;" "font-size: 12pt")


#Lists
        productList = QtGui.QListWidget(self)
        productList.move(0,75)
        productList.setFixedWidth(227)
        productList.setMaximumHeight(175)
        productList.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")

#Rename at some point
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
        orderList.move(self.width() / 3 * 2 + 33,75)
        orderList.setFixedWidth(227)
        orderList.setFixedHeight(200)
        orderList.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")

#example orders
        orderList.addItem("Carlsberg  12/09/15 12:00")

#TextBoxes

        quantityTextBox = QtGui.QLineEdit(self)
        quantityTextBox.move(0,280)
        quantityTextBox.setText("0")
        quantityTextBox.setFixedWidth(228)
        quantityTextBox.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95)")


#Time and Date Selection

        hourSelect = QtGui.QComboBox(self)
        hourSelect.move(270,70)
        hourSelect.setStyleSheet("color : white;"
                                  "background:rgb(0,104,95);"
                                  "border: 2px solid white")
        hourSelect.setFixedWidth(150)
        hourSelect.addItem("00:00")
        hourSelect.addItem("01:00")
        hourSelect.addItem("02:00")
        hourSelect.addItem("03:00")
        hourSelect.addItem("04:00")
        hourSelect.addItem("05:00")
        hourSelect.addItem("06:00")
        hourSelect.addItem("07:00")
        hourSelect.addItem("08:00")
        hourSelect.addItem("09:00")
        hourSelect.addItem("10:00")
        hourSelect.addItem("11:00")
        hourSelect.addItem("12:00")
        hourSelect.addItem("13:00")
        hourSelect.addItem("14:00")
        hourSelect.addItem("15:00")
        hourSelect.addItem("16:00")
        hourSelect.addItem("17:00")
        hourSelect.addItem("18:00")
        hourSelect.addItem("19:00")
        hourSelect.addItem("20:00")
        hourSelect.addItem("21:00")
        hourSelect.addItem("22:00")
        hourSelect.addItem("23:00")

        datePicker = QtGui.QCalendarWidget(self)
        datePicker.move(228,150)
        datePicker.setHorizontalHeaderFormat(0)
        datePicker.setVerticalHeaderFormat(0)
        datePicker.setGridVisible(1)


#Set Interface size and title

        self.setGeometry(50, 50, 683, 384)
        self.setWindowTitle('UI Test')
        self.show()





#Lines

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
        qp.drawLine(self.width()/3, 22,self.width()/3, self.height())
        qp.drawLine(self.width() /3 * 2 + 5 , 22, self.width() /3 *2 + 5, self.height())






def main():

    app = QtGui.QApplication(sys.argv)
    ex = interface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
