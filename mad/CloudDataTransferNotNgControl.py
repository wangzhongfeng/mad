# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.cloud_data_cut_notng_dialog import Ui_cloud_data_cut_notng_dialog
from PyQt5.QtWidgets import QMessageBox
import NgDataToolStartControl
class CloudDataTransferNotNgControl(QtWidgets.QDialog, Ui_cloud_data_cut_notng_dialog):
    def __init__(self):
        super(CloudDataTransferNotNgControl, self).__init__()
        self.setupUi(self)

        self.datatoolstart = NgDataToolStartControl.NgDataToolStartControl()

        #添加事件
        self.open_datatool_button.clicked.connect(self.jump_to_datatoolstart)

    def jump_to_datatoolstart(self):
        try:
            self.datatoolstart.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开火烈鸟数据工具启动页面异常,异常信息为:{}".format(str(e))))
