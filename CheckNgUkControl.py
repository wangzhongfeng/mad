# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_uk_connect_dailog import Ui_check_uk_connect_dailog
from PyQt5.QtWidgets import QMessageBox
class CheckNgUkControl(QtWidgets.QDialog, Ui_check_uk_connect_dailog):
    def __init__(self):
        super(CheckNgUkControl, self).__init__()
        self.setupUi(self)