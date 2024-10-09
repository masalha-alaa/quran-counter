# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 701)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 20pt \"Calibri\";")
        self.arabicLangButton = QAction(MainWindow)
        self.arabicLangButton.setObjectName(u"arabicLangButton")
        self.englishLangButton = QAction(MainWindow)
        self.englishLangButton.setObjectName(u"englishLangButton")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchWord.sizePolicy().hasHeightForWidth())
        self.searchWord.setSizePolicy(sizePolicy1)
        self.searchWord.setMaximumSize(QSize(16777215, 16777215))
        self.searchWord.setStyleSheet(u"")
        self.searchWord.setMaxLength(40)

        self.verticalLayout.addWidget(self.searchWord)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.yaAlifMaksuraCheckbox = QCheckBox(self.centralwidget)
        self.yaAlifMaksuraCheckbox.setObjectName(u"yaAlifMaksuraCheckbox")
        self.yaAlifMaksuraCheckbox.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.yaAlifMaksuraCheckbox)

        self.finalTaCheckbox = QCheckBox(self.centralwidget)
        self.finalTaCheckbox.setObjectName(u"finalTaCheckbox")
        self.finalTaCheckbox.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.finalTaCheckbox.setFont(font)

        self.horizontalLayout_8.addWidget(self.finalTaCheckbox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.beginningOfWordCheckbox = QCheckBox(self.centralwidget)
        self.beginningOfWordCheckbox.setObjectName(u"beginningOfWordCheckbox")

        self.verticalLayout_2.addWidget(self.beginningOfWordCheckbox)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_13)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.endOfWordCheckbox = QCheckBox(self.centralwidget)
        self.endOfWordCheckbox.setObjectName(u"endOfWordCheckbox")

        self.verticalLayout_3.addWidget(self.endOfWordCheckbox)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.fullWordcheckbox = QCheckBox(self.centralwidget)
        self.fullWordcheckbox.setObjectName(u"fullWordcheckbox")

        self.verticalLayout_4.addWidget(self.fullWordcheckbox)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(58, 48, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.matchesNumber.sizePolicy().hasHeightForWidth())
        self.matchesNumber.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.matchesNumberSurahs.sizePolicy().hasHeightForWidth())
        self.matchesNumberSurahs.setSizePolicy(sizePolicy2)
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

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

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
        icon = QIcon()
        icon.addFile(u":/filter-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filterButton.setIcon(icon)
        self.filterButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.filterButton)

        self.clearFilterButton = QPushButton(self.ayatTab)
        self.clearFilterButton.setObjectName(u"clearFilterButton")
        self.clearFilterButton.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/clear-filter-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearFilterButton.setIcon(icon1)
        self.clearFilterButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.clearFilterButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.foundVerses = QTextBrowser(self.ayatTab)
        self.foundVerses.setObjectName(u"foundVerses")
        self.foundVerses.setStyleSheet(u"font-family: 'Noto Naskh Arabic'; font-size: 17pt;")

        self.horizontalLayout_4.addWidget(self.foundVerses)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

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
        icon2 = QIcon()
        icon2.addFile(u":/sort-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sortPushButton.setIcon(icon2)
        self.sortPushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.sortPushButton)

        self.sortMethodLabel = QLabel(self.surahTab)
        self.sortMethodLabel.setObjectName(u"sortMethodLabel")

        self.horizontalLayout_6.addWidget(self.sortMethodLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

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


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.surahTab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 18)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1097, 42))
        self.menu_Language = QMenu(self.menubar)
        self.menu_Language.setObjectName(u"menu_Language")
        icon3 = QIcon()
        icon3.addFile(u":/language-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_Language.setIcon(icon3)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.searchWord, self.beginningOfWordCheckbox)
        QWidget.setTabOrder(self.beginningOfWordCheckbox, self.endOfWordCheckbox)
        QWidget.setTabOrder(self.endOfWordCheckbox, self.fullWordcheckbox)
        QWidget.setTabOrder(self.fullWordcheckbox, self.yaAlifMaksuraCheckbox)
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
        self.menu_Language.addAction(self.arabicLangButton)
        self.menu_Language.addAction(self.englishLangButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.arabicLangButton.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.englishLangButton.setText(QCoreApplication.translate("MainWindow", u"English", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0643\u0644\u0645\u0629", None))
        self.yaAlifMaksuraCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0649 / \u064a", None))
        self.finalTaCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0640\u062a / \u0640\u0629", None))
#if QT_CONFIG(tooltip)
        self.beginningOfWordCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.beginningOfWordCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062f\u0627\u064a\u0629 \u0643\u0644\u0645\u0629", None))
#if QT_CONFIG(tooltip)
        self.endOfWordCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.endOfWordCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0647\u0627\u064a\u0629 \u0643\u0644\u0645\u0629", None))
#if QT_CONFIG(tooltip)
        self.fullWordcheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fullWordcheckbox.setText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0643\u0627\u0645\u0644\u0629", None))
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
        self.filterButton.setText("")
        self.clearFilterButton.setText("")
#if QT_CONFIG(tooltip)
        self.colorizeCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.colorizeCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0644\u0648\u064a\u0646", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ayatTab), QCoreApplication.translate("MainWindow", u"\u0622\u064a\u0627\u062a", None))
        self.sortPushButton.setText("")
        self.sortMethodLabel.setText(QCoreApplication.translate("MainWindow", u"\u0637\u0631\u064a\u0642\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628", None))
#if QT_CONFIG(tooltip)
        self.allResultsCheckbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.allResultsCheckbox.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0645\u064a\u0639\n"
"\u0627\u0644\u0646\u062a\u0627\u0626\u062c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.surahTab), QCoreApplication.translate("MainWindow", u"\u0633\u0648\u0631", None))
        self.menu_Language.setTitle(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0644\u063a\u0629 / Language", None))
    # retranslateUi

