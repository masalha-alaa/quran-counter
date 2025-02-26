# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'word_detailed_display_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_DetailedWordDisplayDialog(object):
    def setupUi(self, DetailedWordDisplayDialog):
        if not DetailedWordDisplayDialog.objectName():
            DetailedWordDisplayDialog.setObjectName(u"DetailedWordDisplayDialog")
        DetailedWordDisplayDialog.setWindowModality(Qt.NonModal)
        DetailedWordDisplayDialog.resize(959, 462)
        DetailedWordDisplayDialog.setLayoutDirection(Qt.RightToLeft)
        DetailedWordDisplayDialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 20pt \"Calibri\";\n"
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
"QCheckBox:hover {\n"
"    background-color: rgba(71, 96, 126, 0.2);\n"
"}")
        DetailedWordDisplayDialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        DetailedWordDisplayDialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(DetailedWordDisplayDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(DetailedWordDisplayDialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textBrowser.setStyleSheet(u"font-family: 'Noto Naskh Arabic'; font-size: 17pt;")
        self.textBrowser.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))

        self.horizontalLayout.addWidget(self.textBrowser)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.colorizeCheckbox = QCheckBox(DetailedWordDisplayDialog)
        self.colorizeCheckbox.setObjectName(u"colorizeCheckbox")
        self.colorizeCheckbox.setChecked(True)

        self.verticalLayout.addWidget(self.colorizeCheckbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(DetailedWordDisplayDialog)

        QMetaObject.connectSlotsByName(DetailedWordDisplayDialog)
    # setupUi

    def retranslateUi(self, DetailedWordDisplayDialog):
        DetailedWordDisplayDialog.setWindowTitle(QCoreApplication.translate("DetailedWordDisplayDialog", u"\u062a\u0641\u0627\u0635\u064a\u0644 \u0645\u0648\u0633\u0651\u0639\u0629", None))
        self.colorizeCheckbox.setText(QCoreApplication.translate("DetailedWordDisplayDialog", u"\u062a\u0644\u0648\u064a\u0646", None))
    # retranslateUi

