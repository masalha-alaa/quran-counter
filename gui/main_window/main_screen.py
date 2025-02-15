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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from my_widgets.lazy_text_browser_widget.lazy_text_browser import LazyTextBrowser
from my_widgets.surah_lazy_table_widget import SurahLazyTableWidget
from my_widgets.topic_lazy_table_widget import TopicLazyTableWidget
from my_widgets.word_lazy_table_widget import WordLazyTableWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1179, 873)
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 20pt \"Calibri\";\n"
"}\n"
"\n"
"QMenuBar, QMenu {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #4A90E2, stop:1 #D0021B\n"
"    );\n"
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
"QCheckBox::indicator:hover {\n"
"    background-color: #47607E;\n"
"}\n"
"\n"
"/* Radio button styling */\n"
"QRadioButton {\n"
"    color: #D8DEE9;\n"
"    font: 19pt;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border: 2px solid #81A1C1;\n"
"    border-radius: 9px;\n"
"    background-color: #3B4252;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #"
                        "537EAA;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
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
"}\n"
"\n"
"/* Line edit styling */\n"
"QLineEdit {\n"
"    border: 1px solid #4C566A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Slider */\n"
"QSlider::handle:horizontal {\n"
"    background: #3498DB;\n"
"    border: 1px solid #2488CB;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #44A8EB;\n"
"    border: 1px solid #2488CB;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #3094D7;\n"
"    border: 1px solid #2488CB;\n"
""
                        "    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #CCCCCC;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"}")
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
        self.enterGptKeyButton = QAction(MainWindow)
        self.enterGptKeyButton.setObjectName(u"enterGptKeyButton")
        self.aboutMenuButton = QAction(MainWindow)
        self.aboutMenuButton.setObjectName(u"aboutMenuButton")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"")

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
        self.alifAlifMaksuraCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: 18pt;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
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
        self.yaAlifMaksuraCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: 18pt;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.yaAlifMaksuraCheckbox.setText(u"\u0649 / \u064a")
        self.yaAlifMaksuraCheckbox.setChecked(False)

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
        self.finalTaCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: 18pt;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.finalTaCheckbox.setText(u"\u0640\u062a / \u0640\u0629")

        self.horizontalLayout_8.addWidget(self.finalTaCheckbox)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.wordPermutationsCheckbox = QCheckBox(self.centralwidget)
        self.wordPermutationsCheckbox.setObjectName(u"wordPermutationsCheckbox")
        self.wordPermutationsCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: 18pt;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
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
        self.optionalAlTarifCheckbox.setStyleSheet(u"QCheckBox{\n"
"	font: 18pt;\n"
"}\n"
"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}")
        self.optionalAlTarifCheckbox.setText(u"\u0627\u0644\u061f")

        self.horizontalLayout_8.addWidget(self.optionalAlTarifCheckbox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, 30, -1, -1)
        self.beginningOfWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup = QButtonGroup(MainWindow)
        self.searchOptionsButtonGroup.setObjectName(u"searchOptionsButtonGroup")
        self.searchOptionsButtonGroup.addButton(self.beginningOfWordRadioButton)
        self.beginningOfWordRadioButton.setObjectName(u"beginningOfWordRadioButton")
        self.beginningOfWordRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.beginningOfWordRadioButton, 0, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.noRestrictionsRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.noRestrictionsRadioButton)
        self.noRestrictionsRadioButton.setObjectName(u"noRestrictionsRadioButton")
        self.noRestrictionsRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")
        self.noRestrictionsRadioButton.setChecked(True)

        self.verticalLayout_20.addWidget(self.noRestrictionsRadioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_20, 1, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.similarWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.similarWordRadioButton)
        self.similarWordRadioButton.setObjectName(u"similarWordRadioButton")
        self.similarWordRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.similarWordRadioButton)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15.setContentsMargins(-1, -1, 19, -1)
        self.similarityThresholdSlider = QSlider(self.centralwidget)
        self.similarityThresholdSlider.setObjectName(u"similarityThresholdSlider")
        self.similarityThresholdSlider.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.similarityThresholdSlider.sizePolicy().hasHeightForWidth())
        self.similarityThresholdSlider.setSizePolicy(sizePolicy2)
        self.similarityThresholdSlider.setMinimum(1)
        self.similarityThresholdSlider.setMaximum(5)
        self.similarityThresholdSlider.setPageStep(2)
        self.similarityThresholdSlider.setValue(1)
        self.similarityThresholdSlider.setOrientation(Qt.Horizontal)
        self.similarityThresholdSlider.setInvertedAppearance(True)
        self.similarityThresholdSlider.setInvertedControls(False)
        self.similarityThresholdSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_15.addWidget(self.similarityThresholdSlider)

        self.similarityThresholdLabel = QLabel(self.centralwidget)
        self.similarityThresholdLabel.setObjectName(u"similarityThresholdLabel")
        self.similarityThresholdLabel.setStyleSheet(u"font-size: 15pt;")
        self.similarityThresholdLabel.setText(u"1")
        self.similarityThresholdLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.similarityThresholdLabel.setMargin(1)
        self.similarityThresholdLabel.setIndent(-1)

        self.horizontalLayout_15.addWidget(self.similarityThresholdLabel)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)


        self.gridLayout.addLayout(self.verticalLayout_18, 1, 1, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.regexRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.regexRadioButton)
        self.regexRadioButton.setObjectName(u"regexRadioButton")
