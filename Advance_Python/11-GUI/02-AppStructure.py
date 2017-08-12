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
        self.show()

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())