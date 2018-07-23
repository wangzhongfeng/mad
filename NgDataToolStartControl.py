# -*- coding: utf-8 -*-
#Author : Andy
import this

from PyQt5 import QtCore, QtGui, QtWidgets

from ui.ng_data_tool_start_dailog import Ui_ng_data_tool_start_dailog
from PyQt5.QtWidgets import QMessageBox
import NgDataTransferControl
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class NgDataToolStartControl(QtWidgets.QDialog, Ui_ng_data_tool_start_dailog):
    def __init__(self):
        super(NgDataToolStartControl, self).__init__()
        self.setupUi(self)

        self.datatransfer = NgDataTransferControl.NgDataTransferControl()

        #添加事件
        self.next_Button.clicked.connect(self.jump_to_datatransfer)

    def jump_to_datatransfer(self):
        try:
            self.hide()
            self.datatransfer.browser = QWebEngineView(self.datatransfer.fromObj)
            url = 'https://www.baidu.com'
            self.datatransfer.browser.load(QUrl(url))
            self.datatransfer.browser.setGeometry(QtCore.QRect(0, 100, 1071, 711))
            self.datatransfer.browser.setObjectName("browser")
            self.datatransfer.show()
        except Exception as e:
             QMessageBox.critical(self,"异常",self.tr("打开火烈鸟数据工具启动页面异常,异常信息为:{}".format(str(e))))
