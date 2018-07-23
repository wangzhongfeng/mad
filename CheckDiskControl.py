# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_disk_dialog import Ui_check_disk_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckDiskControl(QtWidgets.QDialog, Ui_check_disk_dialog):
    def __init__(self):
        super(CheckDiskControl, self).__init__()
        self.setupUi(self)