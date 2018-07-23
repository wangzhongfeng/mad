# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ng_data_transfer_dailog import Ui_ng_data_transfer_dailog
from PyQt5.QtWidgets import QMessageBox
class NgDataTransferControl(QtWidgets.QDialog, Ui_ng_data_transfer_dailog):
    def __init__(self):
        super(NgDataTransferControl, self).__init__()
        self.setupUi(self)