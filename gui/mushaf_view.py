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
        MushafViewDialog.resize(1132, 885)
        MushafViewDialog.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 18pt \"Calibri\";")
        self.verticalLayout_4 = QVBoxLayout(MushafViewDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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
        self.nextPushButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.nextPushButton)

        self.prevPushButton = QPushButton(MushafViewDialog)
        self.prevPushButton.setObjectName(u"prevPushButton")
        self.prevPushButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.prevPushButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 6)

        self.verticalLayout_4.addLayout(self.verticalLayout)

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
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.wawIsAWordCheckbox = QCheckBox(self.frame)
        self.wawIsAWordCheckbox.setObjectName(u"wawIsAWordCheckbox")
        self.wawIsAWordCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.wawIsAWordCheckbox.setStyleSheet(u"font: bold;")
        self.wawIsAWordCheckbox.setChecked(True)

        self.verticalLayout_18.addWidget(self.wawIsAWordCheckbox)

        self.waykaannaTwoWordsCheckbox = QCheckBox(self.frame)
        self.waykaannaTwoWordsCheckbox.setObjectName(u"waykaannaTwoWordsCheckbox")
        self.waykaannaTwoWordsCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.waykaannaTwoWordsCheckbox.setStyleSheet(u"font: bold;")

        self.verticalLayout_18.addWidget(self.waykaannaTwoWordsCheckbox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_18)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_13)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.resetStatsButton = QPushButton(self.frame_3)
        self.resetStatsButton.setObjectName(u"resetStatsButton")
        icon1 = QIcon()
        icon1.addFile(u":/reset-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetStatsButton.setIcon(icon1)

        self.verticalLayout_17.addWidget(self.resetStatsButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 1, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"font: bold;")

        self.verticalLayout_13.addWidget(self.label_3)

        self.surahLettersNum = QLabel(self.frame_3)
        self.surahLettersNum.setObjectName(u"surahLettersNum")
        sizePolicy2.setHeightForWidth(self.surahLettersNum.sizePolicy().hasHeightForWidth())
        self.surahLettersNum.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.surahLettersNum.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.surahLettersNum.setLayoutDirection(Qt.LeftToRight)
        self.surahLettersNum.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.surahLettersNum.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.surahLettersNum)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.verticalLayout_13, 1, 1, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setStyleSheet(u"font: bold;")

        self.verticalLayout_14.addWidget(self.label_13)

        self.mostRepeatedLetter = QLabel(self.frame_3)
        self.mostRepeatedLetter.setObjectName(u"mostRepeatedLetter")
        sizePolicy2.setHeightForWidth(self.mostRepeatedLetter.sizePolicy().hasHeightForWidth())
        self.mostRepeatedLetter.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.mostRepeatedLetter.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.verticalLayout_14.addWidget(self.mostRepeatedLetter)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 2, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: bold;")

        self.verticalLayout_12.addWidget(self.label_2)

        self.surahWordsNum = QLabel(self.frame_3)
        self.surahWordsNum.setObjectName(u"surahWordsNum")
        sizePolicy2.setHeightForWidth(self.surahWordsNum.sizePolicy().hasHeightForWidth())
        self.surahWordsNum.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.surahWordsNum.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.surahWordsNum.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.surahWordsNum)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 2, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setStyleSheet(u"font: bold;")

        self.verticalLayout_9.addWidget(self.label_12)

        self.wordsInSelection = QLabel(self.frame_3)
        self.wordsInSelection.setObjectName(u"wordsInSelection")
        sizePolicy2.setHeightForWidth(self.wordsInSelection.sizePolicy().hasHeightForWidth())
        self.wordsInSelection.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.wordsInSelection.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.wordsInSelection.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.wordsInSelection)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 9)
        self.gridLayout_2.setColumnStretch(2, 7)

        self.horizontalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.frame)

        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 1)
        QWidget.setTabOrder(self.pageInput, self.goToPageButton)
        QWidget.setTabOrder(self.goToPageButton, self.surahNumInput)
        QWidget.setTabOrder(self.surahNumInput, self.verseInput)
        QWidget.setTabOrder(self.verseInput, self.goToRefButton)
        QWidget.setTabOrder(self.goToRefButton, self.surahNameInput)
        QWidget.setTabOrder(self.surahNameInput, self.verseInput_2)
        QWidget.setTabOrder(self.verseInput_2, self.goToRef_2)
        QWidget.setTabOrder(self.goToRef_2, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.surahNumDisplay)
        QWidget.setTabOrder(self.surahNumDisplay, self.pageNumDisplay)
        QWidget.setTabOrder(self.pageNumDisplay, self.nextPushButton)
        QWidget.setTabOrder(self.nextPushButton, self.prevPushButton)
        QWidget.setTabOrder(self.prevPushButton, self.wawIsAWordCheckbox)
        QWidget.setTabOrder(self.wawIsAWordCheckbox, self.waykaannaTwoWordsCheckbox)
        QWidget.setTabOrder(self.waykaannaTwoWordsCheckbox, self.resetStatsButton)

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
        self.label_15.setText(QCoreApplication.translate("MushafViewDialog", u"\u0635\u0641\u062d\u0629", None))
        self.label_14.setText(QCoreApplication.translate("MushafViewDialog", u"\u0633\u0648\u0631\u0629", None))
        self.nextPushButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062a\u0627\u0644\u064a", None))
        self.prevPushButton.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u0633\u0627\u0628\u0642", None))
        self.wawIsAWordCheckbox.setText(QCoreApplication.translate("MushafViewDialog", u"\u0648\"  \u0643\u0644\u0645\u0629 \u0645\u0646\u0641\u0631\u062f\u0629\"", None))
        self.waykaannaTwoWordsCheckbox.setText(QCoreApplication.translate("MushafViewDialog", u"\u0648\u064a\u0643\u0623\u0646\"  \u0643\u0644\u0645\u062a\u0627\u0646\"", None))
#if QT_CONFIG(tooltip)
        self.resetStatsButton.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0645\u062d\u0648 \u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
#endif // QT_CONFIG(tooltip)
        self.resetStatsButton.setText("")
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u062c\u0645\u064a\u0639 \u0627\u0644\u0623\u062d\u0631\u0641, \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0623\u062d\u0631\u0641 \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahLettersNum.setText("")
        self.label_13.setText(QCoreApplication.translate("MushafViewDialog", u"\u0627\u0644\u062d\u0631\u0641 \u0627\u0644\u0623\u0643\u062b\u0631 \u062a\u0643\u0631\u0627\u0631\u064b\u0627 \u0641\u064a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.mostRepeatedLetter.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u062c\u0645\u064a\u0639 \u0627\u0644\u0643\u0644\u0645\u0627\u062a, \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MushafViewDialog", u"\u0639\u062f\u062f \u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0633\u0648\u0631\u0629", None))
        self.surahWordsNum.setText("")
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("MushafViewDialog", u"\u062c\u0645\u064a\u0639 \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f, \u0645\u0639 \u062a\u0643\u0631\u0627\u0631", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MushafViewDialog", u"\u0643\u0644\u0645\u0627\u062a \u062f\u0627\u062e\u0644 \u0627\u0644\u062a\u062d\u062f\u064a\u062f", None))
        self.wordsInSelection.setText(QCoreApplication.translate("MushafViewDialog", u"0", None))
    # retranslateUi

