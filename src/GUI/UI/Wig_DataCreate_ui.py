# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wig_DataCreate.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Wig_DataCreate(object):
    def setupUi(self, Wig_DataCreate):
        if not Wig_DataCreate.objectName():
            Wig_DataCreate.setObjectName(u"Wig_DataCreate")
        Wig_DataCreate.resize(400, 519)
        self.gridLayout = QGridLayout(Wig_DataCreate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GCreateProcessGroup = QGroupBox(Wig_DataCreate)
        self.GCreateProcessGroup.setObjectName(u"GCreateProcessGroup")
        font = QFont()
        font.setFamilies([u"Adwaita Sans"])
        font.setPointSize(12)
        font.setItalic(False)
        self.GCreateProcessGroup.setFont(font)
        self.GCreateProcessGroup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.GCreateProcessGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Wig_CreateMenu = QWidget(self.GCreateProcessGroup)
        self.Wig_CreateMenu.setObjectName(u"Wig_CreateMenu")
        self.horizontalLayout = QHBoxLayout(self.Wig_CreateMenu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.WCreateMenuTitle = QWidget(self.Wig_CreateMenu)
        self.WCreateMenuTitle.setObjectName(u"WCreateMenuTitle")
        self.verticalLayout_3 = QVBoxLayout(self.WCreateMenuTitle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.WCreateMenuTitle)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.WCreateMenuTitle)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.WCreateMenuTitle)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.WCreateMenuTitle)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.WCreateMenuTitle)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.WCreateMenuTitle)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.WCreateMenuTitle)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_7.raise_()

        self.horizontalLayout.addWidget(self.WCreateMenuTitle)

        self.Wig_values = QWidget(self.Wig_CreateMenu)
        self.Wig_values.setObjectName(u"Wig_values")
        self.verticalLayout_2 = QVBoxLayout(self.Wig_values)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SpinBoxMaxIoTime = QSpinBox(self.Wig_values)
        self.SpinBoxMaxIoTime.setObjectName(u"SpinBoxMaxIoTime")
        self.SpinBoxMaxIoTime.setMinimum(1)

        self.verticalLayout_2.addWidget(self.SpinBoxMaxIoTime)

        self.SpinBoxMinIoTime = QSpinBox(self.Wig_values)
        self.SpinBoxMinIoTime.setObjectName(u"SpinBoxMinIoTime")
        self.SpinBoxMinIoTime.setMinimum(1)

        self.verticalLayout_2.addWidget(self.SpinBoxMinIoTime)

        self.SpinBoxMaxCpuTime = QSpinBox(self.Wig_values)
        self.SpinBoxMaxCpuTime.setObjectName(u"SpinBoxMaxCpuTime")
        self.SpinBoxMaxCpuTime.setMinimum(1)

        self.verticalLayout_2.addWidget(self.SpinBoxMaxCpuTime)

        self.SpinBoxMinCpuTime = QSpinBox(self.Wig_values)
        self.SpinBoxMinCpuTime.setObjectName(u"SpinBoxMinCpuTime")
        self.SpinBoxMinCpuTime.setMinimum(1)

        self.verticalLayout_2.addWidget(self.SpinBoxMinCpuTime)

        self.SpinBoxProcesNumb = QSpinBox(self.Wig_values)
        self.SpinBoxProcesNumb.setObjectName(u"SpinBoxProcesNumb")
        self.SpinBoxProcesNumb.setMinimum(1)
        self.SpinBoxProcesNumb.setMaximum(10000)

        self.verticalLayout_2.addWidget(self.SpinBoxProcesNumb)

        self.SpinBoxIoBreak = QSpinBox(self.Wig_values)
        self.SpinBoxIoBreak.setObjectName(u"SpinBoxIoBreak")

        self.verticalLayout_2.addWidget(self.SpinBoxIoBreak)

        self.SpinBoxMaxArrivalTime = QSpinBox(self.Wig_values)
        self.SpinBoxMaxArrivalTime.setObjectName(u"SpinBoxMaxArrivalTime")
        self.SpinBoxMaxArrivalTime.setMaximum(1000)

        self.verticalLayout_2.addWidget(self.SpinBoxMaxArrivalTime)


        self.horizontalLayout.addWidget(self.Wig_values)


        self.verticalLayout.addWidget(self.Wig_CreateMenu)

        self.Button_CreateProcess = QPushButton(self.GCreateProcessGroup)
        self.Button_CreateProcess.setObjectName(u"Button_CreateProcess")

        self.verticalLayout.addWidget(self.Button_CreateProcess)


        self.gridLayout.addWidget(self.GCreateProcessGroup, 0, 0, 1, 1)


        self.retranslateUi(Wig_DataCreate)

        QMetaObject.connectSlotsByName(Wig_DataCreate)
    # setupUi

    def retranslateUi(self, Wig_DataCreate):
        Wig_DataCreate.setWindowTitle(QCoreApplication.translate("Wig_DataCreate", u"Form", None))
        self.GCreateProcessGroup.setTitle(QCoreApplication.translate("Wig_DataCreate", u"Process Group Create", None))
        self.label.setText(QCoreApplication.translate("Wig_DataCreate", u"io max time", None))
        self.label_2.setText(QCoreApplication.translate("Wig_DataCreate", u"io min time", None))
        self.label_3.setText(QCoreApplication.translate("Wig_DataCreate", u"cpu max time", None))
        self.label_4.setText(QCoreApplication.translate("Wig_DataCreate", u"cpu min time", None))
        self.label_5.setText(QCoreApplication.translate("Wig_DataCreate", u"process number", None))
        self.label_6.setText(QCoreApplication.translate("Wig_DataCreate", u"io break number", None))
        self.label_7.setText(QCoreApplication.translate("Wig_DataCreate", u"max arrival time", None))
        self.Button_CreateProcess.setText(QCoreApplication.translate("Wig_DataCreate", u"Create Process Group", None))
    # retranslateUi

