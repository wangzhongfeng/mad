# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\cloud_new_setting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cloud_new_setting_dialog(object):
    def setupUi(self, cloud_new_setting_dialog):
        cloud_new_setting_dialog.setObjectName("cloud_new_setting_dialog")
        cloud_new_setting_dialog.resize(327, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cloud_new_setting_dialog.setWindowIcon(icon)
        self.ciname_code_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.ciname_code_text.setGeometry(QtCore.QRect(110, 60, 151, 20))
        self.ciname_code_text.setObjectName("ciname_code_text")
        self.label_3 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label.setGeometry(QtCore.QRect(50, 140, 54, 21))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 54, 12))
        self.label_5.setObjectName("label_5")
        self.port_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.port_text.setGeometry(QtCore.QRect(110, 180, 151, 20))
        self.port_text.setObjectName("port_text")
        self.password_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.password_text.setGeometry(QtCore.QRect(110, 250, 151, 20))
        self.password_text.setObjectName("password_text")
        self.delaytime_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.delaytime_text.setEnabled(True)
        self.delaytime_text.setGeometry(QtCore.QRect(190, 300, 51, 20))
        self.delaytime_text.setDragEnabled(False)
        self.delaytime_text.setClearButtonEnabled(False)
        self.delaytime_text.setObjectName("delaytime_text")
        self.label_2 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 41, 21))
        self.label_2.setObjectName("label_2")
        self.username_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.username_text.setGeometry(QtCore.QRect(110, 220, 151, 20))
        self.username_text.setObjectName("username_text")
        self.radioButton_2 = QtWidgets.QRadioButton(cloud_new_setting_dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 300, 51, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_9 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 180, 41, 21))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 54, 16))
        self.label_7.setObjectName("label_7")
        self.nextButton = QtWidgets.QPushButton(cloud_new_setting_dialog)
        self.nextButton.setGeometry(QtCore.QRect(190, 350, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.closeButton = QtWidgets.QPushButton(cloud_new_setting_dialog)
        self.closeButton.setGeometry(QtCore.QRect(80, 350, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.serverip_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.serverip_text.setGeometry(QtCore.QRect(110, 140, 151, 20))
        self.serverip_text.setObjectName("serverip_text")
        self.radioButton = QtWidgets.QRadioButton(cloud_new_setting_dialog)
        self.radioButton.setGeometry(QtCore.QRect(80, 300, 51, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.ciname_name_text = QtWidgets.QLineEdit(cloud_new_setting_dialog)
        self.ciname_name_text.setGeometry(QtCore.QRect(110, 20, 151, 20))
        self.ciname_name_text.setObjectName("ciname_name_text")
        self.label_8 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 60, 54, 21))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(250, 300, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(cloud_new_setting_dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 71, 21))
        self.label_4.setObjectName("label_4")
        self.os_type_select = QtWidgets.QComboBox(cloud_new_setting_dialog)
        self.os_type_select.setGeometry(QtCore.QRect(110, 100, 151, 22))
        self.os_type_select.setObjectName("os_type_select")
        self.os_type_select.addItem("")
        self.os_type_select.addItem("")

        self.retranslateUi(cloud_new_setting_dialog)
        QtCore.QMetaObject.connectSlotsByName(cloud_new_setting_dialog)

    def retranslateUi(self, cloud_new_setting_dialog):
        _translate = QtCore.QCoreApplication.translate
        cloud_new_setting_dialog.setWindowTitle(_translate("cloud_new_setting_dialog", "云票务新装设置"))
        self.label_3.setText(_translate("cloud_new_setting_dialog", "密   码："))
        self.label.setText(_translate("cloud_new_setting_dialog", "服务器IP："))
        self.label_5.setText(_translate("cloud_new_setting_dialog", "触发时间："))
        self.port_text.setText(_translate("cloud_new_setting_dialog", "36566"))
        self.label_2.setText(_translate("cloud_new_setting_dialog", "用户名："))
        self.username_text.setText(_translate("cloud_new_setting_dialog", "root"))
        self.radioButton_2.setText(_translate("cloud_new_setting_dialog", "定时"))
        self.label_9.setText(_translate("cloud_new_setting_dialog", "端口："))
        self.label_7.setText(_translate("cloud_new_setting_dialog", "影院名称："))
        self.nextButton.setText(_translate("cloud_new_setting_dialog", "下一步"))
        self.closeButton.setText(_translate("cloud_new_setting_dialog", "关闭"))
        self.serverip_text.setText(_translate("cloud_new_setting_dialog", "127.0.0.1"))
        self.radioButton.setText(_translate("cloud_new_setting_dialog", "立即"))
        self.label_8.setText(_translate("cloud_new_setting_dialog", "影院编码："))
        self.label_6.setText(_translate("cloud_new_setting_dialog", "分钟后执行"))
        self.label_4.setText(_translate("cloud_new_setting_dialog", "服务器类型："))
        self.os_type_select.setItemText(0, _translate("cloud_new_setting_dialog", "linux"))
        self.os_type_select.setItemText(1, _translate("cloud_new_setting_dialog", "window"))

