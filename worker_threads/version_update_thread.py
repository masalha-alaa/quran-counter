import os
import requests
from paths import ROOT_DIR
from PySide6.QtCore import QThread, Signal


class Version:
    def __init__(self, version):
        major, minor, patch = [int(v) for v in version.split(".")]
        self.major = major
        self.minor = minor
        self.patch = patch

    def __gt__(self, other):
        return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

class VersionUpdateThread(QThread):
    check_finished = Signal(str, QThread)

    BASE_URL = "https://sourceforge.net/projects"
    PROJECT_NAME = "qurancounter"
    FILES_PATH = "files"
    LATEST_VERSION_INFO_URL = f"{BASE_URL}/{PROJECT_NAME}/{FILES_PATH}/app_info.json"
    LATEST_VERSION_FILE_URL = f"{BASE_URL}/{PROJECT_NAME}/{FILES_PATH}/QuranCounter.zip"

    def __init__(self):
        super().__init__()

    def check_for_update(self, current_version=None):
        if current_version is None:
            from json import load as j_load
            from my_utils.utils import resource_path
            app_info_path = resource_path(os.path.join(ROOT_DIR, "app_info.json"))
            current_version = j_load(open(app_info_path))['app_version']
        current_version = Version(current_version)
        response = requests.get(VersionUpdateThread.LATEST_VERSION_INFO_URL)
        if response.status_code == 200:
            latest_data = response.json()
            latest_version = Version(latest_data["app_version"])
            if latest_version > current_version:
                print(f"Update available: {latest_version}")
                return VersionUpdateThread.LATEST_VERSION_FILE_URL
        return ''

    def run(self):
        update_url = self.check_for_update()
        self.check_finished.emit(update_url, self)


if __name__ == "__main__":
    # TEST
    def check_done_callback(update_url: str, caller_thread: VersionUpdateThread):
        caller_thread.check_finished.disconnect(check_done_callback)
        if update_url:
            print(f"Download new version: {update_url}")
        else:
            print("You're up to date!")

    v = VersionUpdateThread()
    v.check_finished.connect(check_done_callback)
    v.start()
    while True: pass
