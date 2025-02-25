from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import requests
import time


class ModelDownloader:
    def __init__(self, download_started_callback=None,
                 download_progress_callback=None,
                 download_finished_callback=None):
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.on_download_finished)
        self.network_reply = None
        self.start_time = None
        self.last_packet_time = None
        self.eta_calc_freq_sec = 1
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
        self.network_reply = self.manager.get(file_url)
        self.start_time = time.time()
        self.last_packet_time = self.start_time

        # Connect the progress signal to update the progress bar
        self.network_reply.downloadProgress.connect(self.on_progress)

    def on_progress(self, total_bytes_received, total_bytes):
        if self.download_progress_callback is not None:
            now = time.time()
            elapsed_time_since_last_packet = now - self.last_packet_time
            if elapsed_time_since_last_packet > self.eta_calc_freq_sec:
                self.last_packet_time = now
                total_elapsed_time = now - self.start_time
                download_speed = total_bytes_received / total_elapsed_time  # Bytes per second
                remaining_bytes = total_bytes - total_bytes_received
                eta = remaining_bytes / download_speed  # Remaining time in seconds
            else:
                eta = None
            self.download_progress_callback(total_bytes_received, total_bytes, eta)


    def on_download_finished(self, reply: QNetworkReply):
        self.manager.finished.disconnect(self.on_download_finished)
        reply.deleteLater()

        # call user callback
        if self.download_finished_callback is not None:
            self.download_finished_callback(reply)

    def cancel_download(self):
        self.network_reply.abort()
        self.network_reply.deleteLater()
        self.network_reply = None
