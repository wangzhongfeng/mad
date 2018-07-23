# -*- coding: utf-8 -*-
#Author : Andy
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ng_new_dailog import Ui_ng_new_dialog
class NgNewInstallControl(QtWidgets.QDialog, Ui_ng_new_dialog):
    def __init__(self):
        super(NgNewInstallControl, self).__init__()
        self.setupUi(self)
