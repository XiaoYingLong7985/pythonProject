# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWin001gXFrfb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qrc_img import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1206, 895)
        MainWindow.setStyleSheet(u"QMainWindow{background-color: rgba(255, 255, 255, 200);	\n"
"border-radius:10px;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow{background-color: rgba(255, 255, 255, 76);	\n"
"border-radius:20px;}")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{	border-radius:10px;	background-color: rgb(255, 255, 255);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setStyleSheet(u"border:none")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(55, 55))
        self.widget.setMaximumSize(QSize(100, 100))
        self.widget.setStyleSheet(u"border-image: url(:/pi/R4.jpg);\n"
"border-radius:20px;\n"
"background-color: rgb(233, 233, 233);")

        self.horizontalLayout_5.addWidget(self.widget)


        self.verticalLayout.addWidget(self.frame_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(20, 55, 55);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(100, 128, 128);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.listWidget = QListWidget(self.frame)
        icon = QIcon()
        icon.addFile(u":/icon/OIP.jpg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setIcon(icon);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setIcon(icon);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 300))
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setStyleSheet(u"QListWidget{	/*padding-top:24px;	padding-left:24px;*/	\n"
"	border-radius:24px;	color:rgb(106, 106, 106);\n"
"	border: none;	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QListWidget::item{	background-color:transparent;	height:24px;	padding-left:30px;	padding-top:12px;	}\n"
"QListWidget::item:hover{	background-color:rgba(216, 216, 216, 50);}\n"
"QListWidget::item:selected{	background-color:rgba(90, 216, 212, 50);	/*background-color:rgb(255, 248, 241);	color:rgb(255, 133, 0);	border-left:2px solid rgb(255, 133, 0);*/	color:rgb(50, 90, 90);	border-left:2px solid rgb(90, 216, 216);}")
        self.listWidget.setLineWidth(0)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setIconSize(QSize(30, 30))
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setSpacing(6)
        self.listWidget.setViewMode(QListView.ListMode)

        self.verticalLayout.addWidget(self.listWidget)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setStyleSheet(u".QFrame{		background-color: rgba(255, 255, 255, 0);	border-radius:20px;}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calendarWidget = QCalendarWidget(self.frame_5)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei")
        self.calendarWidget.setFont(font1)
        self.calendarWidget.setStyleSheet(u".QCalendarWidget{\n"
"	border: none;	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.calendarWidget)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.frame)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_6.addWidget(self.widget_2)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.graphicsView = QGraphicsView(self.frame_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"QGraphicsView{	border-radius:10px;	background-color: rgb(255, 255, 255);}/*border: none;*/")

        self.horizontalLayout_2.addWidget(self.graphicsView)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1206, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ZLiang", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Administrator", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u793a", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u8ddf\u8e2a", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

