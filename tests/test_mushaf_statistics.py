"""Run the real statistics workers against small, deterministic Surah fixtures."""
import os
from types import SimpleNamespace
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6.QtCore import QEvent, QSignalBlocker, QThread
from PySide6.QtWidgets import QApplication


class MushafStatisticsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        from gui.mushaf_view_dialog import my_mushaf_view_dialog
        cls.module = my_mushaf_view_dialog

    def setUp(self):
        self.workers = []
        self.native_start = self.module.SpanInfoThread.start
        self.texts = {55: ["ا ب ب"], 56: ["ت ت ا ب"]}
        self.names = {"الرحمن": 55, "الواقعة": 56, "": 0}
        loader = self.module.MyDataLoader
        # Use all 29 bins, as in the form, with easily checked fixture counts.
        alphabet = "ابتثجحخدذرزسشصضطظعغفقكلمنهويء"
        patches = (
            patch.object(loader, "letters_histogram_index", dict(zip(alphabet, range(len(alphabet))))),
            patch.object(loader, "get_surah", side_effect=self.texts.__getitem__),
            patch.object(loader, "get_surah_num", side_effect=self.names.__getitem__),
            patch.object(self.module.SpanInfoThread, "start", new=lambda worker: self.workers.append(worker)),
            patch.object(self.module.QTimer, "singleShot"),
        )
        for patcher in patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.dialog = self.module.MyMushafViewDialog(self.module.AppLang.ARABIC)
        # Page 531 is the reported two-Surah case. Text is a small fixture,
        # not the unavailable full Quran dataset or claimed page-531 totals.
        self.dialog._current_page = 531
        self.dialog.page.surahs = [SimpleNamespace(surah_num=number, surah_name=name)
                                  for name, number in self.names.items() if number]
        self.dialog.last_selection_type = self.module.SelectionType.BY_PAGE

    def tearDown(self):
        self.dialog.spinner.stop()
        self.dialog.running_threads.clear()
        self.dialog.deleteLater()
        self.app.sendPostedEvents(None, QEvent.DeferredDelete)

    def reset(self):
        start = len(self.workers)
        self.dialog.resetStatsButton.click()
        return self.workers[start:]

    def snapshot(self):
        return ([self.dialog.lettersHistogram.item(0, i).text()
                 for i in range(self.dialog.lettersHistogram.columnCount())],
                self.dialog.lettersSumTableWidget.item(0, 0).text(),
                self.dialog.surahWordsNum.text())

    def assert_combined(self):
        counts, total, words = self.snapshot()
        self.assertEqual(list(map(int, counts)), [2, 3, 2] + [0] * 26)
        self.assertEqual(total, "7")
        self.assertEqual(words, "الرحمن: 3, الواقعة: 4")

    def select_text(self, text):
        with QSignalBlocker(self.dialog.textBrowser):
            self.dialog.textBrowser.setPlainText(text)
            cursor = self.dialog.textBrowser.textCursor()
            cursor.select(cursor.SelectionType.Document)
            self.dialog.textBrowser.setTextCursor(cursor)
        self.dialog.start_span_info_thread(self.module.SelectionType.BY_TEXT)
        return self.workers[-1]

    def test_repeated_resets_sum_both_surahs_in_either_completion_order(self):
        for order in ((0, 1), (1, 0), (0, 1), (1, 0)):
            with self.subTest(order=order):
                workers = self.reset()
                self.assertEqual(len(workers), 2)
                workers[order[0]].run()
                self.assertEqual(self.snapshot()[0], [""] * 29)
                workers[order[1]].run()
                self.assert_combined()

    def test_previous_reset_cannot_overwrite_or_duplicate_new_statistics(self):
        older = self.reset()
        current = self.reset()
        current[1].run()
        older[0].run()
        current[0].run()
        older[1].run()
        self.assert_combined()

    def test_reset_ignores_pending_selection_result(self):
        selection = self.select_text("ا ا ا")
        self.dialog.waiting()
        self.assertFalse(self.dialog.textBrowser.isEnabled())
        for worker in self.reset():
            worker.run()
        self.assert_combined()
        self.assertTrue(self.dialog.textBrowser.isEnabled())
        self.assertFalse(self.dialog.spinner.timer.isActive())
        selection.run()
        self.assert_combined()

    def test_selection_ignores_pending_surah_results(self):
        page = self.reset()
        selection = self.select_text("ب ب")
        selection.run()
        expected = self.snapshot()
        for worker in reversed(page):
            worker.run()
        self.assertEqual(self.snapshot(), expected)
        self.assertEqual(expected[1], "2")

    def test_one_surah_and_selection_reset_still_work(self):
        self.dialog.page.surahs = self.dialog.page.surahs[:1]
        self.reset()[0].run()
        self.assertEqual(self.snapshot()[0][:3], ["1", "2", "0"])
        self.assertEqual(self.snapshot()[1], "3")

        self.select_text("ت ا").run()
        self.assertEqual(self.snapshot()[1], "2")
        self.dialog.selectionResetButton.click()
        self.workers[-1].run()
        self.assertEqual(self.snapshot()[0][:3], ["1", "2", "0"])
        self.assertEqual(self.snapshot()[1], "3")

    def test_real_threads_publish_combined_counts_on_the_gui_thread(self):
        workers = self.reset()
        update_threads = []
        self.dialog.lettersHistogram.itemChanged.connect(
            lambda item: update_threads.append(QThread.currentThread()))
        for worker in workers:
            self.native_start(worker)
        for worker in workers:
            self.assertTrue(worker.wait(2000))
        self.app.processEvents()
        self.assert_combined()
        self.assertTrue(update_threads)
        self.assertTrue(all(thread == self.app.thread() for thread in update_threads))


if __name__ == "__main__":
    unittest.main()
