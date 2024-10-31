# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from my_widgets.lazy_text_browser_widget.lazy_text_browser import LazyTextBrowser
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 873)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 20pt \"Calibri\";")
        self.arabicLangButton = QAction(MainWindow)
        self.arabicLangButton.setObjectName(u"arabicLangButton")
        self.arabicLangButton.setText(u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629")
        self.arabicLangButton.setIconText(u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629")
#if QT_CONFIG(tooltip)
        self.arabicLangButton.setToolTip(u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629")
#endif // QT_CONFIG(tooltip)
        self.englishLangButton = QAction(MainWindow)
        self.englishLangButton.setObjectName(u"englishLangButton")
        self.englishLangButton.setText(u"English")
        self.englishLangButton.setIconText(u"English")
#if QT_CONFIG(tooltip)
        self.englishLangButton.setToolTip(u"English")
#endif // QT_CONFIG(tooltip)
        self.mushafNavigationButton = QAction(MainWindow)
        self.mushafNavigationButton.setObjectName(u"mushafNavigationButton")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_22 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.searchWord = QLineEdit(self.centralwidget)
        self.searchWord.setObjectName(u"searchWord")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchWord.sizePolicy().hasHeightForWidth())
        self.searchWord.setSizePolicy(sizePolicy1)
        self.searchWord.setMaximumSize(QSize(16777215, 16777215))
        self.searchWord.setStyleSheet(u"")
        self.searchWord.setMaxLength(30)

        self.verticalLayout.addWidget(self.searchWord)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.alifAlifMaksuraCheckbox = QCheckBox(self.centralwidget)
        self.alifAlifMaksuraCheckbox.setObjectName(u"alifAlifMaksuraCheckbox")
        self.alifAlifMaksuraCheckbox.setStyleSheet(u"font: 18pt;")
        self.alifAlifMaksuraCheckbox.setText(u"\u0627 / \u0649")

        self.horizontalLayout_8.addWidget(self.alifAlifMaksuraCheckbox)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_4)

        self.yaAlifMaksuraCheckbox = QCheckBox(self.centralwidget)
        self.yaAlifMaksuraCheckbox.setObjectName(u"yaAlifMaksuraCheckbox")
        self.yaAlifMaksuraCheckbox.setEnabled(True)
        self.yaAlifMaksuraCheckbox.setStyleSheet(u"font: 18pt;")
        self.yaAlifMaksuraCheckbox.setText(u"\u0649 / \u064a")

        self.horizontalLayout_8.addWidget(self.yaAlifMaksuraCheckbox)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.finalTaCheckbox = QCheckBox(self.centralwidget)
        self.finalTaCheckbox.setObjectName(u"finalTaCheckbox")
        self.finalTaCheckbox.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.finalTaCheckbox.setFont(font)
        self.finalTaCheckbox.setStyleSheet(u"font: 18pt;")
        self.finalTaCheckbox.setText(u"\u0640\u062a / \u0640\u0629")

        self.horizontalLayout_8.addWidget(self.finalTaCheckbox)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.wordPermutationsCheckbox = QCheckBox(self.centralwidget)
        self.wordPermutationsCheckbox.setObjectName(u"wordPermutationsCheckbox")
        self.wordPermutationsCheckbox.setStyleSheet(u"font: 18pt;")
        self.wordPermutationsCheckbox.setText(u"")
        icon = QIcon()
        icon.addFile(u":/in-order-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wordPermutationsCheckbox.setIcon(icon)
        self.wordPermutationsCheckbox.setIconSize(QSize(26, 26))
        self.wordPermutationsCheckbox.setChecked(False)

        self.horizontalLayout_8.addWidget(self.wordPermutationsCheckbox)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_8)

        self.optionalAlTarifCheckbox = QCheckBox(self.centralwidget)
        self.optionalAlTarifCheckbox.setObjectName(u"optionalAlTarifCheckbox")
        self.optionalAlTarifCheckbox.setStyleSheet(u"font: 18pt;")
        self.optionalAlTarifCheckbox.setText(u"\u0627\u0644\u061f")

        self.horizontalLayout_8.addWidget(self.optionalAlTarifCheckbox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.beginningOfWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup = QButtonGroup(MainWindow)
        self.searchOptionsButtonGroup.setObjectName(u"searchOptionsButtonGroup")
        self.searchOptionsButtonGroup.addButton(self.beginningOfWordRadioButton)
        self.beginningOfWordRadioButton.setObjectName(u"beginningOfWordRadioButton")

        self.verticalLayout_2.addWidget(self.beginningOfWordRadioButton)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_13)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.endOfWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.endOfWordRadioButton)
        self.endOfWordRadioButton.setObjectName(u"endOfWordRadioButton")

        self.verticalLayout_3.addWidget(self.endOfWordRadioButton)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.fullWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.fullWordRadioButton)
        self.fullWordRadioButton.setObjectName(u"fullWordRadioButton")

        self.verticalLayout_4.addWidget(self.fullWordRadioButton)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_17)

        self.rootRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.rootRadioButton)
        self.rootRadioButton.setObjectName(u"rootRadioButton")

        self.verticalLayout_19.addWidget(self.rootRadioButton)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_18)


        self.horizontalLayout.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_19)

        self.noRestrictionsRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.noRestrictionsRadioButton)
        self.noRestrictionsRadioButton.setObjectName(u"noRestrictionsRadioButton")
        self.noRestrictionsRadioButton.setChecked(True)

        self.verticalLayout_20.addWidget(self.noRestrictionsRadioButton)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_20)


        self.horizontalLayout.addLayout(self.verticalLayout_20)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_22.addLayout(self.horizontalLayout)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.matchesNumber = QLineEdit(self.centralwidget)
        self.matchesNumber.setObjectName(u"matchesNumber")
        self.matchesNumber.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.matchesNumber.sizePolicy().hasHeightForWidth())
        self.matchesNumber.setSizePolicy(sizePolicy1)
        self.matchesNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.matchesNumber)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.matchesNumberSurahs = QLineEdit(self.centralwidget)
        self.matchesNumberSurahs.setObjectName(u"matchesNumberSurahs")
        self.matchesNumberSurahs.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.matchesNumberSurahs.sizePolicy().hasHeightForWidth())
        self.matchesNumberSurahs.setSizePolicy(sizePolicy1)
        self.matchesNumberSurahs.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.matchesNumberSurahs)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.matchesNumberVerses = QLineEdit(self.centralwidget)
        self.matchesNumberVerses.setObjectName(u"matchesNumberVerses")
        self.matchesNumberVerses.setEnabled(False)
        self.matchesNumberVerses.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.matchesNumberVerses)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)

        self.verticalLayout_22.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.ayatTab = QWidget()
        self.ayatTab.setObjectName(u"ayatTab")
        self.verticalLayout_12 = QVBoxLayout(self.ayatTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filterButton = QPushButton(self.ayatTab)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/filter-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filterButton.setIcon(icon1)
        self.filterButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.filterButton)

        self.clearFilterButton = QPushButton(self.ayatTab)
        self.clearFilterButton.setObjectName(u"clearFilterButton")
        self.clearFilterButton.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/clear-filter-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearFilterButton.setIcon(icon2)
        self.clearFilterButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.clearFilterButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.line_3 = QFrame(self.ayatTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.foundVerses = LazyTextBrowser(self.ayatTab)
        self.foundVerses.setObjectName(u"foundVerses")
        self.foundVerses.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.foundVerses.setStyleSheet(u"font-family: 'Noto Naskh Arabic'; font-size: 17pt;")

        self.verticalLayout_17.addWidget(self.foundVerses)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.colorizeCheckbox = QCheckBox(self.ayatTab)
        self.colorizeCheckbox.setObjectName(u"colorizeCheckbox")
        self.colorizeCheckbox.setChecked(True)

        self.verticalLayout_9.addWidget(self.colorizeCheckbox)

        self.verticalSpacer_9 = QSpacerItem(83, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.ayatTab, "")
        self.surahTab = QWidget()
        self.surahTab.setObjectName(u"surahTab")
        self.verticalLayout_13 = QVBoxLayout(self.surahTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sortPushButton = QPushButton(self.surahTab)
        self.sortPushButton.setObjectName(u"sortPushButton")
        self.sortPushButton.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/sort-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sortPushButton.setIcon(icon3)
        self.sortPushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.sortPushButton)

        self.sortMethodLabel = QLabel(self.surahTab)
        self.sortMethodLabel.setObjectName(u"sortMethodLabel")

        self.horizontalLayout_6.addWidget(self.sortMethodLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(self.surahTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.surahResultsListWidget = QListWidget(self.surahTab)
        self.surahResultsListWidget.setObjectName(u"surahResultsListWidget")

        self.horizontalLayout_10.addWidget(self.surahResultsListWidget)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.allResultsCheckbox = QCheckBox(self.surahTab)
        self.allResultsCheckbox.setObjectName(u"allResultsCheckbox")
        self.allResultsCheckbox.setChecked(False)

        self.verticalLayout_14.addWidget(self.allResultsCheckbox)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_16)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.surahTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.surahTab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.surahResultsSum = QLineEdit(self.surahTab)
        self.surahResultsSum.setObjectName(u"surahResultsSum")
        self.surahResultsSum.setEnabled(False)
        self.surahResultsSum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.surahResultsSum)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 8)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.surahTab, "")
        self.wordsTab = QWidget()
        self.wordsTab.setObjectName(u"wordsTab")
        self.verticalLayout_5 = QVBoxLayout(self.wordsTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.wordsSortPushButton = QPushButton(self.wordsTab)
        self.wordsSortPushButton.setObjectName(u"wordsSortPushButton")
        self.wordsSortPushButton.setEnabled(False)
        self.wordsSortPushButton.setIcon(icon3)
        self.wordsSortPushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.wordsSortPushButton)

        self.wordSortMethodLabel = QLabel(self.wordsTab)
        self.wordSortMethodLabel.setObjectName(u"wordSortMethodLabel")

        self.horizontalLayout_7.addWidget(self.wordSortMethodLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_7)

        self.line = QFrame(self.wordsTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.wordResultsListWidget = QListWidget(self.wordsTab)
        self.wordResultsListWidget.setObjectName(u"wordResultsListWidget")

        self.horizontalLayout_11.addWidget(self.wordResultsListWidget)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.diacriticsCheckbox = QCheckBox(self.wordsTab)
        self.diacriticsCheckbox.setObjectName(u"diacriticsCheckbox")
        self.diacriticsCheckbox.setChecked(True)

        self.verticalLayout_16.addWidget(self.diacriticsCheckbox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_5)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addLayout(self.verticalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.minimum_letters_restriction_lbl = QLabel(self.wordsTab)
        self.minimum_letters_restriction_lbl.setObjectName(u"minimum_letters_restriction_lbl")
        self.minimum_letters_restriction_lbl.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.verticalLayout_21.addWidget(self.minimum_letters_restriction_lbl)

        self.label_7 = QLabel(self.wordsTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.verticalLayout_21.addWidget(self.label_7)


        self.horizontalLayout_14.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.wordsTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_12.addWidget(self.label_3)

        self.wordSum = QLineEdit(self.wordsTab)
        self.wordSum.setObjectName(u"wordSum")
        self.wordSum.setEnabled(False)
        self.wordSum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.wordSum)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 8)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.tabWidget.addTab(self.wordsTab, "")

        self.verticalLayout_22.addWidget(self.tabWidget)

        self.verticalLayout_22.setStretch(0, 1)
        self.verticalLayout_22.setStretch(1, 1)
        self.verticalLayout_22.setStretch(2, 1)
        self.verticalLayout_22.setStretch(3, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 42))
        self.menu_Language = QMenu(self.menubar)
        self.menu_Language.setObjectName(u"menu_Language")
        self.menu_Language.setTitle(u"\u0627\u0644\u0644\u063a\u0629 / Language")
        icon4 = QIcon()
        icon4.addFile(u":/language-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_Language.setIcon(icon4)
        self.mushafViewButton = QMenu(self.menubar)
        self.mushafViewButton.setObjectName(u"mushafViewButton")
        icon5 = QIcon()
        icon5.addFile(u":/book-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mushafViewButton.setIcon(icon5)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.searchWord, self.beginningOfWordRadioButton)
        QWidget.setTabOrder(self.beginningOfWordRadioButton, self.endOfWordRadioButton)
        QWidget.setTabOrder(self.endOfWordRadioButton, self.fullWordRadioButton)
        QWidget.setTabOrder(self.fullWordRadioButton, self.yaAlifMaksuraCheckbox)
        QWidget.setTabOrder(self.yaAlifMaksuraCheckbox, self.finalTaCheckbox)
        QWidget.setTabOrder(self.finalTaCheckbox, self.matchesNumber)
        QWidget.setTabOrder(self.matchesNumber, self.matchesNumberSurahs)
        QWidget.setTabOrder(self.matchesNumberSurahs, self.matchesNumberVerses)
        QWidget.setTabOrder(self.matchesNumberVerses, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.filterButton)
        QWidget.setTabOrder(self.filterButton, self.clearFilterButton)
        QWidget.setTabOrder(self.clearFilterButton, self.foundVerses)
        QWidget.setTabOrder(self.foundVerses, self.colorizeCheckbox)

        self.menubar.addAction(self.menu_Language.menuAction())
        self.menubar.addAction(self.mushafViewButton.menuAction())
        self.menu_Language.addAction(self.arabicLangButton)
        self.menu_Language.addAction(self.englishLangButton)
        self.mushafViewButton.addAction(self.mushafNavigationButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u0651\u0627\u062f \u0627\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0643\u0631\u064a\u0645", None))
        self.mushafNavigationButton.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0641\u0651\u062d", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
#if QT_CONFIG(tooltip)
        self.alifAlifMaksuraCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u0645 \u0627\u0644\u062a\u0641\u0631\u064a\u0642 \u0628\u064a\u0646 '\u0627' / '\u0649'", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.yaAlifMaksuraCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u0645 \u0627\u0644\u062a\u0641\u0631\u064a\u0642 \u0628\u064a\u0646 '\u0649' / '\u064a'", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.finalTaCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u0645 \u0627\u0644\u062a\u0641\u0631\u064a\u0642 \u0628\u064a\u0646 '\u0640\u062a' / '\u0640\u0629'", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wordPermutationsCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b \u0643\u0644\u0645\u062a\u064a\u0646 \u0645\u0639 \u0627\u0645\u0643\u0627\u0646\u064a\u0629 \u0639\u0643\u0633 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.optionalAlTarifCheckbox.setToolTip(QCoreApplication.translate("MainWindow", u"\"\u0627\u0644\" \u0627\u0644\u062a\u0639\u0631\u064a\u0641 \u062e\u064a\u0627\u0631\u064a\u0629", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.beginningOfWordRadioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.beginningOfWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062f\u0627\u064a\u0629 \u0643\u0644\u0645\u0629", None))
#if QT_CONFIG(tooltip)
        self.endOfWordRadioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.endOfWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0647\u0627\u064a\u0629 \u0643\u0644\u0645\u0629", None))
#if QT_CONFIG(tooltip)
        self.fullWordRadioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fullWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0643\u0627\u0645\u0644\u0629", None))
        self.rootRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0630\u0631", None))
        self.noRestrictionsRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646 \u063a\u064a\u0631 \u062a\u0642\u064a\u064a\u062f", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u062f\u062f", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0631", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0622\u064a\u0627\u062a", None))
#if QT_CONFIG(tooltip)
        self.filterButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0641\u064a\u0629 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0628\u0645\u0633\u0627\u0639\u062f\u0629 ChatGPT", None))
#endif // QT_CONFIG(tooltip)
        self.filterButton.setText("")
#if QT_CONFIG(tooltip)
        self.clearFilterButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u063a\u0627\u0621 \u0627\u0644\u062a\u0635\u0641\u064a\u0629", None))
#endif // QT_CONFIG(tooltip)
        self.clearFilterButton.setText("")
#if QT_CONFIG(tooltip)
        self.colorizeCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colorizeCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0644\u0648\u064a\u0646", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ayatTab), QCoreApplication.translate("MainWindow", u"\u0622\u064a\u0627\u062a", None))
#if QT_CONFIG(tooltip)
        self.sortPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u063a\u0637 \u0644\u062a\u063a\u064a\u064a\u0631 \u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
#endif // QT_CONFIG(tooltip)
        self.sortPushButton.setText("")
        self.sortMethodLabel.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
#if QT_CONFIG(tooltip)
        self.allResultsCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.allResultsCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0645\u064a\u0639\n"
"\u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u0636\u063a\u0637 \u0645\u0631\u062a\u064a\u0646 \u0639\u0644\u0649 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0639\u0631\u0636 \u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u062e\u062a\u0627\u0631\u0629:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.surahTab), QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0631", None))
#if QT_CONFIG(tooltip)
        self.wordsSortPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u063a\u0637 \u0644\u062a\u063a\u064a\u064a\u0631 \u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
#endif // QT_CONFIG(tooltip)
        self.wordsSortPushButton.setText("")
        self.wordSortMethodLabel.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
        self.diacriticsCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0631\u0643\u0627\u062a", None))
        self.minimum_letters_restriction_lbl.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u062f\u062e\u0644 \u062d\u0631\u0641\u064a\u0646 \u0627\u0648 \u0627\u0643\u062b\u0631 \u0644\u0644\u0628\u062d\u062b.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u0636\u063a\u0637 \u0645\u0631\u062a\u064a\u0646 \u0639\u0644\u0649 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0639\u0631\u0636 \u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u062e\u062a\u0627\u0631\u0629:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wordsTab), QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0627\u062a", None))
        self.mushafViewButton.setTitle("")
    # retranslateUi

