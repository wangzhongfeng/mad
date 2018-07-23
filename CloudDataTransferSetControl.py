# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.cloud_data_cut_setting_dialog import Ui_cloud_data_cut_setting_dialog
from PyQt5.QtWidgets import QMessageBox
import CloudDataTransferNgControl
import CloudDataTransferNotNgControl
class CloudDataTransferSetControl(QtWidgets.QDialog, Ui_cloud_data_cut_setting_dialog):
    def __init__(self):
        super(CloudDataTransferSetControl, self).__init__()
        self.setupUi(self)

        self.dataTransferNg=CloudDataTransferNgControl.CloudDataTransferNgControl()
        self.dataTransferNotNg = CloudDataTransferNotNgControl.CloudDataTransferNotNgControl()

        #添加事件
        self.nextButton.clicked.connect(self.jump_to_dataTransfer)
        self.ng_radioButton.toggled.connect(self.select_ng_radio)
        self.not_ng_radioButton.toggled.connect(self.select_notng_radio)

    def jump_to_dataTransfer(self):
        try:
            self.hide()
            if self.ng_radioButton.isChecked():
                self.dataTransferNg.show()
            elif self.not_ng_radioButton.isChecked():
                self.dataTransferNotNg.show()
            else:
                QMessageBox.critical(self,"提醒",self.tr("请选择数据源类型".format(str(e))))
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开云票务数据迁移页面异常,异常信息为:{}".format(str(e))))

    def select_ng_radio(self):
        self.label_5.show()
        self.label_6.show()
        self.label_7.show()
        self.label_18.show()
        self.label_19.show()
        self.serverip_text.show()
        self.dbname_text.show()
        self.port_text.show()
        self.username_text.show()
        self.password_text.show()
        self.label_8.show()
    def select_notng_radio(self):
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_18.hide()
        self.label_19.hide()
        self.serverip_text.hide()
        self.dbname_text.hide()
        self.port_text.hide()
        self.username_text.hide()
        self.password_text.hide()
        self.label_8.hide()