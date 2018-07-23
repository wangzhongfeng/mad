# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_port_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_port_dialog(object):
    def setupUi(self, check_port_dialog):
        check_port_dialog.setObjectName("check_port_dialog")
        check_port_dialog.resize(400, 169)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_port_dialog.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(check_port_dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 218, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget1 = QtWidgets.QWidget(check_port_dialog)
        self.widget1.setGeometry(QtCore.QRect(310, 20, 39, 119))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.one_port_states = QtWidgets.QLabel(self.widget1)
        self.one_port_states.setObjectName("one_port_states")
        self.verticalLayout_2.addWidget(self.one_port_states)
        self.two_port_states = QtWidgets.QLabel(self.widget1)
        self.two_port_states.setObjectName("two_port_states")
        self.verticalLayout_2.addWidget(self.two_port_states)
        self.three_port_states = QtWidgets.QLabel(self.widget1)
        self.three_port_states.setObjectName("three_port_states")
        self.verticalLayout_2.addWidget(self.three_port_states)

        self.retranslateUi(check_port_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_port_dialog)

    def retranslateUi(self, check_port_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_port_dialog.setWindowTitle(_translate("check_port_dialog", "相关端口检测"))
        self.label.setText(_translate("check_port_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">ping 59.252.101.11</span></p></body></html>"))
        self.label_2.setText(_translate("check_port_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">telnet 59.252.101.9 8000</span></p></body></html>"))
        self.label_3.setText(_translate("check_port_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\"> telnet 59.252.101.5 7000</span></p></body></html>"))
        self.one_port_states.setText(_translate("check_port_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.two_port_states.setText(_translate("check_port_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.three_port_states.setText(_translate("check_port_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))

