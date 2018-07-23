# -*- coding: utf-8 -*-
#Author : Andy

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ng_cut_setting_dailog import Ui_ng_cut_setting_dailog
from PyQt5.QtWidgets import QMessageBox
import NgDataToolStartControl
class NgDataTranSettingControl(QtWidgets.QDialog, Ui_ng_cut_setting_dailog):
    def __init__(self):
        super(NgDataTranSettingControl, self).__init__()
        self.setupUi(self)

        self.datatoolstart = NgDataToolStartControl.NgDataToolStartControl()

        #添加事件
        self.nextButton.clicked.connect(self.jump_to_datatoolstart)

    def jump_to_datatoolstart(self):
        try:
            self.hide()
            self.datatoolstart.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开火烈鸟数据工具启动页面异常,异常信息为:{}".format(str(e))))
