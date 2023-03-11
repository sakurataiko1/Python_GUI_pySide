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

from Ui_MainWindow import Ui_MainWindow  # myk add

from Ui_CustomWidget import Ui_CustomWidget  # myk add
from CustomWidget import CustomWidget  # myk add

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_DEBUG01.setText("DEBUG_abc")

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
