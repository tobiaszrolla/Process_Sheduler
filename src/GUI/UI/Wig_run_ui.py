# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wig_run.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Wig_run(object):
    def setupUi(self, Wig_run):
        if not Wig_run.objectName():
            Wig_run.setObjectName(u"Wig_run")
        Wig_run.resize(828, 536)
        self.verticalLayout_3 = QVBoxLayout(Wig_run)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(Wig_run)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ComboBox_Algorithm = QComboBox(self.widget_2)
        self.ComboBox_Algorithm.addItem("")
        self.ComboBox_Algorithm.addItem("")
        self.ComboBox_Algorithm.addItem("")
        self.ComboBox_Algorithm.addItem("")
        self.ComboBox_Algorithm.setObjectName(u"ComboBox_Algorithm")

        self.verticalLayout_2.addWidget(self.ComboBox_Algorithm)

        self.SpinBox_StartTime = QSpinBox(self.widget_2)
        self.SpinBox_StartTime.setObjectName(u"SpinBox_StartTime")

        self.verticalLayout_2.addWidget(self.SpinBox_StartTime)

        self.SpinBox_finishTime = QSpinBox(self.widget_2)
        self.SpinBox_finishTime.setObjectName(u"SpinBox_finishTime")

        self.verticalLayout_2.addWidget(self.SpinBox_finishTime)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget = QWidget(Wig_run)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Butt_SourceFile = QPushButton(self.widget)
        self.Butt_SourceFile.setObjectName(u"Butt_SourceFile")

        self.horizontalLayout.addWidget(self.Butt_SourceFile)

        self.Button_Run = QPushButton(self.widget)
        self.Button_Run.setObjectName(u"Button_Run")

        self.horizontalLayout.addWidget(self.Button_Run)

        self.Button_Save = QPushButton(self.widget)
        self.Button_Save.setObjectName(u"Button_Save")

        self.horizontalLayout.addWidget(self.Button_Save)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(Wig_run)

        QMetaObject.connectSlotsByName(Wig_run)
    # setupUi

    def retranslateUi(self, Wig_run):
        Wig_run.setWindowTitle(QCoreApplication.translate("Wig_run", u"Form", None))
        self.label.setText(QCoreApplication.translate("Wig_run", u"Algorithm", None))
        self.label_2.setText(QCoreApplication.translate("Wig_run", u"Start Time", None))
        self.label_3.setText(QCoreApplication.translate("Wig_run", u"Finish Time", None))
        self.ComboBox_Algorithm.setItemText(0, QCoreApplication.translate("Wig_run", u"Round Robin", None))
        self.ComboBox_Algorithm.setItemText(1, QCoreApplication.translate("Wig_run", u"FCFS", None))
        self.ComboBox_Algorithm.setItemText(2, QCoreApplication.translate("Wig_run", u"LCFS", None))
        self.ComboBox_Algorithm.setItemText(3, QCoreApplication.translate("Wig_run", u"SJF", None))

        self.Butt_SourceFile.setText(QCoreApplication.translate("Wig_run", u"Source File", None))
        self.Button_Run.setText(QCoreApplication.translate("Wig_run", u"Run", None))
        self.Button_Save.setText(QCoreApplication.translate("Wig_run", u"Save", None))
    # retranslateUi