#if QT_CONFIG(tooltip)
        self.regexRadioButton.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.regexRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")
        self.regexRadioButton.setChecked(False)

        self.verticalLayout_23.addWidget(self.regexRadioButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_23, 1, 4, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.topicsRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.topicsRadioButton)
        self.topicsRadioButton.setObjectName(u"topicsRadioButton")
#if QT_CONFIG(tooltip)
        self.topicsRadioButton.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.topicsRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")
        self.topicsRadioButton.setChecked(False)

        self.verticalLayout_24.addWidget(self.topicsRadioButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_24, 1, 3, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.relatedWordsRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.relatedWordsRadioButton)
        self.relatedWordsRadioButton.setObjectName(u"relatedWordsRadioButton")
        self.relatedWordsRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.relatedWordsRadioButton)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(-1, -1, 19, -1)
        self.relatedWordsThresholdSlider = QSlider(self.centralwidget)
        self.relatedWordsThresholdSlider.setObjectName(u"relatedWordsThresholdSlider")
        self.relatedWordsThresholdSlider.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.relatedWordsThresholdSlider.sizePolicy().hasHeightForWidth())
        self.relatedWordsThresholdSlider.setSizePolicy(sizePolicy2)
        self.relatedWordsThresholdSlider.setMinimum(1)
        self.relatedWordsThresholdSlider.setMaximum(5)
        self.relatedWordsThresholdSlider.setPageStep(2)
        self.relatedWordsThresholdSlider.setValue(1)
        self.relatedWordsThresholdSlider.setOrientation(Qt.Horizontal)
        self.relatedWordsThresholdSlider.setInvertedAppearance(True)
        self.relatedWordsThresholdSlider.setInvertedControls(False)
        self.relatedWordsThresholdSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_18.addWidget(self.relatedWordsThresholdSlider)

        self.relatedWordsThresholdLabel = QLabel(self.centralwidget)
        self.relatedWordsThresholdLabel.setObjectName(u"relatedWordsThresholdLabel")
        self.relatedWordsThresholdLabel.setStyleSheet(u"font-size: 15pt;")
        self.relatedWordsThresholdLabel.setText(u"1")
        self.relatedWordsThresholdLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.relatedWordsThresholdLabel.setMargin(1)
        self.relatedWordsThresholdLabel.setIndent(-1)

        self.horizontalLayout_18.addWidget(self.relatedWordsThresholdLabel)


        self.verticalLayout_19.addLayout(self.horizontalLayout_18)


        self.gridLayout.addLayout(self.verticalLayout_19, 1, 2, 1, 1)

        self.rootRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.rootRadioButton)
        self.rootRadioButton.setObjectName(u"rootRadioButton")
        self.rootRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.rootRadioButton, 0, 3, 1, 1)

        self.endOfWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.endOfWordRadioButton)
        self.endOfWordRadioButton.setObjectName(u"endOfWordRadioButton")
        self.endOfWordRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.endOfWordRadioButton, 0, 1, 1, 1)

        self.fullWordRadioButton = QRadioButton(self.centralwidget)
        self.searchOptionsButtonGroup.addButton(self.fullWordRadioButton)
        self.fullWordRadioButton.setObjectName(u"fullWordRadioButton")
        self.fullWordRadioButton.setStyleSheet(u"QToolTip { \n"
"    color: #484848;\n"
"	font: 14pt;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.fullWordRadioButton, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

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

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet(u"QTabBar::tab:selected {\n"
"    color: rgb(80, 160, 255);\n"
"}\n"
"")
        self.tabWidget.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.ayatTab = QWidget()
        self.ayatTab.setObjectName(u"ayatTab")
        self.ayatTab.setStyleSheet(u"")
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
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.surahResultsTableWidget = SurahLazyTableWidget(self.surahTab)
        self.surahResultsTableWidget.setObjectName(u"surahResultsTableWidget")
        self.surahResultsTableWidget.setMouseTracking(True)
        self.surahResultsTableWidget.setFocusPolicy(Qt.NoFocus)
        self.surahResultsTableWidget.setStyleSheet(u"QTableWidget {\n"
"        font-size: 17pt;\n"
"    }\n"
"QHeaderView {\n"
"        font-size: 17pt;\n"
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
        self.surahResultsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.surahResultsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.surahResultsTableWidget.setSortingEnabled(False)
        self.surahResultsTableWidget.setRowCount(0)
        self.surahResultsTableWidget.setColumnCount(0)
        self.surahResultsTableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.surahResultsTableWidget.verticalHeader().setProperty(u"showSortIndicator", False)

        self.horizontalLayout_10.addWidget(self.surahResultsTableWidget)


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
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.wordResultsTableWidget = WordLazyTableWidget(self.wordsTab)
        self.wordResultsTableWidget.setObjectName(u"wordResultsTableWidget")
        self.wordResultsTableWidget.setMouseTracking(True)
        self.wordResultsTableWidget.setFocusPolicy(Qt.NoFocus)
        self.wordResultsTableWidget.setLayoutDirection(Qt.RightToLeft)
        self.wordResultsTableWidget.setStyleSheet(u"QTableWidget {\n"
"        font-size: 17pt;\n"
"    }\n"
"QHeaderView {\n"
"        font-size: 17pt;\n"
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
        self.wordResultsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.wordResultsTableWidget.setTabKeyNavigation(True)
        self.wordResultsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.wordResultsTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.wordResultsTableWidget.setSortingEnabled(False)
        self.wordResultsTableWidget.setRowCount(0)
        self.wordResultsTableWidget.setColumnCount(0)
        self.wordResultsTableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)

        self.horizontalLayout_11.addWidget(self.wordResultsTableWidget)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.diacriticsCheckbox = QCheckBox(self.wordsTab)
        self.diacriticsCheckbox.setObjectName(u"diacriticsCheckbox")
        self.diacriticsCheckbox.setStyleSheet(u"margin-top:15px;")
        self.diacriticsCheckbox.setChecked(True)

        self.verticalLayout_16.addWidget(self.diacriticsCheckbox)

        self.line_2 = QFrame(self.wordsTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_2)

        self.wordTransliterationCheckbox = QCheckBox(self.wordsTab)
        self.wordTransliterationCheckbox.setObjectName(u"wordTransliterationCheckbox")
        self.wordTransliterationCheckbox.setStyleSheet(u"font: 12pt;")
        self.wordTransliterationCheckbox.setChecked(True)

        self.verticalLayout_16.addWidget(self.wordTransliterationCheckbox)

        self.wordMeaningCheckbox = QCheckBox(self.wordsTab)
        self.wordMeaningCheckbox.setObjectName(u"wordMeaningCheckbox")
        self.wordMeaningCheckbox.setStyleSheet(u"font: 12pt;")
        self.wordMeaningCheckbox.setChecked(True)

        self.verticalLayout_16.addWidget(self.wordMeaningCheckbox)

        self.line_9 = QFrame(self.wordsTab)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_5)

        self.verticalLayout_16.setStretch(0, 2)
        self.verticalLayout_16.setStretch(5, 25)

        self.horizontalLayout_11.addLayout(self.verticalLayout_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

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
        self.topicsTab = QWidget()
        self.topicsTab.setObjectName(u"topicsTab")
        self.verticalLayout_3 = QVBoxLayout(self.topicsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.topicResultsTableWidget = TopicLazyTableWidget(self.topicsTab)
        self.topicResultsTableWidget.setObjectName(u"topicResultsTableWidget")
        self.topicResultsTableWidget.setMouseTracking(True)
        self.topicResultsTableWidget.setFocusPolicy(Qt.NoFocus)
        self.topicResultsTableWidget.setStyleSheet(u"QTableWidget {\n"
"        font-size: 17pt;\n"
"    }\n"
"QHeaderView {\n"
"        font-size: 17pt;\n"
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
        self.topicResultsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.topicResultsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.topicResultsTableWidget.setSortingEnabled(False)
        self.topicResultsTableWidget.setRowCount(0)
        self.topicResultsTableWidget.setColumnCount(0)

        self.horizontalLayout_6.addWidget(self.topicResultsTableWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.minimum_letters_restriction_lbl_2 = QLabel(self.topicsTab)
        self.minimum_letters_restriction_lbl_2.setObjectName(u"minimum_letters_restriction_lbl_2")
        self.minimum_letters_restriction_lbl_2.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.verticalLayout_22.addWidget(self.minimum_letters_restriction_lbl_2)

        self.label_10 = QLabel(self.topicsTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: italic 400 10pt \"Calibri\";")

        self.verticalLayout_22.addWidget(self.label_10)


        self.horizontalLayout_17.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.topicsTab)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_16.addWidget(self.label_9)

        self.topicSum = QLineEdit(self.topicsTab)
        self.topicSum.setObjectName(u"topicSum")
        self.topicSum.setEnabled(False)
        self.topicSum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.topicSum)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 8)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.tabWidget.addTab(self.topicsTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1179, 42))
        self.menu_Language = QMenu(self.menubar)
        self.menu_Language.setObjectName(u"menu_Language")
#if QT_CONFIG(tooltip)
        self.menu_Language.setToolTip(u"\u0627\u0644\u0644\u063a\u0629 / Language")
#endif // QT_CONFIG(tooltip)
        self.menu_Language.setTitle(u"")
        icon3 = QIcon()
        icon3.addFile(u":/language-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_Language.setIcon(icon3)
        self.menu_Language.setToolTipsVisible(True)
        self.mushafViewButton = QMenu(self.menubar)
        self.mushafViewButton.setObjectName(u"mushafViewButton")
        self.mushafViewButton.setTitle(u"")
        icon4 = QIcon()
        icon4.addFile(u":/book-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mushafViewButton.setIcon(icon4)
        self.mushafViewButton.setToolTipsVisible(True)
        self.menuChatGPT = QMenu(self.menubar)
        self.menuChatGPT.setObjectName(u"menuChatGPT")
        self.menuChatGPT.setTitle(u"")
        icon5 = QIcon()
        icon5.addFile(u":/chatgpt-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuChatGPT.setIcon(icon5)
        self.menuChatGPT.setToolTipsVisible(True)
        self.helpMenuButton = QMenu(self.menubar)
        self.helpMenuButton.setObjectName(u"helpMenuButton")
        self.helpMenuButton.setTitle(u"?")
        self.helpMenuButton.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.searchWord, self.noRestrictionsRadioButton)
        QWidget.setTabOrder(self.noRestrictionsRadioButton, self.similarWordRadioButton)
        QWidget.setTabOrder(self.similarWordRadioButton, self.similarityThresholdSlider)
        QWidget.setTabOrder(self.similarityThresholdSlider, self.regexRadioButton)
        QWidget.setTabOrder(self.regexRadioButton, self.alifAlifMaksuraCheckbox)
        QWidget.setTabOrder(self.alifAlifMaksuraCheckbox, self.yaAlifMaksuraCheckbox)
        QWidget.setTabOrder(self.yaAlifMaksuraCheckbox, self.finalTaCheckbox)
        QWidget.setTabOrder(self.finalTaCheckbox, self.wordPermutationsCheckbox)
        QWidget.setTabOrder(self.wordPermutationsCheckbox, self.optionalAlTarifCheckbox)
        QWidget.setTabOrder(self.optionalAlTarifCheckbox, self.matchesNumber)
        QWidget.setTabOrder(self.matchesNumber, self.matchesNumberSurahs)
        QWidget.setTabOrder(self.matchesNumberSurahs, self.matchesNumberVerses)
        QWidget.setTabOrder(self.matchesNumberVerses, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.foundVerses)
        QWidget.setTabOrder(self.foundVerses, self.filterButton)
        QWidget.setTabOrder(self.filterButton, self.clearFilterButton)
        QWidget.setTabOrder(self.clearFilterButton, self.colorizeCheckbox)
        QWidget.setTabOrder(self.colorizeCheckbox, self.allResultsCheckbox)
        QWidget.setTabOrder(self.allResultsCheckbox, self.surahResultsSum)
        QWidget.setTabOrder(self.surahResultsSum, self.diacriticsCheckbox)
        QWidget.setTabOrder(self.diacriticsCheckbox, self.wordSum)

        self.menubar.addAction(self.menu_Language.menuAction())
        self.menubar.addAction(self.mushafViewButton.menuAction())
        self.menubar.addAction(self.menuChatGPT.menuAction())
        self.menubar.addAction(self.helpMenuButton.menuAction())
        self.menu_Language.addAction(self.arabicLangButton)
        self.menu_Language.addAction(self.englishLangButton)
        self.mushafViewButton.addAction(self.mushafNavigationButton)
        self.menuChatGPT.addAction(self.enterGptKeyButton)
        self.helpMenuButton.addAction(self.aboutMenuButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u0651\u0627\u062f \u0627\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0643\u0631\u064a\u0645", None))
        self.mushafNavigationButton.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0641\u0651\u062d", None))
#if QT_CONFIG(tooltip)
        self.mushafNavigationButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0641\u0651\u062d", None))
#endif // QT_CONFIG(tooltip)
        self.enterGptKeyButton.setText(QCoreApplication.translate("MainWindow", u"ChatGPT \u0625\u062f\u062e\u0627\u0644 \u0645\u0641\u062a\u0627\u062d", None))
        self.aboutMenuButton.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0648\u0644 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c", None))
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
        self.noRestrictionsRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646 \u063a\u064a\u0631 \u062a\u0642\u064a\u064a\u062f", None))
#if QT_CONFIG(tooltip)
        self.similarWordRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0627\u062a \u0645\u0634\u0627\u0628\u0647\u0629 (\u0641\u064a \u0627\u0644\u0635\u064a\u0627\u063a\u0629 \u0648\u0644\u064a\u0633 \u0641\u064a \u0627\u0644\u0645\u0639\u0646\u0649)", None))
#endif // QT_CONFIG(tooltip)
        self.similarWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0645\u0634\u0627\u0628\u0647\u0629", None))
#if QT_CONFIG(tooltip)
        self.similarityThresholdSlider.setToolTip(QCoreApplication.translate("MainWindow", u"\u0639\u062a\u0628\u0629 \u0627\u0644\u062a\u0634\u0627\u0628\u0647", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.similarityThresholdLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.regexRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0631\u064a\u0686\u064a\u0643\u0633", None))
        self.topicsRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0627\u0636\u064a\u0639", None))
#if QT_CONFIG(tooltip)
        self.relatedWordsRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0627\u062a \u0645\u0634\u0627\u0628\u0647\u0629 (\u0641\u064a \u0627\u0644\u0635\u064a\u0627\u063a\u0629 \u0648\u0644\u064a\u0633 \u0641\u064a \u0627\u0644\u0645\u0639\u0646\u0649)", None))
#endif // QT_CONFIG(tooltip)
        self.relatedWordsRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0630\u0627\u062a \u0635\u0644\u0629", None))
#if QT_CONFIG(tooltip)
        self.relatedWordsThresholdSlider.setToolTip(QCoreApplication.translate("MainWindow", u"\u0639\u062a\u0628\u0629 \u0627\u0644\u062a\u0634\u0627\u0628\u0647", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.relatedWordsThresholdLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rootRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0627\u062a \u0628\u0646\u0641\u0633 \u062c\u0630\u0631 \u0643\u0644\u0645\u0629 \u0627\u0644\u0628\u062d\u062b", None))
#endif // QT_CONFIG(tooltip)
        self.rootRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0630\u0631", None))
#if QT_CONFIG(tooltip)
        self.endOfWordRadioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.endOfWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0647\u0627\u064a\u0629 \u0643\u0644\u0645\u0629", None))
#if QT_CONFIG(tooltip)
        self.fullWordRadioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fullWordRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0643\u0627\u0645\u0644\u0629", None))
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
        self.allResultsCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.allResultsCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0645\u064a\u0639\n"
"\u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u0636\u063a\u0637 \u0645\u0631\u062a\u064a\u0646 \u0639\u0644\u0649 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0639\u0631\u0636 \u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u062e\u062a\u0627\u0631\u0629:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.surahTab), QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0631", None))
        self.diacriticsCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062d\u0631\u0643\u0627\u062a", None))
        self.wordTransliterationCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062d\u064e\u0648\u0631\u064e\u0641\u064e\u0629", None))
        self.wordMeaningCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0631\u062c\u0645\u0629", None))
        self.minimum_letters_restriction_lbl.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u062f\u062e\u0644 \u062d\u0631\u0641\u064a\u0646 \u0627\u0648 \u0627\u0643\u062b\u0631 \u0644\u0644\u0628\u062d\u062b.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u0636\u063a\u0637 \u0645\u0631\u062a\u064a\u0646 \u0639\u0644\u0649 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0639\u0631\u0636 \u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u062e\u062a\u0627\u0631\u0629:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wordsTab), QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0627\u062a", None))
        self.minimum_letters_restriction_lbl_2.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u062f\u062e\u0644 \u062d\u0631\u0641\u064a\u0646 \u0627\u0648 \u0627\u0643\u062b\u0631 \u0644\u0644\u0628\u062d\u062b.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"* \u0627\u0636\u063a\u0637 \u0645\u0631\u062a\u064a\u0646 \u0639\u0644\u0649 \u0627\u0644\u0646\u062a\u064a\u062c\u0629 \u0644\u0639\u0631\u0636 \u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0627\u0644\u0645\u062e\u062a\u0627\u0631\u0629:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.topicsTab), QCoreApplication.translate("MainWindow", u"\u0645\u0648\u0627\u0636\u064a\u0639", None))
#if QT_CONFIG(tooltip)
        self.mushafViewButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0635\u062d\u0641", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.menuChatGPT.setToolTip(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0630\u0643\u0627\u0621 \u0627\u0644\u0627\u0635\u0637\u0646\u0627\u0639\u064a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.helpMenuButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0645\u0633\u0627\u0639\u062f\u0629", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

