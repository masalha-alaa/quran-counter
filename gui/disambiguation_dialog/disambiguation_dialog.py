# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disambiguation_dialog.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DidsambiguationDialog(object):
    def setupUi(self, DidsambiguationDialog):
        if not DidsambiguationDialog.objectName():
            DidsambiguationDialog.setObjectName(u"DidsambiguationDialog")
        DidsambiguationDialog.resize(647, 391)
        DidsambiguationDialog.setStyleSheet(u"QWidget {\n"
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
"")
        self.verticalLayout = QVBoxLayout(DidsambiguationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.spinnerParentLayout = QHBoxLayout()
        self.spinnerParentLayout.setSpacing(0)
        self.spinnerParentLayout.setObjectName(u"spinnerParentLayout")

        self.horizontalLayout_2.addLayout(self.spinnerParentLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.instructionsWordLabel = QLabel(DidsambiguationDialog)
        self.instructionsWordLabel.setObjectName(u"instructionsWordLabel")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.instructionsWordLabel.setFont(font)
        self.instructionsWordLabel.setLayoutDirection(Qt.RightToLeft)
        self.instructionsWordLabel.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))

        self.horizontalLayout_3.addWidget(self.instructionsWordLabel)

        self.instructionsLabel = QLabel(DidsambiguationDialog)
        self.instructionsLabel.setObjectName(u"instructionsLabel")
        self.instructionsLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.instructionsLabel)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.resultsListWidget = QListWidget(DidsambiguationDialog)
        self.resultsListWidget.setObjectName(u"resultsListWidget")
        self.resultsListWidget.setLayoutDirection(Qt.RightToLeft)
        self.resultsListWidget.setTextElideMode(Qt.ElideNone)
        self.resultsListWidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.resultsListWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(DidsambiguationDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.okButton = QPushButton(DidsambiguationDialog)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.okButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(DidsambiguationDialog)

        QMetaObject.connectSlotsByName(DidsambiguationDialog)
    # setupUi

    def retranslateUi(self, DidsambiguationDialog):
        DidsambiguationDialog.setWindowTitle(QCoreApplication.translate("DidsambiguationDialog", u"\u062a\u0648\u0636\u064a\u062d", None))
        self.instructionsWordLabel.setText(QCoreApplication.translate("DidsambiguationDialog", u"'\u0627\u0644\u0643\u0644\u0645\u0629'", None))
        self.instructionsLabel.setText(QCoreApplication.translate("DidsambiguationDialog", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u0639\u0646\u0649 \u0627\u0644\u0645\u0646\u0627\u0633\u0628 \u0644\u0643\u0644\u0645\u0629", None))
        self.cancelButton.setText(QCoreApplication.translate("DidsambiguationDialog", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.okButton.setText(QCoreApplication.translate("DidsambiguationDialog", u"\u062a\u0637\u0628\u064a\u0642", None))
    # retranslateUi

