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
import GetNgPkcodeControl
import GetCloudPkcodeControl
import QMainWindow
import CheckCloudUkControl
import CheckNgUkControl
import CheckNgSysLoginControl
import CheckCloudSysLoginControl
import CheckPortControl
import CheckDiskControl
import CheckNgAllControl
import CheckCloudAllControl
import AliPayOpenControl
import WetcatpayOpenControl
import GlobalSetControl
class MainWindowControl(QMainWindow.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowControl, self).__init__()
        self.setupUi(self)
        self.installSetting = NgInstallSettingControl.NgInstallSettingControl()
        self.dataTransferSetting = NgDataTranSettingControl.NgDataTranSettingControl()
        self.coludInstallSet = CloudInstallSettingControl.CloudInstallSettingControl()
        self.clouddataTranSet = CloudDataTransferSetControl.CloudDataTransferSetControl()
        self.getngpkcode = GetNgPkcodeControl.GetPkcodeControl()
        self.getcloudpkcode = GetCloudPkcodeControl.GetCloudPkcodeControl()
        self.checknguk=CheckNgUkControl.CheckNgUkControl()
        self.checkclouduk = CheckCloudUkControl.CheckCloudUkControl()
        self.checknglogin = CheckNgSysLoginControl.CheckNgSysLoginControl()
        self.checkcloudlogin = CheckCloudSysLoginControl.CheckCloudSysLoginControl()
        self.checkport = CheckPortControl.CheckPortControl()
        self.checkdisk = CheckDiskControl.CheckDiskControl()
        self.checkngall =CheckNgAllControl.CheckNgAllControl()
        self.checkcloudall = CheckCloudAllControl.CheckCloudAllControl()
        self.alipayopen = AliPayOpenControl.AliPayOpenControl()
        self.weichatopen = WetcatpayOpenControl.WetcatpayOpenControl()
        self.globalset=GlobalSetControl.GlobalSetControl()
        #添加事件
        self.ng_install_Button.clicked.connect(self.jump_to_install_setting)
        self.data_transfer_Button.clicked.connect(self.jump_to_dataTran_setting)
        self.ng_cloud_Button.clicked.connect(self.jump_to_cloud_install)
        self.ng_cloud_cut_Button.clicked.connect(self.jump_to_cloudDataTran_set)
        self.ng_getpk_action.triggered.connect(self.jump_to_ngPkCode)
        self.cloud_getpk_action.triggered.connect(self.jump_to_cloudPkCode)
        self.ng_check_uk_action.triggered.connect(self.jump_to_nguk)
        self.cloud_check_uk_action.triggered.connect(self.jump_to_clouduk)
        self.ng_check_login_action.triggered.connect(self.jump_to_nglogin)
        self.cloud_check_login_action.triggered.connect(self.jump_to_cloudlogin)
        self.check_port_action.triggered.connect(self.jump_to_checkport)
        self.check_disk_action.triggered.connect(self.jump_to_checkdisk)
        self.ng_check_all_action.triggered.connect(self.jump_to_checkngall)
        self.cloud_check_all_action.triggered.connect(self.jump_to_checkcloudall)
        self.open_aipay_action.triggered.connect(self.jump_to_alipay)
        self.open_weichat_action.triggered.connect(self.jump_to_weicatpay)
        self.global_set_action.triggered.connect(self.jump_to_globalset)
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

    def jump_to_ngPkCode(self):
        try:
            self.getngpkcode.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开获取火烈鸟Pk信息页面异常,异常信息为:{}".format(str(e))))

    def jump_to_cloudPkCode(self):
        try:
            self.getcloudpkcode.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开获取云票务Pk信息页面异常,异常信息为:{}".format(str(e))))

    def jump_to_nguk(self):
        try:
            self.checknguk.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试火烈鸟Uk连接页面异常,异常信息为:{}".format(str(e))))
    def jump_to_clouduk(self):
        try:
            self.checkclouduk.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试云票务Uk连接页面异常,异常信息为:{}".format(str(e))))

    def jump_to_nglogin(self):
        try:
            self.checknglogin.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试火烈鸟登陆页面异常,异常信息为:{}".format(str(e))))
    def jump_to_cloudlogin(self):
        try:
            self.checkcloudlogin.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试云票务登陆页面异常,异常信息为:{}".format(str(e))))
    def jump_to_checkport(self):
        try:
            self.checkport.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试端口页面异常,异常信息为:{}".format(str(e))))
    def jump_to_checkdisk(self):
        try:
            self.checkdisk.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开测试硬件页面异常,异常信息为:{}".format(str(e))))
    def jump_to_checkngall(self):
        try:
            self.checkngall.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开火烈鸟所有测试页面异常,异常信息为:{}".format(str(e))))
    def jump_to_checkcloudall(self):
        try:
            self.checkcloudall.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开云票务所有测试页面异常,异常信息为:{}".format(str(e))))
    def jump_to_alipay(self):
        try:
            self.alipayopen.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开支付宝开通页面异常,异常信息为:{}".format(str(e))))
    def jump_to_weicatpay(self):
        try:
            self.weichatopen.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开微信开通页面异常,异常信息为:{}".format(str(e))))
    def jump_to_globalset(self):
        try:
            self.globalset.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开全局设置页面异常,异常信息为:{}".format(str(e))))