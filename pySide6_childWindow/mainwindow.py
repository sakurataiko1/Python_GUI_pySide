# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

#from PySide2.QtWidgets import QApplication, QWidget
#from PySide2.QtCore import QFile
#from PySide2.QtUiTools import QUiLoader

from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Ui_MainWindow import Ui_MainWindow

# -start- childWIndow
from Ui_SubDialog1 import Ui_SubDialog1
from SubDialog1 import SubDialog1
# -end- childWIndow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # -start- add myk
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.popup_dlg = None

        # フォームと動作の関連付け
        self.ui.pushButton_1.clicked.connect(self.func_on_pushButton_1_clicked)

    def func_on_pushButton_1_clicked(self):
        print("[DEBUG]func_on_pushButton_1_clicked")
        # self.ui.lineEdit_DEBUG1.setText("test_lineEdit01")
        #subWindow = SubDialog1  # サブウィンドウの作成
        #subWindow.show(self)  # サブウィンドウの表示

        self.popup_dlg = SubDialog1() # サブウィンドウの作成 & 表示


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
