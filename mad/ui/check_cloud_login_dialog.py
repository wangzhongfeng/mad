# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_cloud_login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_cloud_login_dialog(object):
    def setupUi(self, check_cloud_login_dialog):
        check_cloud_login_dialog.setObjectName("check_cloud_login_dialog")
        check_cloud_login_dialog.resize(337, 255)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_cloud_login_dialog.setWindowIcon(icon)
        self.service_login_states = QtWidgets.QLabel(check_cloud_login_dialog)
        self.service_login_states.setGeometry(QtCore.QRect(200, 200, 54, 31))
        self.service_login_states.setObjectName("service_login_states")
        self.label = QtWidgets.QLabel(check_cloud_login_dialog)
        self.label.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.label.setObjectName("label")
        self.front_login_states = QtWidgets.QLabel(check_cloud_login_dialog)
        self.front_login_states.setGeometry(QtCore.QRect(200, 140, 54, 31))
        self.front_login_states.setObjectName("front_login_states")
        self.label_2 = QtWidgets.QLabel(check_cloud_login_dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 111, 31))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(check_cloud_login_dialog)
        self.line.setGeometry(QtCore.QRect(0, 120, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(check_cloud_login_dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(check_cloud_login_dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(check_cloud_login_dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 41, 16))
        self.label_5.setObjectName("label_5")
        self.tenant_code_text = QtWidgets.QLineEdit(check_cloud_login_dialog)
        self.tenant_code_text.setGeometry(QtCore.QRect(80, 20, 151, 20))
        self.tenant_code_text.setObjectName("tenant_code_text")
        self.username_text = QtWidgets.QLineEdit(check_cloud_login_dialog)
        self.username_text.setGeometry(QtCore.QRect(80, 50, 151, 20))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(check_cloud_login_dialog)
        self.password_text.setGeometry(QtCore.QRect(80, 80, 151, 20))
        self.password_text.setObjectName("password_text")
        self.pushButton = QtWidgets.QPushButton(check_cloud_login_dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(check_cloud_login_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_cloud_login_dialog)

    def retranslateUi(self, check_cloud_login_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_cloud_login_dialog.setWindowTitle(_translate("check_cloud_login_dialog", "检测系统登录(云票务)"))
        self.service_login_states.setText(_translate("check_cloud_login_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))
        self.label.setText(_translate("check_cloud_login_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">前台登录：</span></p></body></html>"))
        self.front_login_states.setText(_translate("check_cloud_login_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.label_2.setText(_translate("check_cloud_login_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">后台登录:</span></p></body></html>"))
        self.label_3.setText(_translate("check_cloud_login_dialog", "租户："))
        self.label_4.setText(_translate("check_cloud_login_dialog", "用户名："))
        self.label_5.setText(_translate("check_cloud_login_dialog", "密码："))
        self.pushButton.setText(_translate("check_cloud_login_dialog", "检测"))

