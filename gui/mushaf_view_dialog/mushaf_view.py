# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mushaf_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MushafViewDialog(object):
    def setupUi(self, MushafViewDialog):
        if not MushafViewDialog.objectName():
            MushafViewDialog.setObjectName(u"MushafViewDialog")
        MushafViewDialog.resize(1144, 858)
        MushafViewDialog.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 18pt \"Calibri\";")
        self.verticalLayout_7 = QVBoxLayout(MushafViewDialog)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_2 = QFrame(MushafViewDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 14pt;")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.selectionStartButton = QPushButton(self.frame_2)
        self.selectionStartButton.setObjectName(u"selectionStartButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionStartButton.sizePolicy().hasHeightForWidth())
        self.selectionStartButton.setSizePolicy(sizePolicy)
        self.selectionStartButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.selectionStartButton, 0, 1, 1, 1)

        self.selectionEndButton = QPushButton(self.frame_2)
        self.selectionEndButton.setObjectName(u"selectionEndButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectionEndButton.sizePolicy().hasHeightForWidth())
        self.selectionEndButton.setSizePolicy(sizePolicy1)
        self.selectionEndButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.selectionEndButton, 1, 1, 1, 1)

        self.selectionStartLabel = QLabel(self.frame_2)
        self.selectionStartLabel.setObjectName(u"selectionStartLabel")

        self.gridLayout.addWidget(self.selectionStartLabel, 0, 0, 1, 1)

        self.selectionEndLabel = QLabel(self.frame_2)
        self.selectionEndLabel.setObjectName(u"selectionEndLabel")

        self.gridLayout.addWidget(self.selectionEndLabel, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_11.addLayout(self.gridLayout)

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
        self.goToPageButton.setAutoDefault(False)

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
        self.goToRefButton.setAutoDefault(False)

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

        self.goToRef_2 = QPushButton(MushafViewDialog)
        self.goToRef_2.setObjectName(u"goToRef_2")
        self.goToRef_2.setIcon(icon)
        self.goToRef_2.setIconSize(QSize(24, 24))
        self.goToRef_2.setAutoDefault(False)

        self.horizontalLayout_14.addWidget(self.goToRef_2)

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
        self.verseInput_2.setEnabled(True)
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

        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.textBrowser = QTextBrowser(MushafViewDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textBrowser.setLayoutDirection(Qt.RightToLeft)
        self.textBrowser.setStyleSheet(u"font-family: 'Noto Naskh Arabic'; font-size: 17pt;")
        self.textBrowser.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(MushafViewDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"font-size: 16pt;")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nextPushButton = QPushButton(self.frame_4)
        self.nextPushButton.setObjectName(u"nextPushButton")
        icon1 = QIcon()
        icon1.addFile(u":/left-arrow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextPushButton.setIcon(icon1)
        self.nextPushButton.setIconSize(QSize(20, 20))
        self.nextPushButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.nextPushButton)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pageSideIcon = QLabel(self.frame_4)
        self.pageSideIcon.setObjectName(u"pageSideIcon")
        self.pageSideIcon.setPixmap(QPixmap(u":/right-page-icon.png"))
        self.pageSideIcon.setScaledContents(False)
        self.pageSideIcon.setWordWrap(False)

        self.horizontalLayout_23.addWidget(self.pageSideIcon)

        self.pageNumDisplay = QLabel(self.frame_4)
        self.pageNumDisplay.setObjectName(u"pageNumDisplay")
        self.pageNumDisplay.setStyleSheet(u"")
        self.pageNumDisplay.setText(u"\u0627\u0644\u0635\u0641\u062d\u0629")
        self.pageNumDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.pageNumDisplay)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_23)

        self.prevPushButton = QPushButton(self.frame_4)
        self.prevPushButton.setObjectName(u"prevPushButton")
        icon2 = QIcon()
        icon2.addFile(u":/right-arrow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevPushButton.setIcon(icon2)
        self.prevPushButton.setIconSize(QSize(20, 20))
        self.prevPushButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.prevPushButton)

        self.line_7 = QFrame(self.frame_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: #565656;")
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_7)

        self.surahNumDisplay = QLabel(self.frame_4)
        self.surahNumDisplay.setObjectName(u"surahNumDisplay")
        self.surahNumDisplay.setStyleSheet(u"")
        self.surahNumDisplay.setText(u"\u0631\u0642\u0645 \u0627\u0644\u0633\u0648\u0631\u0629")
        self.surahNumDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.surahNumDisplay)

        self.line_6 = QFrame(self.frame_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: #565656;")
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.nextSurahButton = QPushButton(self.frame_4)
        self.nextSurahButton.setObjectName(u"nextSurahButton")
        self.nextSurahButton.setIcon(icon1)
        self.nextSurahButton.setIconSize(QSize(20, 20))
        self.nextSurahButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.nextSurahButton)

        self.surahNameDisplay = QLabel(self.frame_4)
        self.surahNameDisplay.setObjectName(u"surahNameDisplay")
        self.surahNameDisplay.setStyleSheet(u"font: bold;")
        self.surahNameDisplay.setText(u"\u0627\u0633\u0645 \u0627\u0644\u0633\u0648\u0631\u0629")
        self.surahNameDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.surahNameDisplay)

        self.prevSurahButton = QPushButton(self.frame_4)
        self.prevSurahButton.setObjectName(u"prevSurahButton")
        self.prevSurahButton.setIcon(icon2)
        self.prevSurahButton.setIconSize(QSize(20, 20))
        self.prevSurahButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.prevSurahButton)

        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: #565656;")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.versesCountDisplay = QLabel(self.frame_4)
        self.versesCountDisplay.setObjectName(u"versesCountDisplay")
        self.versesCountDisplay.setStyleSheet(u"")
        self.versesCountDisplay.setText(u"\u0639\u062f\u062f \u0627\u0644\u0622\u064a\u0627\u062a")
        self.versesCountDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.versesCountDisplay)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: #565656;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.nextJuzButton = QPushButton(self.frame_4)
        self.nextJuzButton.setObjectName(u"nextJuzButton")
        self.nextJuzButton.setIcon(icon1)
        self.nextJuzButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.nextJuzButton)

        self.juzzNumDisplay = QLabel(self.frame_4)
        self.juzzNumDisplay.setObjectName(u"juzzNumDisplay")
        self.juzzNumDisplay.setStyleSheet(u"")
        self.juzzNumDisplay.setText(u"\u062c\u0632\u0621")
        self.juzzNumDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.juzzNumDisplay)

        self.prevJuzButton = QPushButton(self.frame_4)
        self.prevJuzButton.setObjectName(u"prevJuzButton")
        self.prevJuzButton.setIcon(icon2)
        self.prevJuzButton.setIconSize(QSize(20, 20))
        self.prevJuzButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.prevJuzButton)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(7, 1)
        self.horizontalLayout_2.setStretch(10, 1)
        self.horizontalLayout_2.setStretch(13, 1)

        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 6)

        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.frame = QFrame(MushafViewDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"font-size: 11pt;")
        self.frame.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statsHorizontalLayout = QHBoxLayout()
        self.statsHorizontalLayout.setObjectName(u"statsHorizontalLayout")
        self.exclusiveWordsFrame = QFrame(self.frame)
        self.exclusiveWordsFrame.setObjectName(u"exclusiveWordsFrame")
        self.exclusiveWordsFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.exclusiveWordsFrame.setStyleSheet(u"")
        self.exclusiveWordsFrame.setFrameShape(QFrame.Box)
        self.exclusiveWordsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.exclusiveWordsFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 8, 8)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 8, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.differentRootCheckBox = QCheckBox(self.exclusiveWordsFrame)
        self.differentRootCheckBox.setObjectName(u"differentRootCheckBox")
        self.differentRootCheckBox.setStyleSheet(u"QToolTip { \n"
"    color: red;\n"
"}")

        self.horizontalLayout_3.addWidget(self.differentRootCheckBox)

        self.refreshExclusiveWordsButton = QPushButton(self.exclusiveWordsFrame)
        self.refreshExclusiveWordsButton.setObjectName(u"refreshExclusiveWordsButton")
        self.refreshExclusiveWordsButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/reset-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshExclusiveWordsButton.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.refreshExclusiveWordsButton)

        self.label_7 = QLabel(self.exclusiveWordsFrame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.exclusivePhrasesInSurah1 = QLabel(self.exclusiveWordsFrame)
        self.exclusivePhrasesInSurah1.setObjectName(u"exclusivePhrasesInSurah1")

        self.gridLayout_2.addWidget(self.exclusivePhrasesInSurah1, 1, 0, 1, 1)

        self.exclusivePhrasesInSurah2 = QLabel(self.exclusiveWordsFrame)
        self.exclusivePhrasesInSurah2.setObjectName(u"exclusivePhrasesInSurah2")

        self.gridLayout_2.addWidget(self.exclusivePhrasesInSurah2, 2, 0, 1, 1)

        self.exclusivePhrasesInSurah3 = QLabel(self.exclusiveWordsFrame)
        self.exclusivePhrasesInSurah3.setObjectName(u"exclusivePhrasesInSurah3")

        self.gridLayout_2.addWidget(self.exclusivePhrasesInSurah3, 3, 0, 1, 1)


        self.statsHorizontalLayout.addWidget(self.exclusiveWordsFrame)

        self.statsHorizontalLayout.setStretch(0, 5)

        self.horizontalLayout_6.addLayout(self.statsHorizontalLayout)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.wawIsAWordCheckbox = QCheckBox(self.frame_3)
        self.wawIsAWordCheckbox.setObjectName(u"wawIsAWordCheckbox")
        self.wawIsAWordCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.wawIsAWordCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.wawIsAWordCheckbox.setChecked(False)

        self.verticalLayout_18.addWidget(self.wawIsAWordCheckbox)

        self.waykaannaTwoWordsCheckbox = QCheckBox(self.frame_3)
        self.waykaannaTwoWordsCheckbox.setObjectName(u"waykaannaTwoWordsCheckbox")
        self.waykaannaTwoWordsCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.waykaannaTwoWordsCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.verticalLayout_18.addWidget(self.waykaannaTwoWordsCheckbox)

        self.huroofMaaniCheckbox = QCheckBox(self.frame_3)
        self.huroofMaaniCheckbox.setObjectName(u"huroofMaaniCheckbox")
#if QT_CONFIG(tooltip)
        self.huroofMaaniCheckbox.setToolTip(u"\u062d\u062a\u0649 / \u062b\u0645 / \u0639\u0644\u0649 / \u0639\u0646 ...")
#endif // QT_CONFIG(tooltip)
        self.huroofMaaniCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.huroofMaaniCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.huroofMaaniCheckbox.setChecked(True)

        self.verticalLayout_18.addWidget(self.huroofMaaniCheckbox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_13)

        self.line_8 = QFrame(self.frame_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_22.addWidget(self.line_8)

        self.verticalFrame = QFrame(self.frame_3)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 2, -1)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.verticalFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_3)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.surahUniqueWords = QLabel(self.verticalFrame)
        self.surahUniqueWords.setObjectName(u"surahUniqueWords")
        sizePolicy2.setHeightForWidth(self.surahUniqueWords.sizePolicy().hasHeightForWidth())
        self.surahUniqueWords.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.surahUniqueWords.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.surahUniqueWords.setLayoutDirection(Qt.LeftToRight)
        self.surahUniqueWords.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.surahUniqueWords.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.surahUniqueWords)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)


        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(self.verticalFrame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.mostRepeatedWord = QLabel(self.verticalFrame)
        self.mostRepeatedWord.setObjectName(u"mostRepeatedWord")
        sizePolicy2.setHeightForWidth(self.mostRepeatedWord.sizePolicy().hasHeightForWidth())
        self.mostRepeatedWord.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.mostRepeatedWord.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.mostRepeatedWord.setLayoutDirection(Qt.LeftToRight)
        self.mostRepeatedWord.setStyleSheet(u"")
        self.mostRepeatedWord.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.mostRepeatedWord)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_22.addWidget(self.verticalFrame)

        self.verticalFrame_2 = QFrame(self.frame_3)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setFrameShape(QFrame.NoFrame)
        self.verticalFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, -1, 0, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.resetStatsButton = QPushButton(self.verticalFrame_2)
        self.resetStatsButton.setObjectName(u"resetStatsButton")
        self.resetStatsButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.resetStatsButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.resetStatsButton)

        self.label_12 = QLabel(self.verticalFrame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.horizontalLayout.addWidget(self.label_12)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)

        self.wordsInSelection = QLabel(self.verticalFrame_2)
        self.wordsInSelection.setObjectName(u"wordsInSelection")
        sizePolicy2.setHeightForWidth(self.wordsInSelection.sizePolicy().hasHeightForWidth())
        self.wordsInSelection.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.wordsInSelection.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.wordsInSelection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.wordsInSelection)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)


        self.verticalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.verticalFrame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")

        self.verticalLayout_12.addWidget(self.label_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)

        self.surahWordsNum = QLabel(self.verticalFrame_2)
        self.surahWordsNum.setObjectName(u"surahWordsNum")
        sizePolicy2.setHeightForWidth(self.surahWordsNum.sizePolicy().hasHeightForWidth())
        self.surahWordsNum.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.surahWordsNum.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.surahWordsNum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.surahWordsNum)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)


        self.verticalLayout_4.addLayout(self.verticalLayout_12)


        self.horizontalLayout_22.addWidget(self.verticalFrame_2)

        self.horizontalLayout_22.setStretch(2, 5)
        self.horizontalLayout_22.setStretch(3, 5)

        self.horizontalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_7.addWidget(self.frame)

        self.verticalLayout_7.setStretch(0, 4)
        self.verticalLayout_7.setStretch(1, 1)
        QWidget.setTabOrder(self.pageInput, self.goToPageButton)
        QWidget.setTabOrder(self.goToPageButton, self.surahNumInput)
        QWidget.setTabOrder(self.surahNumInput, self.verseInput)
        QWidget.setTabOrder(self.verseInput, self.goToRefButton)
        QWidget.setTabOrder(self.goToRefButton, self.surahNameInput)
        QWidget.setTabOrder(self.surahNameInput, self.verseInput_2)
        QWidget.setTabOrder(self.verseInput_2, self.goToRef_2)
        QWidget.setTabOrder(self.goToRef_2, self.selectionStartButton)
        QWidget.setTabOrder(self.selectionStartButton, self.selectionEndButton)
        QWidget.setTabOrder(self.selectionEndButton, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.prevJuzButton)
        QWidget.setTabOrder(self.prevJuzButton, self.nextJuzButton)
        QWidget.setTabOrder(self.nextJuzButton, self.prevSurahButton)
        QWidget.setTabOrder(self.prevSurahButton, self.nextSurahButton)
        QWidget.setTabOrder(self.nextSurahButton, self.prevPushButton)
        QWidget.setTabOrder(self.prevPushButton, self.nextPushButton)
        QWidget.setTabOrder(self.nextPushButton, self.resetStatsButton)
        QWidget.setTabOrder(self.resetStatsButton, self.refreshExclusiveWordsButton)
        QWidget.setTabOrder(self.refreshExclusiveWordsButton, self.wawIsAWordCheckbox)
        QWidget.setTabOrder(self.wawIsAWordCheckbox, self.waykaannaTwoWordsCheckbox)

        self.retranslateUi(MushafViewDialog)

        QMetaObject.connectSlotsByName(MushafViewDialog)
    # setupUi

    def retranslateUi(self, MushafViewDialog):
        MushafViewDialog.setWindowTitle(QCoreApplication.translate("MushafViewDialog", u"\u0645\u062a\u0635\u0641\u062d \u0627\u0644\u0642\u0631\u0622\u0646", None))
        self.selectionStartButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.selectionEndButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.selectionStartLabel.setText("")
        self.selectionEndLabel.setText("")
        self.label_16.setText(QCoreApplication.translate("MushafViewDialog", u"1. \u0627\u062e\u062a\u0631 \u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629, \u062b\u0645 \u0627\u0636\u063a\u0637 \"\u0628\u062f\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f\".\n"
"2. \u0627\u062e\u062a\u0631 \u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f (\u0641\u064a \u0646\u0641\u0633 \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0648 \u063a\u064a\u0631\u0647\u0627), \u062b\u0645 \u0627\u0636\u063a\u0637 \"\u0646\u0647\u0627\u064a\u0629 \u0627\u0644\u062a\u062d\u062f\u064a\u062f\".", None))
        self.goToPageButton.setText("")
        self.label.setText(QCoreApplication.translate("MushafViewDialog", u"\u0635\u0641\u062d\u0629", None))
        self.goToRefButton.setText("")
        self.verseInput.setText("")
        self.label_5.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0627\u064a\u0629", None))
        self.label_4.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.goToRef_2.setText("")
        self.verseInput_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631\u0642\u0645 \u0627\u0644\u0627\u064a\u0629", None))
        self.label_6.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0633\u0645 \u0627\u0644\u0633\u0648\u0631\u0629", None))
