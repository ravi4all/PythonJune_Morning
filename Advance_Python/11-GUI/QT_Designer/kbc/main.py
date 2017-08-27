# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import pygame
import threading
import time
import datetime

pygame.mixer.init()
bg_sound = pygame.mixer.Sound('sound_2.wav')
bg_sound.play(-1)

optionLock = pygame.mixer.Sound('optionLock.wav')

class Ui_Dialog(object):

    def __init__(self):

        self.timeLeft = 60

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(952, 695)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 961, 701))
        self.frame.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 925, 695))
        pixmap = QPixmap("kbc_.png")
        self.label_img.setPixmap(pixmap)

        # self.label = QtWidgets.QLabel(self.frame)
        # self.label.setGeometry(QtCore.QRect(170, 160, 621, 121))
        # self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        # self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(170, 480, 161, 81))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 480, 161, 81))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 951, 701))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")


        self.label_timer = QtWidgets.QLabel(self.frame_2)
        self.label_timer.setGeometry(QtCore.QRect(40, 100, 261, 81))
        self.label_timer.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_timer.setObjectName("label_timer")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 300, 661, 81))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 430, 171, 71))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 430, 171, 71))
        self.pushButton_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 550, 171, 71))
        self.pushButton_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 550, 171, 71))
        self.pushButton_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")

        self.frame_2.hide()

        btns = [self.pushButton_3, self.pushButton_4, self.pushButton_5,
                self.pushButton_6]

        for i in range(len(btns)):
            btns[i].clicked.connect(self.checkAns)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def timer(self):
        for t in range(60):
            self.timeLeft -= 1
            time.sleep(1)
            print(self.timeLeft)
            self.label_timer.setText("Time Left : "+str(self.timeLeft))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.label.setText(_translate("Dialog", "Kaun Banega Crorepati"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Exit"))
        # self.label_timer.setText(_translate("Dialog", "Time Left {}".format(self.timeLeft)))
        self.label_2.setText(_translate("Dialog", "Who is the prime minister of India ?"))
        self.pushButton_3.setText(_translate("Dialog", "Modi"))
        self.pushButton_4.setText(_translate("Dialog", "Yogi"))
        self.pushButton_5.setText(_translate("Dialog", "Arvind"))
        self.pushButton_6.setText(_translate("Dialog", "Lalu"))

        self.pushButton.clicked.connect(self.startGame)


    def startGame(self):
        self.frame_2.show()
        bg_sound.stop()
        t2.start()

    def checkAns(self):
        optionLock.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    t1 = threading.Timer(3, ui.startGame)
    t1.start()
    t2 = threading.Thread(target=ui.timer)
    # t2.start()
    Dialog.show()
    sys.exit(app.exec_())

