# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
import sys

class MainGame(QtWidgets.QMainWindow):

    answers = ["Modi", "Delhi"]

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1067, 551)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 160, 871, 111))
        self.label.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 211, 51))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 300, 211, 51))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 410, 211, 51))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 410, 211, 51))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Who is the prime minister of India ?"))
        self.pushButton.setText(_translate("Dialog", "Modi"))
        self.pushButton_2.setText(_translate("Dialog", "Kejriwal"))
        self.pushButton_3.setText(_translate("Dialog", "Lalu"))
        self.pushButton_4.setText(_translate("Dialog", "Yogi"))

        self.ans_1 = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4]

        for i in range(len(self.ans_1)):
            self.ans_1[i].clicked.connect(self.checkAns)

    def checkAns(self):

        sender = self.sender()
        # print(sender.text())
        ans = sender.text()
        if ans == "Modi":
            print("Correct Answer")
            self.nextQues_1()
        elif ans == "Delhi":
            print("Correct Answer")
            self.nextQues_2()
        else:
            print("Wrong Answer")
            self.close_app()

    def nextQues_1(self):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "What is the capital of India ?"))
        self.pushButton.setText(_translate("Dialog", "Delhi"))
        self.pushButton_2.setText(_translate("Dialog", "Lucknow"))
        self.pushButton_3.setText(_translate("Dialog", "Chennai"))
        self.pushButton_4.setText(_translate("Dialog", "Patna"))

    def nextQues_2(self):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "When was GST Implemented ?"))
        self.pushButton.setText(_translate("Dialog", "1st April 2017"))
        self.pushButton_2.setText(_translate("Dialog", "31st July 2017"))
        self.pushButton_3.setText(_translate("Dialog", "1st July 2017"))
        self.pushButton_4.setText(_translate("Dialog", "5th June 2017"))


    def close_app(self):
        choice = QtWidgets.QMessageBox.question(self, "Quit", "Game Over ?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = MainGame()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1067, 550)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 931, 161))
        self.label.setStyleSheet("font: 38pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 191, 101))
        self.pushButton.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 300, 191, 101))
        self.pushButton_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Kaun Banega Crorepati"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton.clicked.connect(self.startGame)
        self.pushButton_2.setText(_translate("Dialog", "Exit"))

    def startGame(self):

        game = MainGame()
        game.setupUi(Dialog)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
