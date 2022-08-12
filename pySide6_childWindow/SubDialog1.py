# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtCore import QFile
# from PySide6.QtUiTools import QUiLoader

from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from Ui_SubDialog1 import Ui_SubDialog1

class SubDialog1(QDialog, Ui_SubDialog1):
    def __init__(self):
        #super().__init__()
        super(SubDialog1, self).__init__()
        self.ui = Ui_SubDialog1()
        self.ui.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.resize(200, 100)
        self.show()
