# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '01-calc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.current_btn = []
        self.result = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 423)
        Dialog.setStyleSheet("background-color: rgb(255, 245, 224);")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 561, 71))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 380, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 380, 51, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 380, 51, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 340, 51, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 340, 51, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 340, 51, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 340, 51, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 300, 51, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 300, 51, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 300, 121, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 300, 71, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(400, 300, 75, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(490, 300, 75, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 350, 71, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(400, 350, 75, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(490, 350, 75, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(150, 250, 121, 41))
        self.pushButton_18.setObjectName("pushButton_18")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "0"))
        self.pushButton_2.setText(_translate("Dialog", "1"))
        self.pushButton_3.setText(_translate("Dialog", "2"))
        self.pushButton_4.setText(_translate("Dialog", "3"))
        self.pushButton_5.setText(_translate("Dialog", "4"))
        self.pushButton_6.setText(_translate("Dialog", "5"))
        self.pushButton_7.setText(_translate("Dialog", "6"))
        self.pushButton_8.setText(_translate("Dialog", "7"))
        self.pushButton_9.setText(_translate("Dialog", "8"))
        self.pushButton_10.setText(_translate("Dialog", "9"))
        self.pushButton_11.setText(_translate("Dialog", "Clear"))
        self.pushButton_12.setText(_translate("Dialog", "+"))
        self.pushButton_13.setText(_translate("Dialog", "-"))
        self.pushButton_14.setText(_translate("Dialog", "*"))
        self.pushButton_15.setText(_translate("Dialog", "/"))
        self.pushButton_16.setText(_translate("Dialog", "%"))
        self.pushButton_17.setText(_translate("Dialog", "sqrt"))
        self.pushButton_18.setText(_translate("Dialog", "="))

        self.pushButton_18.clicked.connect(self.calculate)

        self.pushButton_11.clicked.connect(self.clear_box)


        self.operand_list = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                       self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
                       self.pushButton_9, self.pushButton_10, self.pushButton_12, self.pushButton_13, self.pushButton_14,
                       self.pushButton_15, self.pushButton_16, self.pushButton_17]

        # self.operator_list = [self.pushButton_12, self.pushButton_13, self.pushButton_14,
        #                       self.pushButton_15, self.pushButton_16, self.pushButton_17]

        for i in range(len(self.operand_list)):
            self.operand_list[i].clicked.connect(self.set_operand)

        # for j in range(len(self.operator_list)):
        #     self.operator_list[j].clicked.connect(self.do_operation)



    def set_operand(self):

        self.current_btn.append(self.sender())
        # print(self.current_btn)
        self.lineEdit.clear()

        # self.current_btnValue = self.current_btn.text()
        # self.lineEdit.setText(str(self.current_btnValue))
        for t in self.current_btn:
            # print(t.text())
            self.lineEdit.setText(self.lineEdit.text() + t.text())


        # self.clicked_btn = self.sender()
        # btnValue = int(self.clicked_btn.text())
        #
        # if self.wait:
        #     self.lineEdit.clear()
        #     self.wait = False
        #
        # self.lineEdit.setText(self.lineEdit.text() + str(btnValue))

    def clear_box(self):

        self.current_operator = self.sender()

        self.lineEdit.clear()
        self.lineEdit.setText("")
        self.current_btn = []

    def calculate(self):
        self.result = eval(self.lineEdit.text())
        print(self.result)
        # print(self.lineEdit.text())
        # print(type(self.lineEdit.text()))
        self.lineEdit.setText(str(self.result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

