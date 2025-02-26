# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        if not DownloadDialog.objectName():
            DownloadDialog.setObjectName(u"DownloadDialog")
        DownloadDialog.resize(579, 350)
        DownloadDialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 18pt \"Calibri\";\n"
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
"/* Progress Bar */\n"
"QProgressBar {\n"
"    background-color: #3B4252; /* Dark background */\n"
"    border: 1px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    text-align: center; /* Center text */\n"
"    color: #D8DEE9; /* Text color */\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"                                      stop:0 #81A1C1, stop:1 #88C0"
                        "D0); /* Gradient for progress */\n"
"    border-radius: 5px; /* Rounded corners for the chunk */\n"
"    border: 1px solid #81A1C1; /* Border for the chunk */\n"
"    box-shadow: 0px 0px 5px rgba(129, 161, 193, 0.5); /* Glow effect */\n"
"}")
        self.verticalLayout = QVBoxLayout(DownloadDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.questionLabel = QLabel(DownloadDialog)
        self.questionLabel.setObjectName(u"questionLabel")

        self.verticalLayout.addWidget(self.questionLabel)

        self.detailsLabel = QLabel(DownloadDialog)
        self.detailsLabel.setObjectName(u"detailsLabel")
        self.detailsLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.detailsLabel)

        self.detailedOutputTextBrowser = QTextBrowser(DownloadDialog)
        self.detailedOutputTextBrowser.setObjectName(u"detailedOutputTextBrowser")

        self.verticalLayout.addWidget(self.detailedOutputTextBrowser)

        self.progressBar = QProgressBar(DownloadDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setFormat(u"%p%")

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.noButton = QPushButton(DownloadDialog)
        self.noButton.setObjectName(u"noButton")

        self.horizontalLayout.addWidget(self.noButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.yesButton = QPushButton(DownloadDialog)
        self.yesButton.setObjectName(u"yesButton")

        self.horizontalLayout.addWidget(self.yesButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DownloadDialog)

        QMetaObject.connectSlotsByName(DownloadDialog)
    # setupUi

    def retranslateUi(self, DownloadDialog):
        DownloadDialog.setWindowTitle(QCoreApplication.translate("DownloadDialog", u"\u062a\u062d\u0645\u064a\u0644 \u0645\u0644\u0641\u0627\u062a", None))
        self.questionLabel.setText(QCoreApplication.translate("DownloadDialog", u"\u0628\u0639\u0636 \u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0644\u0647\u0630\u0647 \u0627\u0644\u062e\u0627\u0635\u064a\u0629 \u0646\u0627\u0642\u0635\u0629. \u0647\u0644 \u062a\u0631\u064a\u062f \u062a\u062d\u0645\u064a\u0644\u0647\u0627 \u0627\u0644\u0622\u0646\u061f", None))
        self.detailsLabel.setText("")
        self.noButton.setText(QCoreApplication.translate("DownloadDialog", u"\u0644\u0627", None))
        self.yesButton.setText(QCoreApplication.translate("DownloadDialog", u"\u0646\u0639\u0645", None))
    # retranslateUi

