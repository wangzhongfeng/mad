# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.alipay_open_dialog import Ui_alipay_open_dialog
from PyQt5.QtWidgets import QMessageBox
class AliPayOpenControl(QtWidgets.QDialog, Ui_alipay_open_dialog):
    def __init__(self):
        super(AliPayOpenControl, self).__init__()
        self.setupUi(self)