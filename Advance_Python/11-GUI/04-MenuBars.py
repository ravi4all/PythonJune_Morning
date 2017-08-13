from PyQt5 import QtWidgets
import sys

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Menu Bars")

        menu_item_1 = QtWidgets.QAction("Open", self)
        menu_item_1.setShortcut("Ctrl+o")
        menu_item_2 = QtWidgets.QAction("Exit", self)
        menu_item_2.setShortcut("Ctrl+q")
        menu_item_2.triggered.connect(self.close_app)

        menu_item_3 = QtWidgets.QAction("Cut", self)
        menu_item_3.setShortcut("Ctrl+x")

        menu_item_4 = QtWidgets.QAction("Copy", self)
        menu_item_4.setShortcut("Ctrl+c")

        menu_item_5 = QtWidgets.QAction("Paste", self)
        menu_item_5.setShortcut("Ctrl+v")

        self.statusBar()

        fileMenu = self.menuBar()
        mainMenu_1 = fileMenu.addMenu('File')
        mainMenu_1.addAction(menu_item_1)
        mainMenu_1.addAction(menu_item_2)

        mainMenu_2 = fileMenu.addMenu('Edit')
        mainMenu_2.addAction(menu_item_3)
        mainMenu_2.addAction(menu_item_4)
        mainMenu_2.addAction(menu_item_5)


        self.show()

    def close_app(self):
        choice = QtWidgets.QMessageBox.question(self, "Quit", "Do you wanna quit ?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

        # sys.exit()


app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())