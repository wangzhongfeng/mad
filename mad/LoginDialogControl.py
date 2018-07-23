# -*- coding: utf-8 -*-
#Author : Andy
from ui.login_dailog import Ui_login_dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import MainWindowControl
import sys

class LoginDialogControl(QtWidgets.QDialog, Ui_login_dialog):
    def __init__(self):
        super(LoginDialogControl, self).__init__()
        self.setupUi(self)

        self.main_window = MainWindowControl.MainWindowControl();

        #添加事件
        self.login_Button.clicked.connect(self.jump_to_main)

    def jump_to_main(self):
        try:
            self.hide()
            self.main_window.show()
        except Exception as e:
            QMessageBox.critical(self,"异常",self.tr("打开主窗口异常,异常信息为:{}".format(str(e))))

    '''
        登录验证
    '''
    def login_erificationv(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = LoginDialogControl()
    mywindow.show()
    sys.exit(app.exec_())