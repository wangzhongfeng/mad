# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\login_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(317, 239)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_dialog.setWindowIcon(icon)
        self.login_Button = QtWidgets.QPushButton(login_dialog)
        self.login_Button.setGeometry(QtCore.QRect(60, 200, 75, 23))
        self.login_Button.setObjectName("login_Button")
        self.cancle_Button = QtWidgets.QPushButton(login_dialog)
        self.cancle_Button.setGeometry(QtCore.QRect(170, 200, 75, 23))
        self.cancle_Button.setObjectName("cancle_Button")
        self.username_lable = QtWidgets.QLabel(login_dialog)
        self.username_lable.setGeometry(QtCore.QRect(50, 70, 54, 12))
        self.username_lable.setObjectName("username_lable")
        self.password_lable = QtWidgets.QLabel(login_dialog)
        self.password_lable.setGeometry(QtCore.QRect(50, 110, 54, 12))
        self.password_lable.setObjectName("password_lable")
        self.verificationCode_label = QtWidgets.QLabel(login_dialog)
        self.verificationCode_label.setGeometry(QtCore.QRect(50, 150, 54, 12))
        self.verificationCode_label.setObjectName("verificationCode_label")
        self.username_text = QtWidgets.QLineEdit(login_dialog)
        self.username_text.setGeometry(QtCore.QRect(110, 70, 141, 20))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(login_dialog)
        self.password_text.setGeometry(QtCore.QRect(110, 110, 141, 20))
        self.password_text.setObjectName("password_text")
        self.verificationCode_text = QtWidgets.QLineEdit(login_dialog)
        self.verificationCode_text.setGeometry(QtCore.QRect(110, 150, 141, 20))
        self.verificationCode_text.setObjectName("verificationCode_text")
        self.title_lable = QtWidgets.QLabel(login_dialog)
        self.title_lable.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.title_lable.setStyleSheet("font: 75 16pt \"Agency FB\";")
        self.title_lable.setTextFormat(QtCore.Qt.AutoText)
        self.title_lable.setScaledContents(True)
        self.title_lable.setIndent(-1)
        self.title_lable.setObjectName("title_lable")

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)
        login_dialog.setTabOrder(self.username_text, self.password_text)
        login_dialog.setTabOrder(self.password_text, self.verificationCode_text)
        login_dialog.setTabOrder(self.verificationCode_text, self.login_Button)
        login_dialog.setTabOrder(self.login_Button, self.cancle_Button)


    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "登陆"))
        self.login_Button.setText(_translate("login_dialog", "登陆"))
        self.cancle_Button.setText(_translate("login_dialog", "取消"))
        self.username_lable.setText(_translate("login_dialog", "用户名:"))
        self.password_lable.setText(_translate("login_dialog", "密  码:"))
        self.verificationCode_label.setText(_translate("login_dialog", "验证码:"))
        self.title_lable.setText(_translate("login_dialog", "泰久自动化实施工具（MAD）"))
