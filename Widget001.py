# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget001.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(998, 611)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame#frame{    \n"
"    background-color: rgba(255, 255, 255, 76);\n"
"    border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame#frame_2{    \n"
"    background-color: rgba(255, 255, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("border:none")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.frame_5)
        self.widget_5.setMinimumSize(QtCore.QSize(65, 65))
        self.widget_5.setMaximumSize(QtCore.QSize(65, 65))
        self.widget_5.setStyleSheet("border-image: url(:/pi/R4.jpg);\n"
"border-radius:25px;\n"
"background-color: rgb(233, 233, 233);")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6.addWidget(self.widget_5)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(20, 55, 55);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(100, 128, 128);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setStyleSheet("QListWidget{\n"
"    padding-top:24px;\n"
"    padding-left:16px;\n"
"    border-radius:20px;\n"
"    color:rgb(106, 106, 106);\n"
"}\n"
"QListWidget::item{\n"
"    background-color:transparent;\n"
"    height:40px;\n"
"    padding-left:12px;\n"
"    padding:6px;    \n"
"}\n"
"QListWidget::item:hover{\n"
"    background-color:rgba(216, 216, 216, 50);\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color:rgba(90, 216, 212, 50);\n"
"    /*background-color:rgb(255, 248, 241);\n"
"    color:rgb(255, 133, 0);\n"
"    border-left:2px solid rgb(255, 133, 0);*/\n"
"    color:rgb(50, 90, 90);\n"
"    border-left:2px solid rgb(90, 216, 216);\n"
"}")
        self.listWidget.setLineWidth(0)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setIconSize(QtCore.QSize(24, 24))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/R1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setStyleSheet("QFrame{    \n"
"    background-color: rgb(90, 215, 215);\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_2 = QtWidgets.QWidget(self.frame_6)
        self.widget_2.setMinimumSize(QtCore.QSize(65, 65))
        self.widget_2.setStyleSheet("border-image: url(:/pi/R5.jpg);\n"
"border-radius:15px;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(3, 3)
        self.verticalLayout_2.setStretch(4, 1)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet(".QFrame{    \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius:20px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(6, 6, 9, 9)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(20, 55, 55);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(240, 240, 240);\n"
"    border:0px solid red;\n"
"    border-radius:6px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setStyleSheet("QWidget{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"/*border: none;*/")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_3.setAcceptDrops(False)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_7.setLineWidth(0)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.progressBar = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_6.setAcceptDrops(False)
        self.widget_6.setAutoFillBackground(False)
        self.widget_6.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_13.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_13.setSpacing(12)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_13.addWidget(self.widget_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_13.setLineWidth(0)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget_6)
        self.label_14.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_6)
        self.progressBar_3.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar_3.setProperty("value", 50)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout_7.addWidget(self.progressBar_3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_6)
        self.widget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_9.setAcceptDrops(False)
        self.widget_9.setAutoFillBackground(False)
        self.widget_9.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_15.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_15.addWidget(self.widget_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_16.setLineWidth(0)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.widget_9)
        self.label_17.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget_9)
        self.progressBar_4.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar_4.setProperty("value", 50)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_8.addWidget(self.progressBar_4)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.label_18 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_16.addWidget(self.label_18)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_9)
        self.widget_11 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_11.setAcceptDrops(False)
        self.widget_11.setAutoFillBackground(False)
        self.widget_11.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_17.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_12.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_17.addWidget(self.widget_12)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_19.setLineWidth(0)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.widget_11)
        self.label_20.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_9.addWidget(self.label_20)
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget_11)
        self.progressBar_5.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar_5.setProperty("value", 50)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setInvertedAppearance(False)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_9.addWidget(self.progressBar_5)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.label_21 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_11)
        self.widget_13 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_13.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_13.setAcceptDrops(False)
        self.widget_13.setAutoFillBackground(False)
        self.widget_13.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_19.addWidget(self.widget_14)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_22 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_22.setLineWidth(0)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.widget_13)
        self.label_23.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_10.addWidget(self.label_23)
        self.progressBar_6 = QtWidgets.QProgressBar(self.widget_13)
        self.progressBar_6.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar_6.setProperty("value", 50)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setInvertedAppearance(False)
        self.progressBar_6.setObjectName("progressBar_6")
        self.verticalLayout_10.addWidget(self.progressBar_6)
        self.horizontalLayout_20.addLayout(self.verticalLayout_10)
        self.label_24 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_20.addWidget(self.label_24)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_13)
        self.widget_15 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 78))
        self.widget_15.setAcceptDrops(False)
        self.widget_15.setAutoFillBackground(False)
        self.widget_15.setStyleSheet("QWidget{    \n"
"    background-color: qconicalgradient(\n"
"    x1:0, y1:0, x2:1, y2:0, stop:0 rgb(230, 240, 250),\n"
"    stop:1 rgba(150, 230, 230, 255)\n"
"    );\n"
"    /*(\n"
"    cx:0.5, cy:0.5, angle:90, stop:0 rgb(235, 252, 254),\n"
"    stop:1 rgb(184, 233, 234)\n"
"    );*/\n"
"    border-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.widget_16 = QtWidgets.QWidget(self.widget_15)
        self.widget_16.setStyleSheet("border-radius:15px;\n"
"border-image: url(:/icon/OIP.jpg);")
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_21.addWidget(self.widget_16)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(2)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_25 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color:none;")
        self.label_25.setLineWidth(0)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_11.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.widget_15)
        self.label_26.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        self.progressBar_7 = QtWidgets.QProgressBar(self.widget_15)
        self.progressBar_7.setStyleSheet("QProgressBar::chunk{\n"
"    border-top-left-radius:6px;\n"
"    border-bottom-left-radius:6px;\n"
"    background-color:rgb(100, 216, 216)\n"
"}\n"
"QProgressBar{\n"
"    border-radius:6px;\n"
"    background-color:rgb(223, 223, 223)\n"
"}\n"
"")
        self.progressBar_7.setProperty("value", 50)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setInvertedAppearance(False)
        self.progressBar_7.setObjectName("progressBar_7")
        self.verticalLayout_11.addWidget(self.progressBar_7)
        self.horizontalLayout_22.addLayout(self.verticalLayout_11)
        self.label_27 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(20, 55, 55);\n"
