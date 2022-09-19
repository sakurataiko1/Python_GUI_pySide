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

        # スライダー　小数点対応(QSliderは整数しか対応していない。小数にも対応できるようにする)
        self.ui.lineEdit1.editingFinished.connect(self.func_on_lineEdit1_editingFinished)
        self.ui.slider1.valueChanged.connect(self.func_on_slider1_valueChanged)

        #　GUIフォーム初期値
        self.ui.slider1.setMinimum(1)
        self.ui.slider1.setMaximum(1000)

    def func_on_slider1_valueChanged(self):
        # スライダーは0以下数値を扱えないので、小数点以下にも対応できるように換算
        keta = -1 * 3
        value = self.ui.slider1.value()
        real_value = value * (pow(10, keta)) #round(value * (pow(10, -3)), 3)
        str_value = "%0.*f" % (abs(keta), real_value)
        # テキストボックスに値を入れる (lineEdit にしているので valueChangedにループはしない)
        self.ui.lineEdit1.setText(str_value)
        #　print("[DEBUG]01 MainWindow.py-func_on_slider1_valueChanged value=", value, " real_value=", real_value, " textBox=" , self.ui.lineEdit1.text())

    def func_on_lineEdit1_editingFinished(self):
        #print("[DEBUG]01 MainWindow.py-func_on_model1_editingFinished\n")
        keta = 3
        value = float(self.ui.lineEdit1.text())
        self.ui.slider1.setValue(int(value * 10 ** keta)) # スライダーは0以下数値を扱えないので、小数点以下にも対応できるように換算

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
