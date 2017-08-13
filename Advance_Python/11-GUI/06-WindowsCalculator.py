import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QMainWindow):
# class, inherit from QtGui.QMainWindow

    def __init__(self):
        # Self refrence the current class
        super(Window, self).__init__()
        # Super:- window returns the parent object, so that it acts like a QT object
        self.setGeometry(50, 50, 500, 400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.buttons()
        self.textFields()

        self.num_1 = 0
        self.num_2 = 0
        self.result = 0

        self.show()

    def textFields(self):
        self.box_1 = QtWidgets.QPushButton("0", self)
        self.box_1.move(10, 300)
        self.box_1.resize(30,30)

        self.box_2 = QtWidgets.QPushButton("1", self)
        self.box_2.move(50, 300)
        self.box_2.resize(30,30)

        self.box_3 = QtWidgets.QPushButton("2", self)
        self.box_3.move(90, 300)
        self.box_3.resize(30,30)

        self.box_4 = QtWidgets.QPushButton("3", self)
        self.box_4.move(130, 300)
        self.box_4.resize(30,30)

        self.box_5 = QtWidgets.QPushButton("4", self)
        self.box_5.move(170, 300)
        self.box_5.resize(30,30)

        self.resultBox = QtWidgets.QLineEdit(self)
        self.resultBox.move(10, 50)
        self.resultBox.resize(240,40)
        self.resultBox.setReadOnly(True)

        self.btns = [self.box_1, self.box_2, self.box_3, self.box_4, self.box_5]

        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.clicked)


    def clicked(self):
        sender = self.sender()

        newNum = list(sender.text())
        copyNum = newNum.copy()
        # print("Clicked on",newNum)
        self.resultBox.setText(str(copyNum))


    def buttons(self):
        btn_1 = QtWidgets.QPushButton("+", self)
        btn_1.clicked.connect(self.add)
        btn_1.resize(20, 20)
        btn_1.move(100,150)

        btn_2 = QtWidgets.QPushButton("-", self)
        btn_2.clicked.connect(self.sub)
        btn_2.resize(20, 20)
        btn_2.move(130,150)

        btn_3 = QtWidgets.QPushButton("x", self)
        btn_3.clicked.connect(self.mul)
        btn_3.resize(20, 20)
        btn_3.move(160,150)

        btn_4 = QtWidgets.QPushButton("/", self)
        btn_4.clicked.connect(self.div)
        btn_4.resize(20, 20)
        btn_4.move(190,150)

    def add(self):
        self.num_1 = self.box_1.text()
        self.num_2 = self.box_2.text()

        print(self.num_1)

        # self.result = int(self.num_1) + int(self.num_2)

        # print("Result is", self.result)

        # self.resultBox.setText(str(self.result))

    def sub(self):
        pass

    def mul(self):
        pass

    def div(self):
        pass



app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())