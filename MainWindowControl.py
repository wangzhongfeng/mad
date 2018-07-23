# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\02.售后服务\运维\自动化部署资料\页面UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import NgInstallSettingControl
import NgDataTranSettingControl
import CloudInstallSettingControl
import CloudDataTransferSetControl
import GetPkcodeControl
class MainWindowControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowControl, self).__init__()
        self.setupUi(self)
        self.installSetting = NgInstallSettingControl.NgInstallSettingControl()
        self.dataTransferSetting = NgDataTranSettingControl.NgDataTranSettingControl()
        self.coludInstallSet = CloudInstallSettingControl.CloudInstallSettingControl()
        self.clouddataTranSet = CloudDataTransferSetControl.CloudDataTransferSetControl()

        #添加事件
        self.ng_install_Button.clicked.connect(self.jump_to_install_setting)
        self.data_transfer_Button.clicked.connect(self.jump_to_dataTran_setting)
        self.ng_cloud_Button.clicked.connect(self.jump_to_cloud_install)
        self.ng_cloud_cut_Button.clicked.connect(self.jump_to_cloudDataTran_set)


    def jump_to_install_setting(self):
        try:
            self.installSetting.show()
        except Exception as e:
         QMessageBox.critical(self,"异常",self.tr("打开火烈鸟安装设置页面异常,异常信息为:{}".format(str(e))))

    def jump_to_dataTran_setting(self):
        try:
            self.dataTransferSetting.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开火烈鸟数据迁移设置页面异常,异常信息为:{}".format(str(e))))

    def jump_to_cloud_install(self):
        try:
            self.coludInstallSet.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开云票务安装设置页面异常,异常信息为:{}".format(str(e))))

    def jump_to_cloudDataTran_set(self):
        try:
            self.clouddataTranSet.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开云票务数据迁移设置页面异常,异常信息为:{}".format(str(e))))