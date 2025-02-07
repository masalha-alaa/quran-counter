from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import requests


class ModelDownloader:
    def __init__(self, download_started_callback=None,
                 download_progress_callback=None,
                 download_finished_callback=None):
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.on_download_finished)
        self.download_started_callback = download_started_callback
        self.download_progress_callback = download_progress_callback
        self.download_finished_callback = download_finished_callback

    def set_download_started_callback(self, download_started_callback):
        self.download_started_callback = download_started_callback

    def set_download_progress_callback(self, download_progress_callback):
        self.download_progress_callback = download_progress_callback

    def set_download_finished_callback(self, download_finished_callback):
        self.download_finished_callback = download_finished_callback

    def start_download(self):
        if self.download_started_callback is not None:
            self.download_started_callback()

        # URL of the file to download
        api_url = "https://pufwli82h6.execute-api.us-east-2.amazonaws.com/prod/download-url"

        # Create the network request
        response = requests.get(api_url)
        download_url = response.json()['download_url']
        file_url = QNetworkRequest(QUrl(download_url))

        # Start the download and get the reply object
        self.reply = self.manager.get(file_url)

        # Connect the progress signal to update the progress bar
        if self.download_progress_callback is not None:
            self.reply.downloadProgress.connect(self.download_progress_callback)

    def on_download_finished(self, reply: QNetworkReply):
        self.manager.finished.disconnect(self.on_download_finished)
        reply.deleteLater()

        # call user callback
        if self.download_finished_callback is not None:
            self.download_finished_callback(reply)
