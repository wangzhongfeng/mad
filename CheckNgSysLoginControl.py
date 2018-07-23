# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_sys_login_dailog import Ui_check_ng_login_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckNgSysLoginControl(QtWidgets.QDialog, Ui_check_ng_login_dialog):
    def __init__(self):
        super(CheckNgSysLoginControl, self).__init__()
        self.setupUi(self)