#if QT_CONFIG(tooltip)
        self.nextPushButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.nextPushButton.setText("")
        self.pageSideIcon.setText("")
#if QT_CONFIG(tooltip)
        self.prevPushButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0633\u0627\u0628\u0642\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.prevPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.nextSurahButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0633\u0648\u0631\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.nextSurahButton.setText("")
#if QT_CONFIG(tooltip)
        self.prevSurahButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0633\u0648\u0631\u0629 \u0627\u0644\u0633\u0627\u0628\u0642\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.prevSurahButton.setText("")
#if QT_CONFIG(tooltip)
        self.nextJuzButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062c\u0632\u0621 \u0627\u0644\u062a\u0627\u0644\u064a", None))
#endif // QT_CONFIG(tooltip)
        self.nextJuzButton.setText("")
#if QT_CONFIG(tooltip)
        self.prevJuzButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062c\u0632\u0621 \u0627\u0644\u0633\u0627\u0628\u0642", None))
#endif // QT_CONFIG(tooltip)
        self.prevJuzButton.setText("")
#if QT_CONFIG(tooltip)
        self.exclusiveWordsFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.differentRootCheckBox.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u0645\u062e\u062a\u0644\u0641\u0629 \u0644\u0647\u0627 \u062c\u0630\u0631 \u0645\u0634\u062a\u0631\u0643 \u062a\u0639\u062a\u0628\u0631 \u0643\u0644\u0645\u0627\u062a \u0645\u062a\u0634\u0627\u0628\u0647\u0629 (\u062a\u062c\u0631\u064a\u0628\u064a)", None))
