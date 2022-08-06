# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 実行
        self.ui.pushButton1.clicked.connect(self.func_on_pushButton1_clicked)


    def func_on_pushButton1_clicked(self):
        self.ui.lineEdit1.setText("test_lineEdit01")
        self.ui.label1.setText("test01")


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
