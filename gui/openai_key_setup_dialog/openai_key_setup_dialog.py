# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openai_key_setup_dialog.ui'
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
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_OpenAiKeySetupDialog(object):
    def setupUi(self, OpenAiKeySetupDialog):
        if not OpenAiKeySetupDialog.objectName():
            OpenAiKeySetupDialog.setObjectName(u"OpenAiKeySetupDialog")
        OpenAiKeySetupDialog.resize(720, 496)
        OpenAiKeySetupDialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 15pt \"Calibri\";\n"
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
        self.verticalLayout_2 = QVBoxLayout(OpenAiKeySetupDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(OpenAiKeySetupDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.statusParentLayout = QHBoxLayout()
        self.statusParentLayout.setSpacing(0)
        self.statusParentLayout.setObjectName(u"statusParentLayout")

        self.horizontalLayout_2.addLayout(self.statusParentLayout)

        self.enterKeyLineEdit = QLineEdit(OpenAiKeySetupDialog)
        self.enterKeyLineEdit.setObjectName(u"enterKeyLineEdit")
        self.enterKeyLineEdit.setMaxLength(200)

        self.horizontalLayout_2.addWidget(self.enterKeyLineEdit)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(OpenAiKeySetupDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(OpenAiKeySetupDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"<a href=\"https://platform.openai.com/api-keys\"><span style=\"color:deepskyblue;\">https://platform.openai.com/api-keys</span></a>")
        self.label_3.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cancelButton = QPushButton(OpenAiKeySetupDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(OpenAiKeySetupDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 1)

        self.retranslateUi(OpenAiKeySetupDialog)

        QMetaObject.connectSlotsByName(OpenAiKeySetupDialog)
    # setupUi

    def retranslateUi(self, OpenAiKeySetupDialog):
        OpenAiKeySetupDialog.setWindowTitle(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u062a\u062b\u0628\u064a\u062a \u0627\u0644\u0645\u0641\u062a\u0627\u062d", None))
        self.label.setText(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u0627\u062f\u062e\u0644 \u0627\u0644\u0640 OpenAI Key \u0627\u0644\u062e\u0627\u0635 \u0628\u0643 \u0644\u062a\u0641\u0639\u064a\u0644 ChatGPT:", None))
        self.enterKeyLineEdit.setPlaceholderText(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u0645\u0641\u062a\u0627\u062d / \u0645\u0633\u0627\u0631 \u0627\u0644\u0645\u0644\u0641", None))
        self.label_2.setText(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u064a\u0645\u0643\u0646 \u0627\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0645\u0641\u062a\u0627\u062d \u0645\u0646 \u062e\u0644\u0627\u0644 \u0627\u0644\u0645\u0648\u0642\u0639:", None))
        self.cancelButton.setText(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u0627\u0644\u063a\u0627\u0621", None))
        self.okButton.setText(QCoreApplication.translate("OpenAiKeySetupDialog", u"\u062a\u0637\u0628\u064a\u0642", None))
    # retranslateUi

