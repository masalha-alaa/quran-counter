# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'waiting_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_WaitingDialog(object):
    def setupUi(self, WaitingDialog):
        if not WaitingDialog.objectName():
            WaitingDialog.setObjectName(u"WaitingDialog")
        WaitingDialog.resize(400, 300)
        WaitingDialog.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(207, 207, 207);\n"
"font: 400 20pt \"Calibri\";")
        self.verticalLayout_2 = QVBoxLayout(WaitingDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(WaitingDialog)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(WaitingDialog)

        QMetaObject.connectSlotsByName(WaitingDialog)
    # setupUi

    def retranslateUi(self, WaitingDialog):
        WaitingDialog.setWindowTitle(QCoreApplication.translate("WaitingDialog", u"\u0627\u0646\u062a\u0638\u0627\u0631", None))
        self.label.setText(QCoreApplication.translate("WaitingDialog", u"\u0627\u0644\u0631\u062c\u0627\u0621 \u0627\u0644\u0627\u0646\u062a\u0638\u0627\u0631...", None))
    # retranslateUi

