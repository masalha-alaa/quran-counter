"""Capture every dialog's real presentation with deterministic sample content.

No Quran data, network requests, model workers, or credentials are loaded.
"""
import argparse
from importlib import import_module
import os
from pathlib import Path
import subprocess
import sys
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from PySide6.QtCore import QTranslator, Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QDialog
from gui.dialog_style import prepare_dialog, set_dialog_language
from my_utils.my_enums import AppLang

FORMS = {
    "mushaf": ("mushaf_view_dialog.mushaf_view", "Ui_MushafViewDialog", "mushaf_view"),
    "details": ("detailed_display_dialog.word_detailed_display_dialog", "Ui_DetailedWordDisplayDialog", "word_detailed_display_dialog"),
    "relations": ("relations_graph.relations_graph", "Ui_RelationsGraphDialog", "relations_graph"),
    "key": ("openai_key_setup_dialog.openai_key_setup_dialog", "Ui_OpenAiKeySetupDialog", "openai_key_setup_dialog"),
    "disambiguation": ("disambiguation_dialog.disambiguation_dialog", "Ui_DidsambiguationDialog", "disambiguation_dialog"),
    "download": ("download_dialog.download_dialog", "Ui_DownloadDialog", "download_dialog"),
    "update": ("version_update_dialog.version_update_dialog", "Ui_VersionUpdateDialog", "version_update_dialog"),
    "waiting": ("waiting_dialog.waiting_dialog", "Ui_WaitingDialog", "waiting_dialog"),
}


def create_dialog(kind, *, original=False):
    module, name, _ = FORMS[kind]
    dialog = QDialog()
    ui = getattr(import_module(f"gui.{module}"), name)()
    ui.setupUi(dialog)
    if not original:
        prepare_dialog(dialog, ui, kind)
    return dialog, ui


def sample_content(kind, ui, language):
    """Preview-only samples; never used by production controllers."""
    arabic = language == AppLang.ARABIC
    if kind == "details":
        ui.textBrowser.setHtml('<p dir="rtl" align="right">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</p>')
    if kind == "mushaf":
        # The same centered first-page fixture is used for original/restored
        # comparisons. This is visual sample content, not a data-backed search.
        verses = (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
            "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
            "الرَّحْمَٰنِ الرَّحِيمِ",
            "مَالِكِ يَوْمِ الدِّينِ",
            "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
            "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ",
            "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ",
        )
        ui.textBrowser.setAlignment(Qt.AlignCenter)
        ui.textBrowser.insertHtml('<h3 style="text-align:center">الفاتحة</h3><br>')
        ui.textBrowser.setAlignment(Qt.AlignCenter)
        ui.textBrowser.insertHtml("<br>".join(f"{verse} ({index})" for index, verse in enumerate(verses, 1)))
        for name, value in (("pageNumDisplay", "صفحة 1"), ("surahNumDisplay", "رقم: 1"),
                            ("surahNameDisplay", "الفاتحة"), ("versesCountDisplay", "آيات: 7"),
                            ("juzzNumDisplay", "جزء 1")):
            getattr(ui, name).setText(value)
    elif kind == "relations":
        import networkx as nx
        from algos.related_words import RelatedWords
        from unittest.mock import patch
        graph = nx.DiGraph()
        graph.add_node("مثال", role="source")
        graph.add_node("صلة", role="destination")
        graph.add_node("فرع", role="leaf")
        graph.add_edges_from([("مثال", "صلة"), ("مثال", "فرع")])
        ui.graphWidget.set_data(graph, "#191c23", language)
        with patch.object(RelatedWords, "arb_to_eng", {"مثال": "Example", "صلة": "Related", "فرع": "Branch"}):
            ui.graphWidget.create_graph(True)
    elif kind == "disambiguation":
        ui.instructionsWordLabel.setText("مثال" if arabic else "Example")
        ui.resultsListWidget.addItems(["معنى تجريبي أول", "معنى تجريبي ثانٍ"] if arabic else ["First sample meaning", "Second sample meaning"])
        ui.resultsListWidget.setCurrentRow(0)
    elif kind == "download":
        ui.progressBar.setValue(35)
    elif kind == "update":
        ui.statusLabel.setText("جاري الفحص..." if arabic else "Checking for updates...")
        ui.downloadButton.hide()
    elif kind == "waiting":
        from my_widgets.spinning_loader import SpinningLoader
        ui.spinner = SpinningLoader()
        ui.verticalLayout.addWidget(ui.spinner)
        ui.spinner.show()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("docs/ui/dialogs"))
    parser.add_argument("--screen", choices=("all", *FORMS), default="all")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    os.chdir(ROOT)
    app = QApplication([])
    QFontDatabase.addApplicationFont("fonts/NotoNaskhArabic-VariableFont_wght.ttf")
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        subprocess.run([sys.executable, "tools/compile_translations.py", "--output-dir", temporary], check=True, capture_output=True)
        for language in (AppLang.ARABIC, AppLang.ENGLISH):
            for kind, (_, _, catalog) in FORMS.items():
                if args.screen not in ("all", kind):
                    continue
                translator = QTranslator()
                if not translator.load(str(Path(temporary) / f"{catalog}_{language.value}.qm")):
                    raise RuntimeError(f"Missing translation: {catalog}")
                app.installTranslator(translator)
                dialog, ui = create_dialog(kind)
                set_dialog_language(dialog, language)
                sample_content(kind, ui, language)
                if kind == "mushaf":
                    dialog.resize(1920, 1110)
                dialog.show()
                app.processEvents()
                def capture(name):
                    path = output / f"{name}-{language.value}.png"
                    if not dialog.grab().save(str(path)):
                        raise RuntimeError(f"Could not save {path}")
                capture(kind)
                if kind == "mushaf":
                    ui.stats_toggle.click()
                    app.processEvents()
                    capture("mushaf-collapsed")
                    original, original_ui = create_dialog("mushaf", original=True)
                    sample_content("mushaf", original_ui, language)
                    original.resize(1920, 1110)
                    original.show()
                    app.processEvents()
                    path = output / f"mushaf-original-{language.value}.png"
                    if not original.grab().save(str(path)):
                        raise RuntimeError(f"Could not save {path}")
                    original.close()
                    original.deleteLater()
                if kind == "relations":
                    from matplotlib import pyplot as plt
                    plt.close(ui.graphWidget.figure)
                dialog.close()
                dialog.deleteLater()
                app.removeTranslator(translator)
    print(f"Saved all dialog previews to {output}")


if __name__ == "__main__":
    main()
