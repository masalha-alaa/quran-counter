# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'relations_graph.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from my_widgets.networkx_graph import NetworkXGraph

class Ui_RelationsGraphDialog(object):
    def setupUi(self, RelationsGraphDialog):
        if not RelationsGraphDialog.objectName():
            RelationsGraphDialog.setObjectName(u"RelationsGraphDialog")
        RelationsGraphDialog.resize(400, 300)
        RelationsGraphDialog.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(49, 49, 49);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 400 16pt \"Calibri\";\n"
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
        self.verticalLayout = QVBoxLayout(RelationsGraphDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.expandedGraphCheckbox = QCheckBox(RelationsGraphDialog)
        self.expandedGraphCheckbox.setObjectName(u"expandedGraphCheckbox")
        self.expandedGraphCheckbox.setLayoutDirection(Qt.RightToLeft)
        self.expandedGraphCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.expandedGraphCheckbox, 0, 2, 1, 1)

        self.graphWidget = NetworkXGraph(RelationsGraphDialog)
        self.graphWidget.setObjectName(u"graphWidget")
        self.verticalLayout_2 = QVBoxLayout(self.graphWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addWidget(self.graphWidget, 1, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(RelationsGraphDialog)

        QMetaObject.connectSlotsByName(RelationsGraphDialog)
    # setupUi

    def retranslateUi(self, RelationsGraphDialog):
        RelationsGraphDialog.setWindowTitle(QCoreApplication.translate("RelationsGraphDialog", u"Path", None))
        self.expandedGraphCheckbox.setText(QCoreApplication.translate("RelationsGraphDialog", u"\u0631\u0633\u0645 \u0645\u0648\u0633\u0651\u0639", None))
    # retranslateUi

