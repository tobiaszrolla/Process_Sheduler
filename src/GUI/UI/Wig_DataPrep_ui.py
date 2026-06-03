# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wig_DataPrep.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QWidget)

from .MyWigets import (Wig_DataCreate, Wig_DataMergeSave)

class Ui_Wig_DataPrep(object):
    def setupUi(self, Wig_DataPrep):
        if not Wig_DataPrep.objectName():
            Wig_DataPrep.setObjectName(u"Wig_DataPrep")
        Wig_DataPrep.resize(807, 584)
        self.horizontalLayout = QHBoxLayout(Wig_DataPrep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.wig_create = Wig_DataCreate(Wig_DataPrep)
        self.wig_create.setObjectName(u"wig_create")

        self.horizontalLayout.addWidget(self.wig_create)

        self.wig_merge_save = Wig_DataMergeSave(Wig_DataPrep)
        self.wig_merge_save.setObjectName(u"wig_merge_save")

        self.horizontalLayout.addWidget(self.wig_merge_save)


        self.retranslateUi(Wig_DataPrep)

        QMetaObject.connectSlotsByName(Wig_DataPrep)
    # setupUi

    def retranslateUi(self, Wig_DataPrep):
        Wig_DataPrep.setWindowTitle(QCoreApplication.translate("Wig_DataPrep", u"Form", None))
    # retranslateUi

