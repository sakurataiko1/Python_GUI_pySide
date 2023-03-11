# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_CustomWidget(object):
    def setupUi(self, CustomWidget):
        if not CustomWidget.objectName():
            CustomWidget.setObjectName(u"CustomWidget")
        CustomWidget.resize(265, 50)
        self.verticalLayout = QVBoxLayout(CustomWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CustomWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.path = QLineEdit(CustomWidget)
        self.path.setObjectName(u"path")

        self.horizontalLayout.addWidget(self.path)

        self.btn = QToolButton(CustomWidget)
        self.btn.setObjectName(u"btn")

        self.horizontalLayout.addWidget(self.btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CustomWidget)

        QMetaObject.connectSlotsByName(CustomWidget)
    # setupUi

    def retranslateUi(self, CustomWidget):
        CustomWidget.setWindowTitle(QCoreApplication.translate("CustomWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CustomWidget", u"Name", None))
        self.btn.setText(QCoreApplication.translate("CustomWidget", u"...", None))
    # retranslateUi

