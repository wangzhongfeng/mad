# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\alipay_open_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alipay_open_dialog(object):
    def setupUi(self, alipay_open_dialog):
        alipay_open_dialog.setObjectName("alipay_open_dialog")
        alipay_open_dialog.resize(400, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        alipay_open_dialog.setWindowIcon(icon)
        self.message_info_label = QtWidgets.QLabel(alipay_open_dialog)
        self.message_info_label.setGeometry(QtCore.QRect(20, 500, 54, 12))
        self.message_info_label.setObjectName("message_info_label")
        self.open_Button = QtWidgets.QPushButton(alipay_open_dialog)
        self.open_Button.setGeometry(QtCore.QRect(120, 430, 75, 23))
        self.open_Button.setObjectName("open_Button")
        self.layoutWidget = QtWidgets.QWidget(alipay_open_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 10, 201, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.appid_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.appid_text.setObjectName("appid_text")
        self.verticalLayout_2.addWidget(self.appid_text)
        self.appSecet_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.appSecet_text.setObjectName("appSecet_text")
        self.verticalLayout_2.addWidget(self.appSecet_text)
        self.bussion_code_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.bussion_code_text.setObjectName("bussion_code_text")
        self.verticalLayout_2.addWidget(self.bussion_code_text)
        self.secret_key_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.secret_key_text.setObjectName("secret_key_text")
        self.verticalLayout_2.addWidget(self.secret_key_text)
        self.certficate_file = QtWidgets.QLineEdit(self.layoutWidget)
        self.certficate_file.setObjectName("certficate_file")
        self.verticalLayout_2.addWidget(self.certficate_file)
        self.public_acc_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.public_acc_text.setObjectName("public_acc_text")
        self.verticalLayout_2.addWidget(self.public_acc_text)
        self.public_pwd_text = QtWidgets.QLineEdit(self.layoutWidget)
        self.public_pwd_text.setObjectName("public_pwd_text")
        self.verticalLayout_2.addWidget(self.public_pwd_text)
        self.layoutWidget_2 = QtWidgets.QWidget(alipay_open_dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 10, 134, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.line = QtWidgets.QFrame(alipay_open_dialog)
        self.line.setGeometry(QtCore.QRect(-10, 470, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 250, 351, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 280, 351, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 310, 351, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 340, 351, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 370, 351, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(alipay_open_dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 400, 351, 16))
        self.checkBox_6.setObjectName("checkBox_6")

        self.retranslateUi(alipay_open_dialog)
        QtCore.QMetaObject.connectSlotsByName(alipay_open_dialog)

    def retranslateUi(self, alipay_open_dialog):
        _translate = QtCore.QCoreApplication.translate
        alipay_open_dialog.setWindowTitle(_translate("alipay_open_dialog", "开通支付宝支付"))
        self.message_info_label.setText(_translate("alipay_open_dialog", "开通成功"))
        self.open_Button.setText(_translate("alipay_open_dialog", "开通"))
        self.label.setText(_translate("alipay_open_dialog", "商户Partnerid（PID"))
        self.label_2.setText(_translate("alipay_open_dialog", "RSA密钥（PKCS8编码）"))
        self.label_3.setText(_translate("alipay_open_dialog", "RSA公钥"))
        self.label_4.setText(_translate("alipay_open_dialog", "支付宝账号"))
        self.label_5.setText(_translate("alipay_open_dialog", "安全校验码(Key)"))
        self.label_6.setText(_translate("alipay_open_dialog", "支付宝公钥"))
        self.label_7.setText(_translate("alipay_open_dialog", "Appid"))
        self.checkBox.setText(_translate("alipay_open_dialog", "当面付service:alipay.acquire.precreate"))
        self.checkBox_2.setText(_translate("alipay_open_dialog", "对账"))
        self.checkBox_3.setText(_translate("alipay_open_dialog", "WAP：alipay.wap.create.direct.pay.by.user"))
        self.checkBox_4.setText(_translate("alipay_open_dialog", "退款"))
        self.checkBox_5.setText(_translate("alipay_open_dialog", "支付宝WEB：create_direct_pay_by_user"))
        self.checkBox_6.setText(_translate("alipay_open_dialog", "支付宝APP：mobile.securitypay.pay"))
