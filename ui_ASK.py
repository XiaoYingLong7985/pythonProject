# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ASKnbSVEH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqtgraph import PlotWidget
from pyqtgraph import TableWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1200, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"mystocks/ask.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: rgb(253, 255, 243);\n"
"	\n"
"	font: 25 9pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"	background-color: rgb(85, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QTextBrowser:hover{\n"
"	\n"
"	color: rgb(85, 0, 0);\n"
"	border-color: rgb(0, 0, 0);\n"
"}")
        # Dialog.setSizeGripEnabled(False)
        # Dialog.setModal(False)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Mwidget = QWidget(Dialog)
        self.Mwidget.setObjectName(u"Mwidget")
        self.verticalLayout_7 = QVBoxLayout(self.Mwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pBtn_1 = QPushButton(self.Mwidget)
        self.pBtn_1.setObjectName(u"pBtn_1")
        self.pBtn_1.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pBtn_1.sizePolicy().hasHeightForWidth())
        self.pBtn_1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.pBtn_1.setFont(font)
        self.pBtn_1.setAutoFillBackground(False)
        self.pBtn_1.setAutoRepeatDelay(300)
        self.pBtn_1.setFlat(False)

        self.verticalLayout_2.addWidget(self.pBtn_1)

        self.pBar_1 = QProgressBar(self.Mwidget)
        self.pBar_1.setObjectName(u"pBar_1")
        self.pBar_1.setValue(0)

        self.verticalLayout_2.addWidget(self.pBar_1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pBtn_2 = QPushButton(self.Mwidget)
        self.pBtn_2.setObjectName(u"pBtn_2")
        sizePolicy1.setHeightForWidth(self.pBtn_2.sizePolicy().hasHeightForWidth())
        self.pBtn_2.setSizePolicy(sizePolicy1)
        self.pBtn_2.setFont(font)
        self.pBtn_2.setAutoFillBackground(False)
        self.pBtn_2.setAutoRepeatDelay(300)
        self.pBtn_2.setFlat(False)

        self.verticalLayout_3.addWidget(self.pBtn_2)

        self.pBar_2 = QProgressBar(self.Mwidget)
        self.pBar_2.setObjectName(u"pBar_2")
        self.pBar_2.setValue(0)

        self.verticalLayout_3.addWidget(self.pBar_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pBtn_3 = QPushButton(self.Mwidget)
        self.pBtn_3.setObjectName(u"pBtn_3")
        sizePolicy1.setHeightForWidth(self.pBtn_3.sizePolicy().hasHeightForWidth())
        self.pBtn_3.setSizePolicy(sizePolicy1)
        self.pBtn_3.setFont(font)
        self.pBtn_3.setAutoFillBackground(False)
        self.pBtn_3.setAutoRepeatDelay(300)
        self.pBtn_3.setFlat(False)

        self.verticalLayout_5.addWidget(self.pBtn_3)

        self.pBar_3 = QProgressBar(self.Mwidget)
        self.pBar_3.setObjectName(u"pBar_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pBar_3.sizePolicy().hasHeightForWidth())
        self.pBar_3.setSizePolicy(sizePolicy2)
        self.pBar_3.setValue(0)

        self.verticalLayout_5.addWidget(self.pBar_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pBtn_4 = QPushButton(self.Mwidget)
        self.pBtn_4.setObjectName(u"pBtn_4")
        sizePolicy1.setHeightForWidth(self.pBtn_4.sizePolicy().hasHeightForWidth())
        self.pBtn_4.setSizePolicy(sizePolicy1)
        self.pBtn_4.setFont(font)
        self.pBtn_4.setAutoFillBackground(False)
        self.pBtn_4.setIconSize(QSize(16, 16))
        self.pBtn_4.setAutoRepeatDelay(300)
        self.pBtn_4.setFlat(False)

        self.verticalLayout_6.addWidget(self.pBtn_4)

        self.pBar_4 = QProgressBar(self.Mwidget)
        self.pBar_4.setObjectName(u"pBar_4")
        sizePolicy2.setHeightForWidth(self.pBar_4.sizePolicy().hasHeightForWidth())
        self.pBar_4.setSizePolicy(sizePolicy2)
        self.pBar_4.setValue(0)

        self.verticalLayout_6.addWidget(self.pBar_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = TableWidget(self.Mwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.textBrowser = QTextBrowser(self.Mwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1 Light")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.textBrowser.setFont(font1)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = PlotWidget(self.Mwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 10)

        self.verticalLayout_4.addWidget(self.Mwidget)


        self.retranslateUi(Dialog)

        self.pBtn_1.setDefault(True)
        self.pBtn_2.setDefault(True)
        self.pBtn_3.setDefault(True)
        self.pBtn_4.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ASK", None))
        self.pBtn_1.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u8f7d\u6700\u65b0\u6570\u636e", None))
        self.pBtn_2.setText(QCoreApplication.translate("Dialog", u"\u4eca\u65e5\u63a8\u8350\u5173\u6ce8", None))
        self.pBtn_3.setText(QCoreApplication.translate("Dialog", u"\u7b56\u7565\u9884\u6f14\u7edf\u8ba1", None))
        self.pBtn_4.setText(QCoreApplication.translate("Dialog", u"\u751f\u6210\u7edf\u8ba1\u6982\u7387", None))
    # retranslateUi

