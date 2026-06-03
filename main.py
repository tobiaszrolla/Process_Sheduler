import sys
from PySide6.QtWidgets import QApplication

from src.GUI.Wig_Run import Wig_Run
from src.GUI.Wig_DataPrep import Wig_DataPrep
from src.GUI.MainWindow import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())