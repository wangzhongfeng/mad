# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_all_dialog import Ui_check_ng_all_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckNgAllControl(QtWidgets.QDialog, Ui_check_ng_all_dialog):
    def __init__(self):
        super(CheckNgAllControl, self).__init__()
        self.setupUi(self)