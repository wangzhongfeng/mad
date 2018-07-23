# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\global_setting_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_global_setting_dialog(object):
    def setupUi(self, global_setting_dialog):
        global_setting_dialog.setObjectName("global_setting_dialog")
        global_setting_dialog.resize(299, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        global_setting_dialog.setWindowIcon(icon)
        self.ciname_code_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.ciname_code_text.setGeometry(QtCore.QRect(100, 60, 151, 20))
        self.ciname_code_text.setObjectName("ciname_code_text")
        self.label_7 = QtWidgets.QLabel(global_setting_dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 54, 16))
        self.label_7.setObjectName("label_7")
        self.ciname_name_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.ciname_name_text.setGeometry(QtCore.QRect(100, 20, 151, 20))
        self.ciname_name_text.setObjectName("ciname_name_text")
        self.serverip_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.serverip_text.setGeometry(QtCore.QRect(100, 100, 151, 20))
        self.serverip_text.setObjectName("serverip_text")
        self.label_3 = QtWidgets.QLabel(global_setting_dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 51, 21))
        self.label_3.setObjectName("label_3")
        self.username_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.username_text.setGeometry(QtCore.QRect(100, 170, 151, 20))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.password_text.setGeometry(QtCore.QRect(100, 210, 151, 20))
        self.password_text.setObjectName("password_text")
        self.label_8 = QtWidgets.QLabel(global_setting_dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 60, 54, 21))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(global_setting_dialog)
        self.label.setGeometry(QtCore.QRect(40, 100, 54, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(global_setting_dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 41, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(global_setting_dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(global_setting_dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 41, 21))
        self.label_5.setObjectName("label_5")
        self.port_text = QtWidgets.QLineEdit(global_setting_dialog)
        self.port_text.setGeometry(QtCore.QRect(100, 140, 151, 20))
        self.port_text.setObjectName("port_text")

        self.retranslateUi(global_setting_dialog)
        QtCore.QMetaObject.connectSlotsByName(global_setting_dialog)

    def retranslateUi(self, global_setting_dialog):
        _translate = QtCore.QCoreApplication.translate
        global_setting_dialog.setWindowTitle(_translate("global_setting_dialog", "服务器远程设置"))
        self.label_7.setText(_translate("global_setting_dialog", "影院名称："))
        self.serverip_text.setText(_translate("global_setting_dialog", "127.0.0.1"))
        self.label_3.setText(_translate("global_setting_dialog", "密   码："))
        self.username_text.setText(_translate("global_setting_dialog", "root"))
        self.label_8.setText(_translate("global_setting_dialog", "影院编码："))
        self.label.setText(_translate("global_setting_dialog", "服务器IP："))
        self.label_2.setText(_translate("global_setting_dialog", "用户名："))
        self.pushButton.setText(_translate("global_setting_dialog", "确定"))
        self.label_5.setText(_translate("global_setting_dialog", "端口："))
        self.port_text.setText(_translate("global_setting_dialog", "36566"))
