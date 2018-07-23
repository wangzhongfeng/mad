# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_port_dialog import Ui_check_port_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckPortControl(QtWidgets.QDialog, Ui_check_port_dialog):
    def __init__(self):
        super(CheckPortControl, self).__init__()
        self.setupUi(self)