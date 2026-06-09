from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from .UI.Wig_run_ui import Ui_Wig_run
from src.models.processList import ProcessList
from src.data_prep.data_load_incoming import loadIncomingData
from src.engin.sheduling_engin import ShedulingEngin
from src.algorithm.Algorithms import ShedulingAlgorithm, RoundRobinAlgorithm, FCFSalgorithm, SJFalgorithm, LCSFalgorithm
from src.engin.calculate_metrics import CalculateMetrics
from src.results.save_raw_result import saveRawResult
from src.results.save_raw_metrics import saveRawMetrics
from copy import deepcopy

class Wig_Run(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Wig_run()
        self.ui.setupUi(self)
        self.proces_list : ProcessList | None = None
        self.metrics : CalculateMetrics | None = None
        self.original_process_list : ProcessList

        self.ui.Butt_SourceFile.clicked.connect(
            self.load
        )
        self.ui.Button_Run.clicked.connect(
            self.run
        )
        self.ui.Button_Save.clicked.connect(
            self.save_result
        )

    def load(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
                                                "Save process group",
                                                "process_group.json",
                                                "JSON Files (*.json)"
        )
        file_path = files[0]
        self.original_process_list = loadIncomingData(file_path)
        self.proces_list = deepcopy(self.original_process_list)

    def run(self):
        if self.proces_list is None:
            QMessageBox.warning(self, "Err", "No process loaded")
            return
        start_time = self.ui.SpinBox_StartTime.value() 
        finish_time = self.ui.SpinBox_finishTime.value()
        if start_time > finish_time:
            QMessageBox.warning(self, "Err", "Start time have to be smaller than finish time")
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
        self.proces_list = deepcopy(self.original_process_list)
        engin = ShedulingEngin(
                                algorithm,
                                finish_time,
                                self.proces_list,
                                start_time
                                )
        engin.run()
        self.metrics = engin.metrics
        self.proces_list = engin.process_list
        QMessageBox.information(self,"Sucess","Algorithm have been executed")

    def save_result(self):
        if self.proces_list is None or self.metrics is None:
            QMessageBox.warning(self, "Err", "You have to load file and run algoritm")
            return
        reslult_file_path, _ = QFileDialog.getSaveFileName(
                                                    self,
                                                    "Save process group",
                                                    "result.json",
                                                    "JSON Files (*.json)"
                                                )
        
        metrics_file_path, _ = QFileDialog.getSaveFileName(
                                                    self,
                                                    "Save Metrics",
                                                    "metrics.json",
                                                    "JSON Files (*.json)"
                                                )
        saveRawResult(self.proces_list, reslult_file_path)
        saveRawMetrics(self.metrics, metrics_file_path)



        
        

