# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\ng_data_tool_start_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ng_data_tool_start_dailog(object):
    def setupUi(self, ng_data_tool_start_dailog):
        ng_data_tool_start_dailog.setObjectName("ng_data_tool_start_dailog")
        ng_data_tool_start_dailog.resize(272, 151)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qrc/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ng_data_tool_start_dailog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(ng_data_tool_start_dailog)
        self.label.setGeometry(QtCore.QRect(20, 30, 231, 41))
        self.label.setObjectName("label")
        self.next_Button = QtWidgets.QPushButton(ng_data_tool_start_dailog)
        self.next_Button.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.next_Button.setObjectName("next_Button")

        self.retranslateUi(ng_data_tool_start_dailog)
        QtCore.QMetaObject.connectSlotsByName(ng_data_tool_start_dailog)

    def retranslateUi(self, ng_data_tool_start_dailog):
        _translate = QtCore.QCoreApplication.translate
        ng_data_tool_start_dailog.setWindowTitle(_translate("ng_data_tool_start_dailog", "数据迁移工具启动"))
        self.label.setText(_translate("ng_data_tool_start_dailog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">正在启动迁移工具,请稍等...</span></p></body></html>"))
        self.next_Button.setText(_translate("ng_data_tool_start_dailog", "下一步"))
