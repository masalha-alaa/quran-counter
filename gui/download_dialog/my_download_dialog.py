from PySide6.QtWidgets import QApplication
from datetime import datetime
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShowEvent, QTextCursor, QCloseEvent
from PySide6.QtCore import Slot

import my_utils.utils
from gui.download_dialog.download_dialog import Ui_DownloadDialog
from my_utils.utils import show_error_dialog
from my_utils.shared_data import SharedData
from my_utils.utils import AppLang
from my_utils.model_downloader import ModelDownloader
import os
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtNetwork import QNetworkReply
from my_utils.utils import resource_path, is_package_installed, is_topics_model_available, is_topics_model_zip_available, is_torch_installed_with_gpu
from my_utils.utils import translate_text
from worker_threads.package_installer_thread import PackageInstallerThread
from worker_threads.zip_extractor_thread import ZipExtractorThread
from math import ceil


class MyDownloadDialog(QDialog, Ui_DownloadDialog):

    def __init__(self, language: None | AppLang):
        super(MyDownloadDialog, self).__init__()
        self.setupUi(self)
        self._current_lang = None
        self._apply_language(language)
        self.model_downloader = ModelDownloader()
        # self.sentence_transformers_package_installer = PackageInstallerThread(SharedData.sentence_transformers_pkg_details)
        # self.pytorch_gpu_package_installer = PackageInstallerThread(SharedData.pytorch_gpu_pkg_details)
        model_name = resource_path('embedding_models/topic_sim_model')
        self.zip_extractor = ZipExtractorThread(f"{model_name}.zip", resource_path('embedding_models'))

        # self.failure_icon = QLabel()
        # self.failure_icon.setPixmap(QPixmap(resource_path("gui/resources/failure-x-icon.png")).scaled(15, 16))
        # self.failure_icon.hide()
        # self.success_icon = QLabel()
        # self.success_icon.setPixmap(QPixmap(resource_path("gui/resources/success-v-icon.png")).scaled(15, 16))
        # self.success_icon.hide()
        # self.statusParentLayout.addWidget(self.success_icon)
        # self.statusParentLayout.addWidget(self.failure_icon)
        # self.statusParentLayout.addWidget(self.spinner)

        self._setup_events()

    def showEvent(self, event: QShowEvent):
        super().showEvent(event)
        self.hide_status()

    def closeEvent(self, event):
        self.model_downloader.cancel_download()
        super().closeEvent(event)

    def set_language(self, lang):
        self._apply_language(lang)

    def _apply_language(self, lang):
        if lang != self._current_lang:
            self.retranslateUi(self)
            # self.set_font_for_language(lang)
            self._current_lang = lang

    def _setup_events(self):
        self.noButton.clicked.connect(self.reject)
        self.yesButton.clicked.connect(self.on_accepted)
        self.model_downloader.set_download_started_callback(self.download_started_callback)
        self.model_downloader.set_download_progress_callback(self.download_progress_callback)
        self.model_downloader.set_download_finished_callback(self.download_finished_callback)

    def show_success(self):
        pass

    def show_failure(self, msg="Error"):
        show_error_dialog(self, msg)

    def hide_status(self):
        pass

    @Slot()
    def on_accepted(self):
        self.yesButton.setEnabled(False)
        self.noButton.setEnabled(False)
        self.initialize()

    def initialize(self):
        self.detailsLabel.setText(translate_text("Initializing..."))
        QApplication.processEvents()
        self.progressBar.setValue(0)
        if not is_topics_model_available():
            print("Model not available")
            self.progressBar.setValue(0)
            if not is_topics_model_zip_available():
                print("Zip file not available. Downloading...")
                self.detailsLabel.setText(translate_text("Downloading..."))
                QApplication.processEvents()
                self.model_downloader.start_download()  # => calls self.download_finished_callback()
            else:
                print("Zip file available. Extracting...")
                self.start_zip_extraction()
        else:
            print("Model is available")
            self.accept()
        # if my_utils.utils.is_cuda_available() and not is_torch_installed_with_gpu():
        #     print("Installing torch with GPU...")
        #     self.detailsLabel.setText("Installing pytorch with GPU (ETA ~5 minutes)...")
        #     self.progressBar.setValue(30)
        #     self.pytorch_gpu_package_installer.started.connect(self.pytorch_gpu_installation_started)
        #     self.pytorch_gpu_package_installer.progress.connect(self.pytorch_gpu_installation_progress)
        #     self.pytorch_gpu_package_installer.finished.connect(self.pytorch_gpu_installed)
        #     self.pytorch_gpu_package_installer.start()
        # else:
        #     self.run_sentence_transformers_installation()

    def run_sentence_transformers_installation(self):
        if not is_package_installed(SharedData.sentence_transformers_pkg_details):
            print("Installing sentence transformers...")
            self.detailsLabel.setText("Installing sentence transformers (ETA ~5 minutes)...")
            self.progressBar.setValue(60)
            self.sentence_transformers_package_installer.started.connect(self.sentence_transformers_installation_started)
            self.sentence_transformers_package_installer.progress.connect(self.sentence_transformers_installation_progress)
            self.sentence_transformers_package_installer.finished.connect(self.sentence_transformers_installed)
            self.sentence_transformers_package_installer.start()
        else:
            print("Packages already installed")
            self.progressBar.setValue(100)
            self.sentence_transformers_installed(True, SharedData.sentence_transformers_pkg_details, "", None)

    def sentence_transformers_installation_started(self):
        self.detailedOutputTextBrowser.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def sentence_transformers_installation_progress(self, line):
        self.detailedOutputTextBrowser.append(line)

    def sentence_transformers_installed(self, success: bool, package_name: str, error: str, caller_thread: PackageInstallerThread|None):
        if caller_thread is not None:
            caller_thread.finished.disconnect(self.sentence_transformers_installed)
        if success:
            print("Success")
            self.progressBar.setValue(100)
            if not is_topics_model_available():
                print("Model not available")
                self.progressBar.setValue(0)
                if not is_topics_model_zip_available():
                    print("Zip file not available. Downloading...")
                    self.detailsLabel.setText("Downloading...")
                    self.model_downloader.start_download()  # => calls self.download_finished_callback()
                else:
                    print("Zip file available. Extracting...")
                    self.start_zip_extraction()
            else:
                print("Model is available")
                self.accept()
        else:
            print(f"ERROR INSTALLING PACKAGE {package_name}")

    def pytorch_gpu_installation_started(self):
        self.detailedOutputTextBrowser.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def pytorch_gpu_installation_progress(self, line):
        self.detailedOutputTextBrowser.append(line)

    def pytorch_gpu_installed(self, success: bool, package_name: str, error: str, caller_thread: PackageInstallerThread):
        caller_thread.finished.disconnect(self.pytorch_gpu_installed)
        if success:
            self.run_sentence_transformers_installation()
        else:
            print(f"ERROR INSTALLING PACKAGE {package_name}")


    def start_zip_extraction(self):
        print("Unzipping zip file...")
        self.detailsLabel.setText(translate_text("Unzipping..."))
        QApplication.processEvents()
        self.zip_extractor.progress.connect(self.zip_extraction_progress)
        self.zip_extractor.finished.connect(self.zip_extraction_finished)
        self.zip_extractor.start()

    def download_started_callback(self):
        print("Downloading model...")
        self.progressBar.setValue(0)

    def download_progress_callback(self, total_bytes_received, total_bytes, eta=None):
        # Update progress bar
        # progress = min(ceil((total_bytes_received / total_bytes) * 100), 100)
        progress = (total_bytes_received / total_bytes) * 100

        self.progressBar.setValue(progress)
        if eta is not None:
            eta = int(eta)
            h, s = divmod(eta, 3600)
            m, s = divmod(s, 60)
            self.progressBar.setFormat(f"{progress:.2f}% (ETA {h:02d}:{m:02d}:{s:02d})")

    def download_finished_callback(self, reply: QNetworkReply):
        # Check if the request was successful
        if reply.error() != QNetworkReply.NetworkError.NoError:
            print(f"Download failed: {reply.errorString()}")
            self.show_failure(reply.errorString())
        else:
            # Set the target file path where the downloaded zip file will be saved
            download_folder = resource_path("embedding_models")
            filename = "topic_sim_model.zip"  # Specify the name for the downloaded file
            file_path = os.path.join(download_folder, filename)
            print(file_path)

            # create folder if doesn't exist
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            # Open the file to write the downloaded content
            file = QFile(file_path)
            if file.open(QIODevice.OpenModeFlag.WriteOnly):
                file.write(reply.readAll())  # Write the data to the file
                print(f"File successfully downloaded to {file_path}")
                file.close()  # Manually close the file after writing
                self.show_success()
                self.start_zip_extraction()
            else:
                print("Failed to open file for writing.")
                self.show_failure("Could not open file")

    def zip_extraction_progress(self, progress: float):
        self.progressBar.setValue(progress)

    def zip_extraction_finished(self, src, dst, caller_thread: ZipExtractorThread):
        print("Finished unzipping. Cleaning up...")
        self.progressBar.setValue(90)
        self.detailsLabel.setText("Cleaning up...")
        if os.path.isfile(src):
            os.remove(src)
        self.progressBar.setValue(100)
        caller_thread.finished.disconnect(self.zip_extraction_finished)
        self.detailsLabel.setText("Done")
        print("Extraction done")
        self.accept()  # Close the dialog and return # QDialog.DialogCode.Accepted
