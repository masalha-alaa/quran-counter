# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mushaf_view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MushafViewDialog(object):
    def setupUi(self, MushafViewDialog):
        if not MushafViewDialog.objectName():
            MushafViewDialog.setObjectName(u"MushafViewDialog")
        MushafViewDialog.resize(1029, 840)
        MushafViewDialog.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 18pt \"Calibri\";")
        self.verticalLayout_15 = QVBoxLayout(MushafViewDialog)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line = QFrame(MushafViewDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_2 = QFrame(MushafViewDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 14pt;")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.selectionStartLabel = QLabel(self.frame_2)
        self.selectionStartLabel.setObjectName(u"selectionStartLabel")

        self.horizontalLayout_16.addWidget(self.selectionStartLabel)

        self.selectionStartButton = QPushButton(self.frame_2)
        self.selectionStartButton.setObjectName(u"selectionStartButton")

        self.horizontalLayout_16.addWidget(self.selectionStartButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)

        self.selectionEndLabel = QLabel(self.frame_2)
        self.selectionEndLabel.setObjectName(u"selectionEndLabel")

        self.horizontalLayout_17.addWidget(self.selectionEndLabel)

        self.selectionEndButton = QPushButton(self.frame_2)
        self.selectionEndButton.setObjectName(u"selectionEndButton")

        self.horizontalLayout_17.addWidget(self.selectionEndButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.verticalLayout_11.addWidget(self.label_16)


        self.verticalLayout_10.addWidget(self.frame_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.goToPageButton = QPushButton(MushafViewDialog)
        self.goToPageButton.setObjectName(u"goToPageButton")
        icon = QIcon()
        icon.addFile(u":/search-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goToPageButton.setIcon(icon)
        self.goToPageButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.goToPageButton)

        self.line_2 = QFrame(MushafViewDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_2)

        self.pageInput = QLineEdit(MushafViewDialog)
        self.pageInput.setObjectName(u"pageInput")
        self.pageInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.pageInput)

        self.label = QLabel(MushafViewDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.goToRefButton = QPushButton(MushafViewDialog)
        self.goToRefButton.setObjectName(u"goToRefButton")
        self.goToRefButton.setIcon(icon)
        self.goToRefButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.goToRefButton)

        self.line_3 = QFrame(MushafViewDialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_3)

        self.verseInput = QLineEdit(MushafViewDialog)
        self.verseInput.setObjectName(u"verseInput")
        self.verseInput.setEnabled(True)
        self.verseInput.setLayoutDirection(Qt.RightToLeft)
        self.verseInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.verseInput)

        self.label_5 = QLabel(MushafViewDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.surahNumInput = QLineEdit(MushafViewDialog)
        self.surahNumInput.setObjectName(u"surahNumInput")
        self.surahNumInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.surahNumInput)

        self.label_4 = QLabel(MushafViewDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 8)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.goToSurahNameButton = QPushButton(MushafViewDialog)
        self.goToSurahNameButton.setObjectName(u"goToSurahNameButton")
        self.goToSurahNameButton.setIcon(icon)
        self.goToSurahNameButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.goToSurahNameButton)

        self.line_4 = QFrame(MushafViewDialog)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_14.addWidget(self.line_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verseInput_2 = QLineEdit(MushafViewDialog)
        self.verseInput_2.setObjectName(u"verseInput_2")
        self.verseInput_2.setEnabled(False)
        self.verseInput_2.setLayoutDirection(Qt.RightToLeft)
        self.verseInput_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.verseInput_2)

        self.label_17 = QLabel(MushafViewDialog)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_18.addWidget(self.label_17)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.surahNameInput = QLineEdit(MushafViewDialog)
        self.surahNameInput.setObjectName(u"surahNameInput")

        self.horizontalLayout_19.addWidget(self.surahNameInput)

        self.label_6 = QLabel(MushafViewDialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_19.addWidget(self.label_6)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(3, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.horizontalLayout_11.setStretch(2, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.textBrowser = QTextBrowser(MushafViewDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textBrowser.setLayoutDirection(Qt.RightToLeft)
        self.textBrowser.setStyleSheet(u"font-family: 'Noto Naskh Arabic'; font-size: 17pt;")
        self.textBrowser.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pageNumDisplay = QLineEdit(MushafViewDialog)
        self.pageNumDisplay.setObjectName(u"pageNumDisplay")
        self.pageNumDisplay.setEnabled(False)
        self.pageNumDisplay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.pageNumDisplay)

        self.label_15 = QLabel(MushafViewDialog)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.surahNumDisplay = QLineEdit(MushafViewDialog)
        self.surahNumDisplay.setObjectName(u"surahNumDisplay")
        self.surahNumDisplay.setEnabled(False)
        self.surahNumDisplay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.surahNumDisplay)

        self.label_14 = QLabel(MushafViewDialog)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nextPushButton = QPushButton(MushafViewDialog)
        self.nextPushButton.setObjectName(u"nextPushButton")

        self.horizontalLayout.addWidget(self.nextPushButton)

        self.prevPushButton = QPushButton(MushafViewDialog)
        self.prevPushButton.setObjectName(u"prevPushButton")

        self.horizontalLayout.addWidget(self.prevPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_15.addLayout(self.verticalLayout)

        self.frame = QFrame(MushafViewDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font-size: 11pt;")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_8.addWidget(self.label_11)

        self.wordsFromBeginOfMushaf = QLabel(self.frame)
        self.wordsFromBeginOfMushaf.setObjectName(u"wordsFromBeginOfMushaf")
        self.wordsFromBeginOfMushaf.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.wordsFromBeginOfMushaf)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 3, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.wordsInSelection = QLabel(self.frame)
        self.wordsInSelection.setObjectName(u"wordsInSelection")
        self.wordsInSelection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.wordsInSelection)


        self.gridLayout.addLayout(self.verticalLayout_9, 2, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.wordsFromBeginOfSurah = QLabel(self.frame)
        self.wordsFromBeginOfSurah.setObjectName(u"wordsFromBeginOfSurah")
        self.wordsFromBeginOfSurah.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.wordsFromBeginOfSurah)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 3, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.label_7)

        self.lettersFromBeginOfSurah = QLabel(self.frame)
        self.lettersFromBeginOfSurah.setObjectName(u"lettersFromBeginOfSurah")
        self.lettersFromBeginOfSurah.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lettersFromBeginOfSurah)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.lettersFromBeginOfMushaf = QLabel(self.frame)
        self.lettersFromBeginOfMushaf.setObjectName(u"lettersFromBeginOfMushaf")
        self.lettersFromBeginOfMushaf.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lettersFromBeginOfMushaf)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 2, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_12.addWidget(self.label_2)

        self.surahWordsNum = QLabel(self.frame)
        self.surahWordsNum.setObjectName(u"surahWordsNum")
        self.surahWordsNum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.surahWordsNum)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)

        self.surahLettersNum = QLabel(self.frame)
        self.surahLettersNum.setObjectName(u"surahLettersNum")
        self.surahLettersNum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.surahLettersNum)


        self.gridLayout.addLayout(self.verticalLayout_13, 1, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.lettersInSelection = QLabel(self.frame)
        self.lettersInSelection.setObjectName(u"lettersInSelection")
        self.lettersInSelection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lettersInSelection)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 2, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.mostRepeatedLetter = QLabel(self.frame)
        self.mostRepeatedLetter.setObjectName(u"mostRepeatedLetter")

        self.verticalLayout_14.addWidget(self.mostRepeatedLetter)


        self.gridLayout.addLayout(self.verticalLayout_14, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_15.addWidget(self.frame)

        QWidget.setTabOrder(self.pageInput, self.goToPageButton)
        QWidget.setTabOrder(self.goToPageButton, self.surahNumInput)
        QWidget.setTabOrder(self.surahNumInput, self.verseInput)
        QWidget.setTabOrder(self.verseInput, self.goToRefButton)
        QWidget.setTabOrder(self.goToRefButton, self.goToSurahNameButton)
        QWidget.setTabOrder(self.goToSurahNameButton, self.selectionStartButton)
        QWidget.setTabOrder(self.selectionStartButton, self.prevPushButton)
        QWidget.setTabOrder(self.prevPushButton, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.surahNumDisplay)
        QWidget.setTabOrder(self.surahNumDisplay, self.pageNumDisplay)
        QWidget.setTabOrder(self.pageNumDisplay, self.nextPushButton)
        QWidget.setTabOrder(self.nextPushButton, self.selectionEndButton)

        self.retranslateUi(MushafViewDialog)

        QMetaObject.connectSlotsByName(MushafViewDialog)
    # setupUi

    def retranslateUi(self, MushafViewDialog):
        MushafViewDialog.setWindowTitle(QCoreApplication.translate("MushafViewDialog", u"Dialog", None))
        self.selectionStartLabel.setText("")
        self.selectionStartButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.selectionEndLabel.setText("")
        self.selectionEndButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.label_16.setText(QCoreApplication.translate("MushafViewDialog", u"1. \u0627\u062e\u062a\u0631 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629, \u062b\u0645 \u0627\u0636\u063a\u0637 \"\u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f\".\n"
"2. \u0627\u062e\u062a\u0631 \u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f (\u0641\u064a \u0646\u0641\u0633 \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0648 \u063a\u064a\u0631\u0647\u0627), \u062b\u0645 \u0627\u0636\u063a\u0637 \"\u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f\".", None))
        self.goToPageButton.setText("")
        self.label.setText(QCoreApplication.translate("MushafViewDialog", u"\u0635\u0641\u062d\u0629", None))
        self.goToRefButton.setText("")
        self.verseInput.setText("")
        self.label_5.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0627\u064a\u0629", None))
        self.label_4.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.goToSurahNameButton.setText("")
        self.verseInput_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0627\u064a\u0629", None))
        self.label_6.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0633\u0645 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.label_15.setText(QCoreApplication.translate("MushafViewDialog", u"\u0635\u0641\u062d\u0629", None))
        self.label_14.setText(QCoreApplication.translate("MushafViewDialog", u"\u0633\u0648\u0631\u0629", None))
        self.nextPushButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062a\u0627\u0644\u064a", None))
        self.prevPushButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0633\u0627\u0628\u0642", None))
        self.label_11.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u0645\u0646 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u0645\u0635\u062d\u0641", None))
        self.wordsFromBeginOfMushaf.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.wordsInSelection.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u0645\u0646 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.wordsFromBeginOfSurah.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u062d\u0631\u0641 \u0645\u0646 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.lettersFromBeginOfSurah.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u062d\u0631\u0641 \u0645\u0646 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u0645\u0635\u062d\u0641", None))
        self.lettersFromBeginOfMushaf.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahWordsNum.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u062d\u0631\u0648\u0641 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahLettersNum.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u062d\u0631\u0641 \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.lettersInSelection.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062d\u0631\u0641 \u0627\u0644\u0623\u0643\u062b\u0631 \u0645\u062a\u0631\u062f\u062f \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.mostRepeatedLetter.setText("")
    # retranslateUi

