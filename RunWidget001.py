import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWidgets import QWidget,QApplication

from Widget001 import Ui_Form

class MyWidget(QWidget,Ui_Form):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint) #隐藏窗口边框
        self.shadowStyle(self.widget_3)
        self.shadowStyle(self.widget_6)
        self.shadowStyle ( self.widget_9 )
        self.shadowStyle ( self.widget_11 )
        self.shadowStyle ( self.widget_13 )
        self.shadowStyle ( self.widget_15 )

    def shadowStyle(self,widget:QWidget):
        eft = QtWidgets.QGraphicsDropShadowEffect()
        eft.setOffset(0,20) #偏移
        eft.setBlurRadius(20) #阴影半径
        eft.setColor(QtCore.Qt.gray) #阴影颜色
        widget.setGraphicsEffect(eft)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())

