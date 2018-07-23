# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.global_setting_dailog import Ui_global_setting_dialog
from PyQt5.QtWidgets import QMessageBox
class GlobalSetControl(QtWidgets.QDialog, Ui_global_setting_dialog):
    def __init__(self):
        super(GlobalSetControl, self).__init__()
        self.setupUi(self)