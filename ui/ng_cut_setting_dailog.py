# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\ng_cut_setting_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ng_cut_setting_dailog(object):
    def setupUi(self, ng_cut_setting_dailog):
        ng_cut_setting_dailog.setObjectName("ng_cut_setting_dailog")
        ng_cut_setting_dailog.resize(306, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ng_cut_setting_dailog.setWindowIcon(icon)
        self.label_3 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 80, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label.setGeometry(QtCore.QRect(40, 120, 54, 21))
        self.label.setObjectName("label")
        self.password_text = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.password_text.setGeometry(QtCore.QRect(100, 280, 151, 20))
        self.password_text.setObjectName("password_text")
        self.label_2 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 41, 21))
        self.label_2.setObjectName("label_2")
        self.username_text = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.username_text.setGeometry(QtCore.QRect(100, 240, 151, 20))
        self.username_text.setObjectName("username_text")
        self.label_7 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 54, 16))
        self.label_7.setObjectName("label_7")
        self.nextButton = QtWidgets.QPushButton(ng_cut_setting_dailog)
        self.nextButton.setGeometry(QtCore.QRect(160, 350, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.closeButton = QtWidgets.QPushButton(ng_cut_setting_dailog)
        self.closeButton.setGeometry(QtCore.QRect(50, 350, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.label_4 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_4.setGeometry(QtCore.QRect(100, 140, 151, 16))
        self.label_4.setStyleSheet("font: 8pt \"Agency FB\";\n"
"color:red;")
        self.label_4.setObjectName("label_4")
        self.serverip_text = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.serverip_text.setGeometry(QtCore.QRect(100, 120, 151, 20))
        self.serverip_text.setObjectName("serverip_text")
        self.lineEdit_2 = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 40, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_8.setGeometry(QtCore.QRect(40, 80, 54, 21))
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_13.setGeometry(QtCore.QRect(130, 10, 54, 21))
        self.label_13.setObjectName("label_13")
        self.username_text_2 = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.username_text_2.setGeometry(QtCore.QRect(100, 160, 151, 20))
        self.username_text_2.setObjectName("username_text_2")
        self.label_18 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_18.setGeometry(QtCore.QRect(50, 160, 41, 21))
        self.label_18.setObjectName("label_18")
        self.username_text_3 = QtWidgets.QLineEdit(ng_cut_setting_dailog)
        self.username_text_3.setGeometry(QtCore.QRect(100, 200, 151, 20))
        self.username_text_3.setObjectName("username_text_3")
        self.label_19 = QtWidgets.QLabel(ng_cut_setting_dailog)
        self.label_19.setGeometry(QtCore.QRect(50, 200, 41, 21))
        self.label_19.setObjectName("label_19")

        self.retranslateUi(ng_cut_setting_dailog)
        QtCore.QMetaObject.connectSlotsByName(ng_cut_setting_dailog)

    def retranslateUi(self, ng_cut_setting_dailog):
        _translate = QtCore.QCoreApplication.translate
        ng_cut_setting_dailog.setWindowTitle(_translate("ng_cut_setting_dailog", "火烈鸟数据迁移设置"))
        self.label_3.setText(_translate("ng_cut_setting_dailog", "密   码："))
        self.label.setText(_translate("ng_cut_setting_dailog", "数据库IP："))
        self.password_text.setText(_translate("ng_cut_setting_dailog", "ngV5123"))
        self.label_2.setText(_translate("ng_cut_setting_dailog", "用户名："))
        self.username_text.setText(_translate("ng_cut_setting_dailog", "root"))
        self.label_7.setText(_translate("ng_cut_setting_dailog", "影院名称："))
        self.nextButton.setText(_translate("ng_cut_setting_dailog", "下一步"))
        self.closeButton.setText(_translate("ng_cut_setting_dailog", "关闭"))
        self.label_4.setText(_translate("ng_cut_setting_dailog", "内网IP，如果远程设置VPN地址"))
        self.serverip_text.setText(_translate("ng_cut_setting_dailog", "127.0.0.1"))
        self.label_8.setText(_translate("ng_cut_setting_dailog", "影院编码："))
        self.label_13.setText(_translate("ng_cut_setting_dailog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aa7f;\">火烈鸟</span></p></body></html>"))
        self.username_text_2.setText(_translate("ng_cut_setting_dailog", "SCTS"))
        self.label_18.setText(_translate("ng_cut_setting_dailog", "库名："))
        self.username_text_3.setText(_translate("ng_cut_setting_dailog", "3306"))
        self.label_19.setText(_translate("ng_cut_setting_dailog", "端口："))
