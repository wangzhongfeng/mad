# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_uk_connect_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_uk_connect_dailog(object):
    def setupUi(self, check_uk_connect_dailog):
        check_uk_connect_dailog.setObjectName("check_uk_connect_dailog")
        check_uk_connect_dailog.resize(220, 115)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_uk_connect_dailog.setWindowIcon(icon)
        self.check_uk_dialog = QtWidgets.QLabel(check_uk_connect_dailog)
        self.check_uk_dialog.setGeometry(QtCore.QRect(40, 30, 81, 41))
        self.check_uk_dialog.setObjectName("check_uk_dialog")
        self.uk_connect_states = QtWidgets.QLabel(check_uk_connect_dailog)
        self.uk_connect_states.setGeometry(QtCore.QRect(130, 30, 54, 41))
        self.uk_connect_states.setObjectName("uk_connect_states")

        self.retranslateUi(check_uk_connect_dailog)
        QtCore.QMetaObject.connectSlotsByName(check_uk_connect_dailog)

    def retranslateUi(self, check_uk_connect_dailog):
        _translate = QtCore.QCoreApplication.translate
        check_uk_connect_dailog.setWindowTitle(_translate("check_uk_connect_dailog", "UK连接检测"))
        self.check_uk_dialog.setText(_translate("check_uk_connect_dailog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">UK连接：</span></p></body></html>"))
        self.uk_connect_states.setText(_translate("check_uk_connect_dailog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))

