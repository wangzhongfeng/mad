# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_cloud_login_dialog import Ui_check_cloud_login_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckCloudSysLoginControl(QtWidgets.QDialog, Ui_check_cloud_login_dialog):
    def __init__(self):
        super(CheckCloudSysLoginControl, self).__init__()
        self.setupUi(self)