"""Capture the real main-window layout without loading private Quran data.

This is a visual preview only, not a replacement application entry point.
Run from the repository root, e.g.:
    python tools/render_ui_preview.py --language en --output preview.png
"""

import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from PySide6.QtCore import QEvent, QTranslator
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.main_window.modern_main_window import Ui_MainWindow
from my_utils.my_enums import AppLang


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("ar", "en"), default="ar")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--width", type=int, default=1220)
    parser.add_argument("--height", type=int, default=860)
    args = parser.parse_args()
    output = args.output.resolve()
    os.chdir(ROOT)  # Existing resource_path() resolves development assets here.
    app = QApplication([])
    QFontDatabase.addApplicationFont("fonts/NotoNaskhArabic-VariableFont_wght.ttf")
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    translator = QTranslator()
    with tempfile.TemporaryDirectory() as temporary:
        if args.language == "en":
            translation = Path(temporary) / "main_screen_en.qm"
            executable = "pyside6-lrelease.exe" if sys.platform == "win32" else "pyside6-lrelease"
            subprocess.run([str(Path(sys.executable).with_name(executable)),
                            "translations/main_screen_en.ts", "-qm", str(translation)], check=True)
            if not translator.load(str(translation)):
                raise RuntimeError("Could not load the English translation")
            app.installTranslator(translator)
            ui.retranslateUi(window)
            ui.set_language(window, AppLang.ENGLISH)
        # Mirror the controller's initial presentation without starting workers.
        ui.tabWidget.setTabVisible(3, False)
        for slider, label in ((ui.similarityThresholdSlider, ui.similarityThresholdLabel),
                              (ui.relatedWordsThresholdSlider, ui.relatedWordsThresholdLabel)):
            slider.setEnabled(False)
            label.setText(str(slider.value()))
        window.resize(args.width, args.height)
        window.show()
        app.sendPostedEvents(None, QEvent.Type.DeferredDelete)
        app.processEvents()
        output.parent.mkdir(parents=True, exist_ok=True)
        if not window.grab().save(str(output)):
            raise RuntimeError(f"Could not write preview to {output}")
        print(f"Saved {args.language} UI preview to {output}")
        window.close()


if __name__ == "__main__":
    main()
