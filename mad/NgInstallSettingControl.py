# -*- coding: utf-8 -*-
#Author : Andy
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ng_new_setting_dailog import Ui_ng_new_setting_dialog
from PyQt5.QtWidgets import QMessageBox
import NgNewInstallControl
class NgInstallSettingControl(QtWidgets.QDialog, Ui_ng_new_setting_dialog):
    def __init__(self):
        super(NgInstallSettingControl, self).__init__()
        self.setupUi(self)

        self.nginstall = NgNewInstallControl.NgNewInstallControl()

        #添加事件
        self.nextButton.clicked.connect(self.jump_to_install)

    def jump_to_install(self):
        try:
            self.hide()
            self.nginstall.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开火烈鸟安装页面异常,异常信息为:{}".format(str(e))))