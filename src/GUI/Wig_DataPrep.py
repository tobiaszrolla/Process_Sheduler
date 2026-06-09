from PySide6.QtWidgets import QWidget
from .UI.Wig_DataPrep_ui import Ui_Wig_DataPrep
from src.data_prep.data_generation import gererateProcesess
from src.data_prep.data_save_incoming import saveDataIncoming
from src.models.processList import ProcessList
from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
class Wig_DataPrep(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Wig_DataPrep()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.filebrowser = QFileDialog()
        self.process_group_lists = []
        self.model.clear()
        self.process_group_lists = []
        self.ui.wig_create.ui.Button_CreateProcess.clicked.connect(
            self.createProcessList
        )
        self.ui.wig_merge_save.ui.BSaveJSON.clicked.connect(
            self.save
        )
        self.ui.wig_merge_save.ui.BMerge.clicked.connect(
            self.merge_mix
        )
        self.ui.wig_merge_save.ui.View_ProcessGroups.setModel(self.model)
        


    def createProcessList(self):
        menu = self.ui.wig_create.ui

        nr_io_breaks = menu.SpinBoxIoBreak.value()
        max_cpu_time = menu.SpinBoxMaxCpuTime.value()
        max_io_time = menu.SpinBoxMaxIoTime.value()
        min_cpu_time = menu.SpinBoxMinCpuTime.value()
        min_io_time = menu.SpinBoxMinIoTime.value()
        nr_process = menu.SpinBoxProcesNumb.value()
        max_arr_time = menu.SpinBoxMaxArrivalTime.value()

        if nr_process <= 0:
            QMessageBox.warning(self, "Err", "Process number not > than 0")
            return

        if min_cpu_time > max_cpu_time:
            QMessageBox.warning(self, "Err", "Min CPU > Max CPU")
            return

        if min_io_time > max_io_time:
            QMessageBox.warning(self, "Err", "Min IO > Max IO")
            return

        p_list = gererateProcesess(
            nr_process,
            nr_io_breaks,
            [min_io_time, max_io_time],
            [min_cpu_time, max_cpu_time],
            max_arr_time
        )
        nr = len(self.process_group_lists) + 1
        strig = f"Process Group {nr}"
        item = QStandardItem(strig)
        self.model.appendRow(item)
        self.process_group_lists.append(p_list)

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(
                                                    self,
                                                    "Save process group",
                                                    "process_group.json",
                                                    "JSON Files (*.json)"
                                                )
        if len(self.process_group_lists) > 1:
            QMessageBox.warning(self, "Err", "Merge processes before save")
            return
        elif len(self.process_group_lists) < 1:
            QMessageBox.warning(self, "Err","You have to create process group")
            return
        else:
            QMessageBox.information(self, "Inf", "Saving")
        saveDataIncoming(self.process_group_lists[0], file_path)

    def merge_mix(self):
        if len(self.process_group_lists) < 2:
            QMessageBox.warning(self, "Err", "No process to merge and shuffle")
            return
        new_process = ProcessList()
        for p in self.process_group_lists:
            new_process = new_process.merge(p)
        new_process.shuffle_incoming()
        self.clear_processes()
        self.process_group_lists.append(new_process)
        self.model.appendRow(QStandardItem("Process Group 1"))


    def clear_processes(self):
        self.process_group_lists.clear()
        self.model.clear()       


               