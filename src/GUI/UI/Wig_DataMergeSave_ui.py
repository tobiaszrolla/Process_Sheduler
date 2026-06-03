# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wig_DataMergeSave.ui'
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
from PySide6.QtWidgets import (QApplication, QListView, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Wig_DataMergeSave(object):
    def setupUi(self, Wig_DataMergeSave):
        if not Wig_DataMergeSave.objectName():
            Wig_DataMergeSave.setObjectName(u"Wig_DataMergeSave")
        Wig_DataMergeSave.resize(400, 483)
        self.verticalLayout = QVBoxLayout(Wig_DataMergeSave)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.View_ProcessGroups = QListView(Wig_DataMergeSave)
        self.View_ProcessGroups.setObjectName(u"View_ProcessGroups")

        self.verticalLayout.addWidget(self.View_ProcessGroups)

        self.BMerge = QPushButton(Wig_DataMergeSave)
        self.BMerge.setObjectName(u"BMerge")

        self.verticalLayout.addWidget(self.BMerge)

        self.BSaveJSON = QPushButton(Wig_DataMergeSave)
        self.BSaveJSON.setObjectName(u"BSaveJSON")

        self.verticalLayout.addWidget(self.BSaveJSON)


        self.retranslateUi(Wig_DataMergeSave)

        QMetaObject.connectSlotsByName(Wig_DataMergeSave)
    # setupUi

    def retranslateUi(self, Wig_DataMergeSave):
        Wig_DataMergeSave.setWindowTitle(QCoreApplication.translate("Wig_DataMergeSave", u"Form", None))
        self.BMerge.setText(QCoreApplication.translate("Wig_DataMergeSave", u"Merge", None))
        self.BSaveJSON.setText(QCoreApplication.translate("Wig_DataMergeSave", u"Save", None))
    # retranslateUi

