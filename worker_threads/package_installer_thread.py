from PySide6.QtCore import QThread, Signal
import os
import subprocess
import sys
from my_utils.utils import resource_path

from my_utils.package_details import PackageDetails


class PackageInstallerThread(QThread):
    started = Signal()
    progress = Signal(str)
    install_finished = Signal(bool, str, str, QThread)

    def __init__(self, package_details: PackageDetails):
        super().__init__()
        self.package_details = package_details

    def _install_package(self):
        """
        Installs a Python package into a specified directory.
        """
        self.started.emit()

        # Ensure the target directory exists
        os.makedirs(self.package_details.package_installation_dir, exist_ok=True)

        # Construct the pip install command
        python_executable = resource_path("python-3.10.11-embed-amd64/python.exe") if hasattr(sys, '_MEIPASS') else sys.executable
        # print(f"{python_executable = }")
        pip_command = [
            python_executable, "-m", "pip", "install", self.package_details.package_installation_name,
            "--target", self.package_details.package_installation_dir,
            "--no-cache-dir",  # Avoid caching to save space
            # "-q",  # quite
        ]
        if self.package_details.extra_index_url:
            pip_command.extend(["--extra-index-url", self.package_details.extra_index_url])

        # Run the pip command
        process = subprocess.Popen(pip_command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   bufsize=1)
        # Display output in real-time
        # while True:
        #     char = process.stdout.read(1)  # Read one character at a time
        #     self.progress.emit(char)
        #     # print(char, end="", flush=True)  # Print without newline, flush ensures immediate display
        #     if not char and process.poll() is not None:  # Check if the process is done
        #         break

        for line in process.stdout:
            self.progress.emit(line.lstrip())

    def run(self):
        try:
            self._install_package()
            # Emit success
            self.install_finished.emit(True, self.package_details.package_installation_name, "", self)
        except subprocess.CalledProcessError as e:
            # Emit failure
            self.install_finished.emit(False, self.package_details.package_installation_name, e, self)
