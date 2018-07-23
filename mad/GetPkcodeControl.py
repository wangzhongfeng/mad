# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.get_pkcode_dailog import Ui_ng_pkcode_dialog
from PyQt5.QtWidgets import QMessageBox
class GetPkcodeControl(QtWidgets.QDialog, Ui_ng_pkcode_dialog):
    def __init__(self):
        super(GetPkcodeControl, self).__init__()
        self.setupUi(self)
