# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\check_cloud_all_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_cloud_all_dialog(object):
    def setupUi(self, check_cloud_all_dialog):
        check_cloud_all_dialog.setObjectName("check_cloud_all_dialog")
        check_cloud_all_dialog.resize(502, 637)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        check_cloud_all_dialog.setWindowIcon(icon)
        self.label_5 = QtWidgets.QLabel(check_cloud_all_dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(check_cloud_all_dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(check_cloud_all_dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 41, 16))
        self.label_3.setObjectName("label_3")
        self.password_text = QtWidgets.QLineEdit(check_cloud_all_dialog)
        self.password_text.setGeometry(QtCore.QRect(90, 70, 151, 20))
        self.password_text.setObjectName("password_text")
        self.username_text = QtWidgets.QLineEdit(check_cloud_all_dialog)
        self.username_text.setGeometry(QtCore.QRect(90, 40, 151, 20))
        self.username_text.setObjectName("username_text")
        self.pushButton = QtWidgets.QPushButton(check_cloud_all_dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tenant_code_text = QtWidgets.QLineEdit(check_cloud_all_dialog)
        self.tenant_code_text.setGeometry(QtCore.QRect(90, 10, 151, 20))
        self.tenant_code_text.setObjectName("tenant_code_text")
        self.line = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line.setGeometry(QtCore.QRect(0, 110, 501, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.write_disk_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.write_disk_states.setGeometry(QtCore.QRect(420, 510, 41, 31))
        self.write_disk_states.setObjectName("write_disk_states")
        self.line_2 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 220, 501, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.front_login_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.front_login_states.setGeometry(QtCore.QRect(420, 180, 41, 41))
        self.front_login_states.setObjectName("front_login_states")
        self.two_port_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.two_port_states.setGeometry(QtCore.QRect(420, 350, 37, 31))
        self.two_port_states.setObjectName("two_port_states")
        self.read_disk_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.read_disk_states.setGeometry(QtCore.QRect(420, 460, 41, 31))
        self.read_disk_states.setObjectName("read_disk_states")
        self.write_disk_value = QtWidgets.QLabel(check_cloud_all_dialog)
        self.write_disk_value.setGeometry(QtCore.QRect(280, 490, 54, 49))
        self.write_disk_value.setObjectName("write_disk_value")
        self.layoutWidget = QtWidgets.QWidget(check_cloud_all_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 218, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_uk_dialog = QtWidgets.QLabel(self.layoutWidget)
        self.check_uk_dialog.setObjectName("check_uk_dialog")
        self.verticalLayout.addWidget(self.check_uk_dialog)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.three_port_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.three_port_states.setGeometry(QtCore.QRect(420, 400, 37, 41))
        self.three_port_states.setObjectName("three_port_states")
        self.line_8 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_8.setGeometry(QtCore.QRect(0, 550, 511, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_5 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 380, 511, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_3 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 160, 501, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.read_disk_value = QtWidgets.QLabel(check_cloud_all_dialog)
        self.read_disk_value.setGeometry(QtCore.QRect(280, 440, 54, 49))
        self.read_disk_value.setObjectName("read_disk_value")
        self.line_4 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 330, 501, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.service_login_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.service_login_states.setGeometry(QtCore.QRect(420, 240, 54, 41))
        self.service_login_states.setObjectName("service_login_states")
        self.one_port_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.one_port_states.setGeometry(QtCore.QRect(420, 300, 37, 41))
        self.one_port_states.setObjectName("one_port_states")
        self.line_6 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_6.setGeometry(QtCore.QRect(0, 280, 501, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.uk_connect_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.uk_connect_states.setGeometry(QtCore.QRect(420, 130, 41, 31))
        self.uk_connect_states.setObjectName("uk_connect_states")
        self.healthy_states = QtWidgets.QLabel(check_cloud_all_dialog)
        self.healthy_states.setGeometry(QtCore.QRect(280, 550, 54, 49))
        self.healthy_states.setObjectName("healthy_states")
        self.line_7 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_7.setGeometry(QtCore.QRect(0, 440, 501, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_9 = QtWidgets.QFrame(check_cloud_all_dialog)
        self.line_9.setGeometry(QtCore.QRect(0, 490, 501, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.retranslateUi(check_cloud_all_dialog)
        QtCore.QMetaObject.connectSlotsByName(check_cloud_all_dialog)

    def retranslateUi(self, check_cloud_all_dialog):
        _translate = QtCore.QCoreApplication.translate
        check_cloud_all_dialog.setWindowTitle(_translate("check_cloud_all_dialog", "全部检测(云票务)"))
        self.label_5.setText(_translate("check_cloud_all_dialog", "密码："))
        self.label_4.setText(_translate("check_cloud_all_dialog", "用户名："))
        self.label_3.setText(_translate("check_cloud_all_dialog", "租户："))
        self.pushButton.setText(_translate("check_cloud_all_dialog", "检测"))
        self.write_disk_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))
        self.front_login_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.two_port_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.read_disk_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.write_disk_value.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">100M/s</span></p></body></html>"))
        self.check_uk_dialog.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">UK连接：</span></p></body></html>"))
        self.label.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">前台登录：</span></p></body></html>"))
        self.label_2.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">后台登录:</span></p></body></html>"))
        self.label_6.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">ping 59.252.101.11</span></p></body></html>"))
        self.label_7.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">telnet 59.252.101.9 8000</span></p></body></html>"))
        self.label_8.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\"> telnet 59.252.101.5 7000</span></p></body></html>"))
        self.label_9.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">读速度：</span></p></body></html>"))
        self.label_10.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">写速度：</span></p></body></html>"))
        self.label_11.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">健康状况：</span></p></body></html>"))
        self.three_port_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.read_disk_value.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">100M/s</span></p></body></html>"))
        self.service_login_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/cuo.png\"/></p></body></html>"))
        self.one_port_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.uk_connect_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><img src=\"res/duihao.png\"/></p></body></html>"))
        self.healthy_states.setText(_translate("check_cloud_all_dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">良好</span></p></body></html>"))