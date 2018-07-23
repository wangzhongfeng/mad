# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.wetcatpay_open_dialog import Ui_wetcatpay_open_dialog
from PyQt5.QtWidgets import QMessageBox
class WetcatpayOpenControl(QtWidgets.QDialog, Ui_wetcatpay_open_dialog):
    def __init__(self):
        super(WetcatpayOpenControl, self).__init__()
        self.setupUi(self)