# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
import sys

class register(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 422)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userButton = QtWidgets.QPushButton(Dialog)
        self.userButton.setGeometry(QtCore.QRect(180, 360, 131, 25))
        self.userButton.setObjectName("userButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 81, 17))
        self.label_4.setObjectName("label_4")
        self.emailText = QtWidgets.QTextEdit(Dialog)
        self.emailText.setGeometry(QtCore.QRect(150, 100, 211, 31))
        self.emailText.setObjectName("emailText")
        self.userText = QtWidgets.QTextEdit(Dialog)
        self.userText.setGeometry(QtCore.QRect(150, 160, 211, 31))
        self.userText.setObjectName("userText")
        self.passwordText = QtWidgets.QTextEdit(Dialog)
        self.passwordText.setGeometry(QtCore.QRect(150, 220, 211, 31))
        self.passwordText.setObjectName("passwordText")
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(200, 280, 89, 25))
        self.registerButton.setObjectName("registerButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 320, 331, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.registerButton.clicked.connect(self.register)
        self.userButton.clicked.connect(self.gotoLogin)

    def register(self):
        try:
            con = sqlite3.connect("database.db")
            cursor = con.cursor()
            email = self.emailText.toPlainText()
            username = self.userText.toPlainText()
            password = self.passwordText.toPlainText()

            insert_command = """INSERT INTO register(Email, Username, Password) VALUES(?, ?, ?);"""
            data_truple = (email, username, password)
            cursor.execute(insert_command, data_truple)
            self.label_5.setText("Successfully Registered !")

            cursor.close()

        except sqlite3.Error as e:
            self.label_5.setText("Failed to Register")
        finally:
            if con:
                con.close()
                print("COnnection closed")


    def gotoLoin(self):
        login =


    def login(self):
        print()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Register"))
        self.userButton.setText(_translate("Dialog", "Already an user"))
        self.label_2.setText(_translate("Dialog", "Email :"))
        self.label_3.setText(_translate("Dialog", "Username: "))
        self.label_4.setText(_translate("Dialog", "Password :"))
        self.registerButton.setText(_translate("Dialog", "Register"))


class login(QDialog):
    def __init__(self):
        loadUI()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

app = QApplication(sys.argv)
mainwindow = register()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()