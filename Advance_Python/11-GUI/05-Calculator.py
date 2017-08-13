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
        self.box_1 = QtWidgets.QLineEdit(self)
        self.box_1.move(10, 10)
        self.box_1.resize(240,40)

        self.box_2 = QtWidgets.QLineEdit(self)
        self.box_2.move(10, 70)
        self.box_2.resize(240,40)

        self.box_3 = QtWidgets.QLineEdit(self)
        self.box_3.move(10, 250)
        self.box_3.resize(240,40)
        self.box_3.setReadOnly(True)



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

        self.result = int(self.num_1) + int(self.num_2)

        # print("Result is", self.result)

        self.box_3.setText(str(self.result))

    def sub(self):
        pass

    def mul(self):
        pass

    def div(self):
        pass



app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())