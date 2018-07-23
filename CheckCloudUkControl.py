# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.check_cloud_uk_connect_dialog import Ui_check_cloud_uk_connect_dialog
from PyQt5.QtWidgets import QMessageBox
class CheckCloudUkControl(QtWidgets.QDialog, Ui_check_cloud_uk_connect_dialog):
    def __init__(self):
        super(CheckCloudUkControl, self).__init__()
        self.setupUi(self)