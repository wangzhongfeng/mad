# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_disk_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_disk_dialog(object):
    def setupUi(self, check_disk_dialog):
        check_disk_dialog.setObjectName("check_disk_dialog")
        check_disk_dialog.resize(288, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_disk_dialog.setWindowIcon(icon)
        self.read_disk_states = QtWidgets.QLabel(check_disk_dialog)
        self.read_disk_states.setGeometry(QtCore.QRect(220, 20, 54, 31))
        self.read_disk_states.setObjectName("read_disk_states")
        self.write_disk_states = QtWidgets.QLabel(check_disk_dialog)
        self.write_disk_states.setGeometry(QtCore.QRect(220, 80, 54, 31))
        self.write_disk_states.setObjectName("write_disk_states")
        self.label_6 = QtWidgets.QLabel(check_disk_dialog)
        self.label_6.setGeometry(QtCore.QRect(290, 130, 54, 31))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(check_disk_dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 87, 161))
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
        self.widget1 = QtWidgets.QWidget(check_disk_dialog)
        self.widget1.setGeometry(QtCore.QRect(120, 20, 56, 161))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.read_disk_value = QtWidgets.QLabel(self.widget1)
        self.read_disk_value.setObjectName("read_disk_value")
        self.verticalLayout_2.addWidget(self.read_disk_value)
        self.write_disk_value = QtWidgets.QLabel(self.widget1)
        self.write_disk_value.setObjectName("write_disk_value")
        self.verticalLayout_2.addWidget(self.write_disk_value)
        self.healthy_states = QtWidgets.QLabel(self.widget1)
        self.healthy_states.setObjectName("healthy_states")
        self.verticalLayout_2.addWidget(self.healthy_states)

        self.retranslateUi(check_disk_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_disk_dialog)

    def retranslateUi(self, check_disk_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_disk_dialog.setWindowTitle(_translate("check_disk_dialog", "服务器磁盘检测"))
        self.read_disk_states.setText(_translate("check_disk_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.write_disk_states.setText(_translate("check_disk_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))
        self.label_6.setText(_translate("check_disk_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.label.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">读速度：</span></p></body></html>"))
        self.label_2.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">写速度：</span></p></body></html>"))
        self.label_3.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">健康状况：</span></p></body></html>"))
        self.read_disk_value.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">100M/s</span></p></body></html>"))
        self.write_disk_value.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">100M/s</span></p></body></html>"))
        self.healthy_states.setText(_translate("check_disk_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">良好</span></p></body></html>"))
