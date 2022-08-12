# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_SubDialog1.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QSizePolicy,
    QWidget)

class Ui_SubDialog1(object):
    def setupUi(self, SubDialog1):
        if not SubDialog1.objectName():
            SubDialog1.setObjectName(u"SubDialog1")
        SubDialog1.resize(400, 300)
        self.lineEdit = QLineEdit(SubDialog1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 30, 113, 26))

        self.retranslateUi(SubDialog1)

        QMetaObject.connectSlotsByName(SubDialog1)
    # setupUi

    def retranslateUi(self, SubDialog1):
        SubDialog1.setWindowTitle(QCoreApplication.translate("SubDialog1", u"Dialog", None))
    # retranslateUi