"background-color: none;")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_22.addWidget(self.label_27)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 5)
        self.verticalLayout_12.addWidget(self.widget_15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_23.addWidget(self.scrollArea)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addWidget(self.frame)

        self.retranslateUi(Form)
        self.label_2.linkHovered['QString'].connect(self.lineEdit.setText)
        self.lineEdit.textChanged['QString'].connect(self.label_9.setText)
        self.lineEdit.textChanged['QString'].connect(self.progressBar.update)
        self.listWidget.currentRowChanged['int'].connect(self.progressBar_3.setValue)
        self.listWidget.currentRowChanged['int'].connect(self.label_15.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Erduo"))
        self.label_2.setText(_translate("Form", "Pro Member"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Streams"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Games"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "New"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Librory"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "Join pro"))
        self.label_4.setText(_translate("Form", "for free"))
        self.label_5.setText(_translate("Form", "games.."))
        self.label_6.setText(_translate("Form", "Active Games"))
        self.label_7.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_8.setText(_translate("Form", "PS5 Version"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.label_9.setText(_translate("Form", "50%"))
        self.label_13.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_14.setText(_translate("Form", "PS5 Version"))
        self.progressBar_3.setFormat(_translate("Form", "%p%"))
        self.label_15.setText(_translate("Form", "50%"))
        self.label_16.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_17.setText(_translate("Form", "PS5 Version"))
        self.progressBar_4.setFormat(_translate("Form", "%p%"))
        self.label_18.setText(_translate("Form", "50%"))
        self.label_19.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_20.setText(_translate("Form", "PS5 Version"))
        self.progressBar_5.setFormat(_translate("Form", "%p%"))
        self.label_21.setText(_translate("Form", "50%"))
        self.label_22.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_23.setText(_translate("Form", "PS5 Version"))
        self.progressBar_6.setFormat(_translate("Form", "%p%"))
        self.label_24.setText(_translate("Form", "50%"))
        self.label_25.setText(_translate("Form", "Assossins Creed Vathaila"))
        self.label_26.setText(_translate("Form", "PS5 Version"))
        self.progressBar_7.setFormat(_translate("Form", "%p%"))
        self.label_27.setText(_translate("Form", "50%"))
from qrc_img import img_rc
