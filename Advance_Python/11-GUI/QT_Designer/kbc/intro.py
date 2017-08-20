# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import game

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(865, 550)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 731, 161))
        self.label.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";")
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

        gameObj = game.MainGame()
        gameObj.setupUi(Dialog)
        print("Game Started")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

