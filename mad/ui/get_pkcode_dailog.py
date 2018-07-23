# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\get_pkcode_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ng_pkcode_dialog(object):
    def setupUi(self, ng_pkcode_dialog):
        ng_pkcode_dialog.setObjectName("ng_pkcode_dialog")
        ng_pkcode_dialog.resize(418, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ng_pkcode_dialog.setWindowIcon(icon)
        self.serverip_text = QtWidgets.QLineEdit(ng_pkcode_dialog)
        self.serverip_text.setGeometry(QtCore.QRect(90, 20, 101, 20))
        self.serverip_text.setObjectName("serverip_text")
        self.label_3 = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 51, 21))
        self.label_3.setObjectName("label_3")
        self.username_text = QtWidgets.QLineEdit(ng_pkcode_dialog)
        self.username_text.setGeometry(QtCore.QRect(90, 60, 191, 20))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(ng_pkcode_dialog)
        self.password_text.setGeometry(QtCore.QRect(90, 100, 191, 20))
        self.password_text.setObjectName("password_text")
        self.label = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 54, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 31, 21))
        self.label_4.setObjectName("label_4")
        self.serverip_text_2 = QtWidgets.QLineEdit(ng_pkcode_dialog)
        self.serverip_text_2.setGeometry(QtCore.QRect(230, 20, 51, 20))
        self.serverip_text_2.setObjectName("serverip_text_2")
        self.pushButton = QtWidgets.QPushButton(ng_pkcode_dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(ng_pkcode_dialog)
        self.line.setGeometry(QtCore.QRect(0, 130, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 54, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ng_pkcode_dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 81, 21))
        self.label_6.setObjectName("label_6")
        self.pkcode_label_value = QtWidgets.QLabel(ng_pkcode_dialog)
        self.pkcode_label_value.setGeometry(QtCore.QRect(100, 160, 301, 21))
        self.pkcode_label_value.setObjectName("pkcode_label_value")
        self.netcode_label_value = QtWidgets.QLabel(ng_pkcode_dialog)
        self.netcode_label_value.setGeometry(QtCore.QRect(100, 200, 301, 21))
        self.netcode_label_value.setObjectName("netcode_label_value")

        self.retranslateUi(ng_pkcode_dialog)
        QtCore.QMetaObject.connectSlotsByName(ng_pkcode_dialog)

    def retranslateUi(self, ng_pkcode_dialog):
        _translate = QtCore.QCoreApplication.translate
        ng_pkcode_dialog.setWindowTitle(_translate("ng_pkcode_dialog", "获取PK码和网络账号"))
        self.serverip_text.setText(_translate("ng_pkcode_dialog", "127.0.0.1"))
        self.label_3.setText(_translate("ng_pkcode_dialog", "密   码："))
        self.username_text.setText(_translate("ng_pkcode_dialog", "root"))
        self.password_text.setText(_translate("ng_pkcode_dialog", "taijiu,.2018"))
        self.label.setText(_translate("ng_pkcode_dialog", "服务器IP："))
        self.label_2.setText(_translate("ng_pkcode_dialog", "用户名："))
        self.label_4.setText(_translate("ng_pkcode_dialog", "端口："))
        self.serverip_text_2.setText(_translate("ng_pkcode_dialog", "36566"))
        self.pushButton.setText(_translate("ng_pkcode_dialog", "获取"))
        self.label_5.setText(_translate("ng_pkcode_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">PK码：</span></p></body></html>"))
        self.label_6.setText(_translate("ng_pkcode_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">网络账号：</span></p></body></html>"))
        self.pkcode_label_value.setText(_translate("ng_pkcode_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">3e0fafffb2e110331251df6c4a579244</span></p></body></html>"))
        self.netcode_label_value.setText(_translate("ng_pkcode_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">221805020001</span></p></body></html>"))
