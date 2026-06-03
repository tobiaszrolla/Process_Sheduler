from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from .UI.Wig_run_ui import Ui_Wig_run
from src.models.processList import ProcessList
from src.data_prep.data_load_incoming import loadIncomingData
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.Algorithms import ShedulingAlgorithm, RoundRobinAlgorithm, FCFSalgorithm, SJFalgorithm, LCSFalgorithm

class Wig_Run(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Wig_run()
        self.ui.setupUi(self)
        self.proces_list : ProcessList | None = None

        self.ui.Butt_SourceFile.clicked.connect(
            self.load
        )
        self.ui.Button_Run.clicked.connect(
            self.run
        )

    def load(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
                                                "Save process group",
                                                "process_group.json",
                                                "JSON Files (*.json)"
        )
        file_path = files[0]
        self.proces_list = loadIncomingData(file_path)

    def run(self):
        if self.proces_list is None:
            QMessageBox.warning(self, "Err", "No process loaded")
            return
        algorithm = ShedulingAlgorithm()
        algorithm_name = self.ui.ComboBox_Algorithm.currentText()
        if algorithm_name == 'Round Robin':
            algorithm = RoundRobinAlgorithm(5)
        elif algorithm_name == 'FCFS':
            algorithm = FCFSalgorithm()
        elif algorithm_name == 'LCFS':
            algorithm = LCSFalgorithm()
        elif algorithm_name == 'SJF':
            algorithm = SJFalgorithm()
        

