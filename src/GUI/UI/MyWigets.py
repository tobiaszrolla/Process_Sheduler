from .Wig_DataCreate_ui import Ui_Wig_DataCreate
from .Wig_DataMergeSave_ui import Ui_Wig_DataMergeSave
from PySide6.QtWidgets import QWidget
from .Wig_run_ui import Ui_Wig_run

class Wig_DataCreate(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Wig_DataCreate()
        self.ui.setupUi(self)

class Wig_DataMergeSave(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Wig_DataMergeSave()
        self.ui.setupUi(self)

class Wig_run(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Wig_run()
        self.ui.setupUi(self)

