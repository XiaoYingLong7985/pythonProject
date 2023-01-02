import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWidgets import QWidget,QApplication,QListWidget,QMessageBox

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

        #槽函数 self.selection 不用加()和传递相关参数
        self.listWidget.itemClicked.connect(self.selection)


    def shadowStyle(self,widget:QWidget):
        eft = QtWidgets.QGraphicsDropShadowEffect()
        eft.setOffset(0,20) #偏移
        eft.setBlurRadius(20) #阴影半径
        eft.setColor(QtCore.Qt.gray) #阴影颜色
        widget.setGraphicsEffect(eft)

    def selection(self,itm:QListWidget.item):
        # if item.text() == 'Streams':
        if itm is self.listWidget.item(0):
            self.progressBar.setValue(100)
            self.label_9.setText('100%')
            QMessageBox.information(self,'info','you selected ->' + itm.text())
        elif itm is self.listWidget.item(1):
            self.progressBar_3.setValue(90)
        elif itm is self.listWidget.item(2):
            self.progressBar_4.setValue(80)
        elif itm is self.listWidget.item(3):
            self.progressBar_5.setValue(70)



class ListWidget(QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()

    def clicked(self,item):
        QMessageBox.information(self,'info','you selected ->' + item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())

