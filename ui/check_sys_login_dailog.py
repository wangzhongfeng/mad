# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_sys_login_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_ng_login_dialog(object):
    def setupUi(self, check_ng_login_dialog):
        check_ng_login_dialog.setObjectName("check_ng_login_dialog")
        check_ng_login_dialog.resize(314, 142)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_ng_login_dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(check_ng_login_dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(check_ng_login_dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 111, 31))
        self.label_2.setObjectName("label_2")
        self.front_login_states = QtWidgets.QLabel(check_ng_login_dialog)
        self.front_login_states.setGeometry(QtCore.QRect(190, 20, 54, 31))
        self.front_login_states.setObjectName("front_login_states")
        self.service_login_states = QtWidgets.QLabel(check_ng_login_dialog)
        self.service_login_states.setGeometry(QtCore.QRect(190, 80, 54, 31))
        self.service_login_states.setObjectName("service_login_states")

        self.retranslateUi(check_ng_login_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_ng_login_dialog)

    def retranslateUi(self, check_ng_login_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_ng_login_dialog.setWindowTitle(_translate("check_ng_login_dialog", "检测系统登录（火烈鸟）"))
        self.label.setText(_translate("check_ng_login_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">前台登录：</span></p></body></html>"))
        self.label_2.setText(_translate("check_ng_login_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">后台登录:</span></p></body></html>"))
        self.front_login_states.setText(_translate("check_ng_login_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.service_login_states.setText(_translate("check_ng_login_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))
