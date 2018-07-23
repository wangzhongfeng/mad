# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.cloud_data_cut_ng_dialog import Ui_cloud_data_cut_ng_dialog
from PyQt5.QtWidgets import QMessageBox
class CloudDataTransferNgControl(QtWidgets.QDialog, Ui_cloud_data_cut_ng_dialog):
    def __init__(self):
        super(CloudDataTransferNgControl, self).__init__()
        self.setupUi(self)