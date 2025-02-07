from PySide6.QtCore import QThread, Signal
import zipfile
from PySide6.QtWidgets import QApplication


class ZipExtractorThread(QThread):
    progress = Signal(float)
    finished = Signal(str, str, QThread)

    def __init__(self, zip_path, destination_path):
        super().__init__()
        self.zip_path = zip_path
        self.destination_path = destination_path

    def run(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            for index, file_name in enumerate(file_list):
                zip_ref.extract(file_name, self.destination_path)
                self.progress.emit((index + 1) / total_files * 100)
                QApplication.processEvents()  # Update GUI during extraction

        self.finished.emit(self.zip_path, self.destination_path, self)
