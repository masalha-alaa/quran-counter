# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'version_update_dialog.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_VersionUpdateDialog(object):
    def setupUi(self, VersionUpdateDialog):
        if not VersionUpdateDialog.objectName():
            VersionUpdateDialog.setObjectName(u"VersionUpdateDialog")
        VersionUpdateDialog.resize(450, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VersionUpdateDialog.sizePolicy().hasHeightForWidth())
        VersionUpdateDialog.setSizePolicy(sizePolicy)
        VersionUpdateDialog.setMaximumSize(QSize(450, 150))
        VersionUpdateDialog.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout = QVBoxLayout(VersionUpdateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statusLabel = QLabel(VersionUpdateDialog)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setText(u"\u062c\u0627\u0631\u064a \u0627\u0644\u0641\u062d\u0635...")

        self.verticalLayout.addWidget(self.statusLabel)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.downloadButton = QPushButton(VersionUpdateDialog)
        self.downloadButton.setObjectName(u"downloadButton")

        self.buttonsLayout.addWidget(self.downloadButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(VersionUpdateDialog)

        QMetaObject.connectSlotsByName(VersionUpdateDialog)
    # setupUi

    def retranslateUi(self, VersionUpdateDialog):
        VersionUpdateDialog.setWindowTitle(QCoreApplication.translate("VersionUpdateDialog", u"\u062a\u062d\u062f\u064a\u062b", None))
        self.downloadButton.setText(QCoreApplication.translate("VersionUpdateDialog", u"\u062a\u062d\u0645\u064a\u0644", None))
    # retranslateUi

