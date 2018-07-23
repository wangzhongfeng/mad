# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.cloud_new_dailog import Ui_cloud_new_dailog
from PyQt5.QtWidgets import QMessageBox
class CloudInstallControl(QtWidgets.QDialog, Ui_cloud_new_dailog):
    def __init__(self):
        super(CloudInstallControl, self).__init__()
        self.setupUi(self)