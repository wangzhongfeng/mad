# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_cloud_uk_connect_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_cloud_uk_connect_dialog(object):
    def setupUi(self, check_cloud_uk_connect_dialog):
        check_cloud_uk_connect_dialog.setObjectName("check_cloud_uk_connect_dialog")
        check_cloud_uk_connect_dialog.resize(221, 97)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_cloud_uk_connect_dialog.setWindowIcon(icon)
        self.check_uk_dialog = QtWidgets.QLabel(check_cloud_uk_connect_dialog)
        self.check_uk_dialog.setGeometry(QtCore.QRect(50, 20, 81, 41))
        self.check_uk_dialog.setObjectName("check_uk_dialog")
        self.uk_connect_states = QtWidgets.QLabel(check_cloud_uk_connect_dialog)
        self.uk_connect_states.setGeometry(QtCore.QRect(140, 20, 54, 41))
        self.uk_connect_states.setObjectName("uk_connect_states")

        self.retranslateUi(check_cloud_uk_connect_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_cloud_uk_connect_dialog)

    def retranslateUi(self, check_cloud_uk_connect_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_cloud_uk_connect_dialog.setWindowTitle(_translate("check_cloud_uk_connect_dialog", "UK连接检测(云票务)"))
        self.check_uk_dialog.setText(_translate("check_cloud_uk_connect_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">UK连接：</span></p></body></html>"))
        self.uk_connect_states.setText(_translate("check_cloud_uk_connect_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))