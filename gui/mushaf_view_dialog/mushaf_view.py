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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MushafViewDialog(object):
    def setupUi(self, MushafViewDialog):
        if not MushafViewDialog.objectName():
            MushafViewDialog.setObjectName(u"MushafViewDialog")
        MushafViewDialog.resize(1116, 853)
        icon = QIcon()
        icon.addFile(u":/app-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MushafViewDialog.setWindowIcon(icon)
        MushafViewDialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 17pt \"Calibri\";\n"
"}\n"
"\n"
"/* Line edit styling */\n"
"QLineEdit {\n"
"    border: 1px solid #4C566A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Checkbox styling */\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2px solid #81A1C1;\n"
"    border-radius: 4px;\n"
"    background-color: #3B4252;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #537EAA;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #47607E;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: #5F82AD;\n"
"    color: #2E3440;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 2px 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #81A1C1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #6E90B5;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #838383;\n"
""
                        "}\n"
"")
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

        self.gridLayout.addWidget(self.selectionStartButton, 0, 2, 1, 1)

        self.selectionEndButton = QPushButton(self.frame_2)
        self.selectionEndButton.setObjectName(u"selectionEndButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectionEndButton.sizePolicy().hasHeightForWidth())
        self.selectionEndButton.setSizePolicy(sizePolicy1)
        self.selectionEndButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.selectionEndButton, 1, 2, 1, 1)

        self.selectionStartLabel = QLabel(self.frame_2)
        self.selectionStartLabel.setObjectName(u"selectionStartLabel")

        self.gridLayout.addWidget(self.selectionStartLabel, 0, 1, 1, 1)

        self.selectionEndLabel = QLabel(self.frame_2)
        self.selectionEndLabel.setObjectName(u"selectionEndLabel")

        self.gridLayout.addWidget(self.selectionEndLabel, 1, 1, 1, 1)

        self.selectionResetButton = QPushButton(self.frame_2)
        self.selectionResetButton.setObjectName(u"selectionResetButton")
        icon1 = QIcon()
        icon1.addFile(u":/reset-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.selectionResetButton.setIcon(icon1)
        self.selectionResetButton.setAutoDefault(False)

        self.gridLayout.addWidget(self.selectionResetButton, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)

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
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.goToPageButton = QPushButton(MushafViewDialog)
        self.goToPageButton.setObjectName(u"goToPageButton")
        icon2 = QIcon()
        icon2.addFile(u":/search-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goToPageButton.setIcon(icon2)
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
        self.pageInput.setContextMenuPolicy(Qt.NoContextMenu)
        self.pageInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.pageInput)

        self.label = QLabel(MushafViewDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5.setStretch(0, 5)
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
        self.goToRefButton.setIcon(icon2)
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
        self.verseInput.setContextMenuPolicy(Qt.NoContextMenu)
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
        self.surahNumInput.setContextMenuPolicy(Qt.NoContextMenu)
        self.surahNumInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.surahNumInput)

        self.label_4 = QLabel(MushafViewDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.goToRef_2 = QPushButton(MushafViewDialog)
        self.goToRef_2.setObjectName(u"goToRef_2")
        self.goToRef_2.setIcon(icon2)
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
        self.verseInput_2.setContextMenuPolicy(Qt.NoContextMenu)
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
        self.surahNameInput.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_19.addWidget(self.surahNameInput)

        self.label_6 = QLabel(MushafViewDialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_19.addWidget(self.label_6)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(3, 6)
        self.horizontalLayout_14.setStretch(4, 8)

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
        self.frame_4.setStyleSheet(u"font-size: 15pt;")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nextPushButton = QPushButton(self.frame_4)
        self.nextPushButton.setObjectName(u"nextPushButton")
        icon3 = QIcon()
        icon3.addFile(u":/left-arrow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextPushButton.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/right-arrow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevPushButton.setIcon(icon4)
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
        self.nextSurahButton.setIcon(icon3)
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
        self.prevSurahButton.setIcon(icon4)
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
        self.nextJuzButton.setIcon(icon3)
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
        self.prevJuzButton.setIcon(icon4)
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
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
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
        self.gridLayout_2.setContentsMargins(1, 1, 8, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 8, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.differentRootCheckBox = QCheckBox(self.exclusiveWordsFrame)
        self.differentRootCheckBox.setObjectName(u"differentRootCheckBox")
        self.differentRootCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.differentRootCheckBox.setStyleSheet(u"QCheckBox{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 12pt;\n"
"	color: red;\n"
"}")

        self.horizontalLayout_3.addWidget(self.differentRootCheckBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.refreshExclusiveWordsButton = QPushButton(self.exclusiveWordsFrame)
        self.refreshExclusiveWordsButton.setObjectName(u"refreshExclusiveWordsButton")
        self.refreshExclusiveWordsButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.refreshExclusiveWordsButton.setIcon(icon1)
        self.refreshExclusiveWordsButton.setAutoDefault(False)

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
"	font: 12pt;\n"
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
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 0)
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
"	font: 12pt;\n"
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
"	font: 12pt;\n"
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
"	font: 12pt;\n"
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
        self.verticalLayout_5.setContentsMargins(0, 0, 2, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.uniqueWordsNum = QLabel(self.verticalFrame)
        self.uniqueWordsNum.setObjectName(u"uniqueWordsNum")
        sizePolicy2.setHeightForWidth(self.uniqueWordsNum.sizePolicy().hasHeightForWidth())
        self.uniqueWordsNum.setSizePolicy(sizePolicy2)
        self.uniqueWordsNum.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 12pt;\n"
"}")

        self.verticalLayout_8.addWidget(self.uniqueWordsNum)

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
        self.mostRepeatedWords = QLabel(self.verticalFrame)
        self.mostRepeatedWords.setObjectName(u"mostRepeatedWords")
        sizePolicy2.setHeightForWidth(self.mostRepeatedWords.sizePolicy().hasHeightForWidth())
        self.mostRepeatedWords.setSizePolicy(sizePolicy2)
        self.mostRepeatedWords.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 12pt;\n"
"}")

        self.verticalLayout_6.addWidget(self.mostRepeatedWords)

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
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 0)
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
        self.resetStatsButton.setIcon(icon1)
        self.resetStatsButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.resetStatsButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)


        self.verticalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.allWordsNum = QLabel(self.verticalFrame_2)
        self.allWordsNum.setObjectName(u"allWordsNum")
        sizePolicy2.setHeightForWidth(self.allWordsNum.sizePolicy().hasHeightForWidth())
        self.allWordsNum.setSizePolicy(sizePolicy2)
        self.allWordsNum.setStyleSheet(u"QLabel{\n"
"	font: bold;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 12pt;\n"
"}")

        self.verticalLayout_12.addWidget(self.allWordsNum)

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

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lettersSumTableWidget = QTableWidget(MushafViewDialog)
        if (self.lettersSumTableWidget.columnCount() < 1):
            self.lettersSumTableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.lettersSumTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.lettersSumTableWidget.rowCount() < 1):
            self.lettersSumTableWidget.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lettersSumTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lettersSumTableWidget.setItem(0, 0, __qtablewidgetitem2)
        self.lettersSumTableWidget.setObjectName(u"lettersSumTableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lettersSumTableWidget.sizePolicy().hasHeightForWidth())
        self.lettersSumTableWidget.setSizePolicy(sizePolicy3)
        self.lettersSumTableWidget.setMaximumSize(QSize(111, 85))
        self.lettersSumTableWidget.setLayoutDirection(Qt.RightToLeft)
        self.lettersSumTableWidget.setStyleSheet(u"QTableWidget {\n"
"        font-size: 12pt;\n"
"		font: bold;\n"
"    }\n"
"QHeaderView {\n"
"        font-size: 12pt;\n"
"		font: bold;\n"
"    }\n"
"\n"
"/*headers*/\n"
"QHeaderView::section {\n"
"        background-color: lightsteelblue;\n"
"        color: darkblue;\n"
"    }\n"
"/*headers when corresponding cell is selected*/\n"
"QHeaderView::section:checked {\n"
"        background-color: lightsteelblue;\n"
"        border: 1px outset darkgray;\n"
"    }\n"
"\n"
"/*corner*/\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(59, 59, 59);\n"
"    }\n"
"\n"
"/*selected item*/\n"
"QTableWidget::item:selected {\n"
"        background-color: rgba(47, 74, 97, 1.0);\n"
"        color: rgb(207, 207, 207);\n"
"        border: none;\n"
"    }\n"
"")
        self.lettersSumTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lettersSumTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lettersSumTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lettersSumTableWidget.horizontalHeader().setVisible(True)
        self.lettersSumTableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_24.addWidget(self.lettersSumTableWidget)

        self.lettersHistogram = QTableWidget(MushafViewDialog)
        if (self.lettersHistogram.columnCount() < 29):
            self.lettersHistogram.setColumnCount(29)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(20, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(21, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(22, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(23, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(24, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(25, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(26, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(27, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.lettersHistogram.setHorizontalHeaderItem(28, __qtablewidgetitem31)
        if (self.lettersHistogram.rowCount() < 1):
            self.lettersHistogram.setRowCount(1)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setText(u"0");
        self.lettersHistogram.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 9, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 10, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 11, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 12, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 13, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 14, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 15, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 16, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 17, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 18, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 19, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 20, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 21, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 22, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 23, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 24, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 25, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 26, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 27, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.lettersHistogram.setItem(0, 28, __qtablewidgetitem60)
        self.lettersHistogram.setObjectName(u"lettersHistogram")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lettersHistogram.sizePolicy().hasHeightForWidth())
        self.lettersHistogram.setSizePolicy(sizePolicy4)
        self.lettersHistogram.setMaximumSize(QSize(16777215, 85))
        self.lettersHistogram.setLayoutDirection(Qt.RightToLeft)
        self.lettersHistogram.setStyleSheet(u"\n"
"QTableWidget {\n"
"        font-size: 12pt;\n"
"    }\n"
"QHeaderView {\n"
"        font-size: 12pt;\n"
"    }\n"
"\n"
"/*headers*/\n"
"QHeaderView::section {\n"
"        background-color: lightsteelblue;\n"
"        color: darkblue;\n"
"    }\n"
"/*headers when corresponding cell is selected*/\n"
"QHeaderView::section:checked {\n"
"        background-color: lightsteelblue;\n"
"        border: 1px outset darkgray;\n"
"    }\n"
"\n"
"/*corner*/\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(59, 59, 59);\n"
"    }\n"
"\n"
"/*selected item*/\n"
"QTableWidget::item:selected {\n"
"        background-color: rgba(47, 74, 97, 1.0);\n"
"        color: rgb(207, 207, 207);\n"
"        border: none;\n"
"    }\n"
"")
        self.lettersHistogram.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lettersHistogram.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lettersHistogram.setRowCount(1)
        self.lettersHistogram.setColumnCount(29)
        self.lettersHistogram.verticalHeader().setVisible(False)

        self.horizontalLayout_24.addWidget(self.lettersHistogram)

        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_24)

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
        self.selectionResetButton.setText("")
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
        self.differentRootCheckBox.setToolTip(QCoreApplication.translate("MushafViewDialog", u"(\u062a\u062c\u0631\u064a\u0628\u064a)", None))
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
        self.uniqueWordsNum.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629 (\u0628\u062f\u0648\u0646 \u062a\u0643\u0631\u0627\u0631) \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629 / \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
#endif // QT_CONFIG(tooltip)
        self.uniqueWordsNum.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629", None))
        self.surahUniqueWords.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.mostRepeatedWords.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u0623\u0643\u062b\u0631 \u062a\u0643\u0631\u0627\u0631\u064b\u0627 \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629 / \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
#endif // QT_CONFIG(tooltip)
        self.mostRepeatedWords.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u0623\u0643\u062b\u0631 \u062a\u0643\u0631\u0627\u0631\u064b\u0627", None))
        self.mostRepeatedWord.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.resetStatsButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0645\u062d\u0648 \u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
#endif // QT_CONFIG(tooltip)
        self.resetStatsButton.setText("")
#if QT_CONFIG(tooltip)
        self.allWordsNum.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u062c\u0645\u064a\u0639 \u0627\u0644\u0643\u0644\u0645\u0627\u062a (\u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629 / \u0627\u0644\u062a\u062d\u062f\u064a\u062f), \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.allWordsNum.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0627\u0644\u0643\u0644\u0645\u0627\u062a", None))
        self.surahWordsNum.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
        ___qtablewidgetitem = self.lettersSumTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0645\u062c\u0645\u0648\u0639", None));
        ___qtablewidgetitem1 = self.lettersSumTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));

        __sortingEnabled = self.lettersSumTableWidget.isSortingEnabled()
        self.lettersSumTableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.lettersSumTableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        self.lettersSumTableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.lettersSumTableWidget.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u062d\u0631\u0648\u0641", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.lettersHistogram.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627", None));
        ___qtablewidgetitem4 = self.lettersHistogram.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MushafViewDialog", u"\u0628", None));
        ___qtablewidgetitem5 = self.lettersHistogram.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MushafViewDialog", u"\u062a / \u0640\u0629", None));
        ___qtablewidgetitem6 = self.lettersHistogram.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MushafViewDialog", u"\u062b", None));
        ___qtablewidgetitem7 = self.lettersHistogram.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MushafViewDialog", u"\u062c", None));
        ___qtablewidgetitem8 = self.lettersHistogram.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MushafViewDialog", u"\u062d", None));
        ___qtablewidgetitem9 = self.lettersHistogram.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MushafViewDialog", u"\u062e", None));
        ___qtablewidgetitem10 = self.lettersHistogram.horizontalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MushafViewDialog", u"\u062f", None));
        ___qtablewidgetitem11 = self.lettersHistogram.horizontalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MushafViewDialog", u"\u0630", None));
        ___qtablewidgetitem12 = self.lettersHistogram.horizontalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MushafViewDialog", u"\u0631", None));
        ___qtablewidgetitem13 = self.lettersHistogram.horizontalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MushafViewDialog", u"\u0632", None));
        ___qtablewidgetitem14 = self.lettersHistogram.horizontalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MushafViewDialog", u"\u0633", None));
        ___qtablewidgetitem15 = self.lettersHistogram.horizontalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MushafViewDialog", u"\u0634", None));
        ___qtablewidgetitem16 = self.lettersHistogram.horizontalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MushafViewDialog", u"\u0635", None));
        ___qtablewidgetitem17 = self.lettersHistogram.horizontalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MushafViewDialog", u"\u0636", None));
        ___qtablewidgetitem18 = self.lettersHistogram.horizontalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MushafViewDialog", u"\u0637", None));
        ___qtablewidgetitem19 = self.lettersHistogram.horizontalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MushafViewDialog", u"\u0638", None));
        ___qtablewidgetitem20 = self.lettersHistogram.horizontalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639", None));
        ___qtablewidgetitem21 = self.lettersHistogram.horizontalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MushafViewDialog", u"\u063a", None));
        ___qtablewidgetitem22 = self.lettersHistogram.horizontalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MushafViewDialog", u"\u0641", None));
        ___qtablewidgetitem23 = self.lettersHistogram.horizontalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MushafViewDialog", u"\u0642", None));
        ___qtablewidgetitem24 = self.lettersHistogram.horizontalHeaderItem(21)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643", None));
        ___qtablewidgetitem25 = self.lettersHistogram.horizontalHeaderItem(22)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MushafViewDialog", u"\u0644", None));
        ___qtablewidgetitem26 = self.lettersHistogram.horizontalHeaderItem(23)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MushafViewDialog", u"\u0645", None));
        ___qtablewidgetitem27 = self.lettersHistogram.horizontalHeaderItem(24)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MushafViewDialog", u"\u0646", None));
        ___qtablewidgetitem28 = self.lettersHistogram.horizontalHeaderItem(25)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MushafViewDialog", u"\u0647", None));
        ___qtablewidgetitem29 = self.lettersHistogram.horizontalHeaderItem(26)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MushafViewDialog", u"\u0648", None));
        ___qtablewidgetitem30 = self.lettersHistogram.horizontalHeaderItem(27)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MushafViewDialog", u"\u064a / \u0649", None));
        ___qtablewidgetitem31 = self.lettersHistogram.horizontalHeaderItem(28)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MushafViewDialog", u"\u0621 / \u0624 / \u0626", None));

        __sortingEnabled1 = self.lettersHistogram.isSortingEnabled()
        self.lettersHistogram.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.lettersHistogram.item(0, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem33 = self.lettersHistogram.item(0, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem34 = self.lettersHistogram.item(0, 3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem35 = self.lettersHistogram.item(0, 4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem36 = self.lettersHistogram.item(0, 5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem37 = self.lettersHistogram.item(0, 6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem38 = self.lettersHistogram.item(0, 7)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem39 = self.lettersHistogram.item(0, 8)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem40 = self.lettersHistogram.item(0, 9)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem41 = self.lettersHistogram.item(0, 10)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem42 = self.lettersHistogram.item(0, 11)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem43 = self.lettersHistogram.item(0, 12)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem44 = self.lettersHistogram.item(0, 13)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem45 = self.lettersHistogram.item(0, 14)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem46 = self.lettersHistogram.item(0, 15)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem47 = self.lettersHistogram.item(0, 16)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem48 = self.lettersHistogram.item(0, 17)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem49 = self.lettersHistogram.item(0, 18)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem50 = self.lettersHistogram.item(0, 19)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem51 = self.lettersHistogram.item(0, 20)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem52 = self.lettersHistogram.item(0, 21)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem53 = self.lettersHistogram.item(0, 22)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem54 = self.lettersHistogram.item(0, 23)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem55 = self.lettersHistogram.item(0, 24)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem56 = self.lettersHistogram.item(0, 25)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem57 = self.lettersHistogram.item(0, 26)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem58 = self.lettersHistogram.item(0, 27)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        ___qtablewidgetitem59 = self.lettersHistogram.item(0, 28)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MushafViewDialog", u"0", None));
        self.lettersHistogram.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

