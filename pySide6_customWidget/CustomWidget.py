# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# -start- カスタムWidget
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide6.QtWidgets import QApplication, QWidget
CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
# -end- カスタムWidget

from Ui_CustomWidget import Ui_CustomWidget  # myk add

# カスタムWidget
class CustomWidget(QtWidgets.QWidget):

    def __init__(self, title =None, path=None, parent=None):
        super(CustomWidget, self).__init__(parent)

        self.ui = Ui_CustomWidget()
        self.ui.setupUi(self)

        # シグナルスロット
        self.ui.btn.clicked.connect(self.func_on_btn_clicked)

        # [DEBUG] self.ui.path.setText("DEBUG01 test")

    def func_on_btn_clicked(self):
        self.func_setPath()

    def func_setPath(self):
        path = QtWidgets.QFileDialog().getExistingDirectory()
        if path != "":
            self.ui.path.setText(path)