#endif // QT_CONFIG(tooltip)
        self.differentRootCheckBox.setText(QCoreApplication.translate("MushafViewDialog", u"\u062c\u0630\u0631 \u0645\u062e\u062a\u0644\u0641", None))
#if QT_CONFIG(tooltip)
        self.refreshExclusiveWordsButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u0628\u0627\u0631\u0627\u062a \u0627\u062e\u0631\u0649", None))
#endif // QT_CONFIG(tooltip)
        self.refreshExclusiveWordsButton.setText("")
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u0628\u0627\u0631\u0627\u062a \u062a\u0638\u0647\u0631 \u0641\u0642\u0637 \u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0633\u0648\u0631\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u0628\u0627\u0631\u0627\u062a \u062d\u0635\u0631\u064a\u0629 \u0644\u0644\u0633\u0648\u0631\u0629", None))
        self.exclusivePhrasesInSurah1.setText("")
        self.exclusivePhrasesInSurah2.setText("")
        self.exclusivePhrasesInSurah3.setText("")
        self.wawIsAWordCheckbox.setText(QCoreApplication.translate("MushafViewDialog", u"\u0648\"  \u0643\u0644\u0645\u0629 \u0645\u0646\u0641\u0631\u062f\u0629\"", None))
        self.waykaannaTwoWordsCheckbox.setText(QCoreApplication.translate("MushafViewDialog", u"\u0648\u064a\u0643\u0623\u0646\"  \u0643\u0644\u0645\u062a\u0627\u0646\"", None))
        self.huroofMaaniCheckbox.setText(QCoreApplication.translate("MushafViewDialog", u"\u062d\u0631\u0648\u0641 \u0645\u0639\u0627\u0646\u064a", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629 (\u0628\u062f\u0648\u0646 \u062a\u0643\u0631\u0627\u0631)", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629 \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahUniqueWords.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u0623\u0643\u062b\u0631 \u062a\u0643\u0631\u0627\u0631\u064b\u0627 \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.mostRepeatedWord.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.resetStatsButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0645\u062d\u0648 \u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
#endif // QT_CONFIG(tooltip)
        self.resetStatsButton.setText("")
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u062c\u0645\u064a\u0639 \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f, \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.wordsInSelection.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u062c\u0645\u064a\u0639 \u0627\u0644\u0643\u0644\u0645\u0627\u062a, \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahWordsNum.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
    # retranslateUi

