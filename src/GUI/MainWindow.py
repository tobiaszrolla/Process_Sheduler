from .UI.MainWindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from src.GUI.Wig_Run import Wig_Run
from src.GUI.Wig_DataPrep import Wig_DataPrep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.run_widget = Wig_Run()
        self.data_widget = Wig_DataPrep()

        self.ui.stackedWidget.addWidget(self.run_widget)
        self.ui.stackedWidget.addWidget(self.data_widget)

        self.ui.stackedWidget.setCurrentWidget(self.run_widget)

        self.ui.actionCreator.triggered.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.data_widget)
        )

        self.ui.actionRunner.triggered.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.run_widget)
        )


