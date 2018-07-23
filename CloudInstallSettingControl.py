# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.cloud_new_setting_dialog import Ui_cloud_new_setting_dialog
from PyQt5.QtWidgets import QMessageBox
import CloudInstallControl
class CloudInstallSettingControl(QtWidgets.QDialog, Ui_cloud_new_setting_dialog):
    def __init__(self):
        super(CloudInstallSettingControl, self).__init__()
        self.setupUi(self)

        self.cloudinstall= CloudInstallControl.CloudInstallControl()

        #添加事件
        self.nextButton.clicked.connect(self.jump_to_install)

    def jump_to_install(self):
        try:
            self.hide()
            self.cloudinstall.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开云票务安装页面异常,异常信息为:{}".format(str(e))))