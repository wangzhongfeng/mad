# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\ng_data_transfer_dailog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_ng_data_transfer_dailog(object):
    def setupUi(self, ng_data_transfer_dailog):
        ng_data_transfer_dailog.setObjectName("ng_data_transfer_dailog")
        ng_data_transfer_dailog.resize(1077, 818)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ng_data_transfer_dailog.setWindowIcon(icon)
        self.fromObj = ng_data_transfer_dailog
        # self.webView = QtWebKitWidgets.QWebView(ng_data_transfer_dailog)
        # self.webView.setGeometry(QtCore.QRect(0, 100, 1071, 711))
        # self.webView.setUrl(QtCore.QUrl("http://localhost:8080/html/index.html"))
        # self.webView.setObjectName("webView")
        # self.browser = QWebEngineView(ng_data_transfer_dailog)
        # url = 'https://www.baidu.com'
        # self.browser.load(QUrl(url))
        # self.browser.setGeometry(QtCore.QRect(0, 100, 1071, 711))
        # self.browser.setObjectName("browser")
        self.tempdb_name_label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.tempdb_name_label.setGeometry(QtCore.QRect(350, 70, 41, 16))
        self.tempdb_name_label.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"text-decoration: underline;")
        self.tempdb_name_label.setObjectName("tempdb_name_label")
        self.label_5 = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label_5.setGeometry(QtCore.QRect(400, 70, 61, 16))
        self.label_5.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label_5.setObjectName("label_5")
        self.tempdb_pwd_label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.tempdb_pwd_label.setGeometry(QtCore.QRect(540, 70, 41, 16))
        self.tempdb_pwd_label.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"text-decoration: underline;")
        self.tempdb_pwd_label.setObjectName("tempdb_pwd_label")
        self.tempdb_port_label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.tempdb_port_label.setGeometry(QtCore.QRect(260, 70, 31, 16))
        self.tempdb_port_label.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"text-decoration: underline;")
        self.tempdb_port_label.setObjectName("tempdb_port_label")
        self.tempdb_username_label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.tempdb_username_label.setGeometry(QtCore.QRect(460, 70, 31, 16))
        self.tempdb_username_label.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"text-decoration: underline;")
        self.tempdb_username_label.setObjectName("tempdb_username_label")
        self.label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label.setGeometry(QtCore.QRect(20, 10, 661, 31))
        self.label.setStyleSheet("font: 75 20pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label_6.setGeometry(QtCore.QRect(500, 70, 61, 16))
        self.label_6.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label_7.setGeometry(QtCore.QRect(310, 70, 41, 16))
        self.label_7.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")
        self.tempdb_ip_label = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.tempdb_ip_label.setGeometry(QtCore.QRect(130, 70, 81, 16))
        self.tempdb_ip_label.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
"text-decoration: underline;")
        self.tempdb_ip_label.setObjectName("tempdb_ip_label")
        self.label_4 = QtWidgets.QLabel(ng_data_transfer_dailog)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 41, 16))
        self.label_4.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ng_data_transfer_dailog)
        QtCore.QMetaObject.connectSlotsByName(ng_data_transfer_dailog)

    def retranslateUi(self, ng_data_transfer_dailog):
        _translate = QtCore.QCoreApplication.translate
        ng_data_transfer_dailog.setWindowTitle(_translate("ng_data_transfer_dailog", "数据迁移"))
        self.tempdb_name_label.setText(_translate("ng_data_transfer_dailog", "SCTS"))
        self.label_5.setText(_translate("ng_data_transfer_dailog", "用户名："))
        self.tempdb_pwd_label.setText(_translate("ng_data_transfer_dailog", "ngV523"))
        self.tempdb_port_label.setText(_translate("ng_data_transfer_dailog", "3306"))
        self.tempdb_username_label.setText(_translate("ng_data_transfer_dailog", "root"))
        self.label.setText(_translate("ng_data_transfer_dailog", "深圳泰久电影院（88888888）"))
        self.label_6.setText(_translate("ng_data_transfer_dailog", "密码："))
        self.label_7.setText(_translate("ng_data_transfer_dailog", "库名："))
        self.label_3.setText(_translate("ng_data_transfer_dailog", "火烈鸟数据库IP："))
        self.tempdb_ip_label.setText(_translate("ng_data_transfer_dailog", "192.169.112.346"))
        self.label_4.setText(_translate("ng_data_transfer_dailog", "端口："))


