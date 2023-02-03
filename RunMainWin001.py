import sys,os
from os.path import join
from PySide2 import QtCore,QtWidgets
from PySide2.QtCore import Qt,QUrl
from PySide2.QtGui import QPixmap,QImage
from PySide2.QtWidgets import QWidget,QApplication,QListWidget,QMessageBox,QMainWindow,\
    QGraphicsScene,QGraphicsPixmapItem,QCheckBox,QGraphicsItem,QGraphicsView
from zltools import readfile as rf

import matplotlib.pyplot as plt
import numpy as np

from MainWin001 import Ui_MainWindow

class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.FramelessWindowHint) #隐藏窗口边框

        #槽函数 self.selection 不用加()和传递相关参数
        self.listWidget.itemClicked.connect(self.selection)

        y = np.array ( [ 35, 25, 25, 15 ] )
        mylabels = [ "Apples", "Bananas", "Cherries", "Dates" ]
        myexplode = [ 0.2, 0, 0, 0 ]

        plt.pie ( y, labels=mylabels, explode=myexplode, shadow=True )
        plt.show()
        # p = plt.savefig('p')
        # # scn = QGraphicsScene().addItem(QtWidgets.QGraphicsObject(p))
        # scn = QGraphicsScene ().addItem ( QGraphicsPixmapItem ( QPixmap.fromImage ( QImage ( p ) ) ) )
        # wg3 = QGraphicsView(self.widget_3).setScene(scn)




    def selection(self,itm:QListWidget.item):
        # if item.text() == 'Streams':
        if itm is self.listWidget.item(0):
            self.graphicsView.hide()#隐藏graphicsView视图
            self.GX = QWidget ( self.frame_3 )

            btn = QtWidgets.QPushButton('更新',self.GX)
            btn.setIconSize(QtCore.QSize(20,30))
            txt = QtWidgets.QTextBrowser(self.GX)
            txt.setText('...')

            # hLyOut0 = QtWidgets.QHBoxLayout ()

            self.horizontalLayout_2.removeWidget(self.graphicsView)

            self.horizontalLayout_2.addWidget ( self.GX )

            self.hLyOut = QtWidgets.QHBoxLayout ()
            # self.hLyOut.addWidget(self.GX)
            self.hLyOut.addWidget(btn)
            self.hLyOut.addWidget(txt)

            self.horizontalLayout_2.addLayout ( self.hLyOut )

            # self.msg(itm)
        elif itm is self.listWidget.item(1):
            rf.openAnimation ( open=True )

            cps = rf.CreatePics ( stocks_need=100, w=8, h=5 )
            # cps.saveTrainingPics()
            cps.saveNewestPics ( offset_days=None )
            # cps.checkFilterPolicy()

            # 打开文件夹
            file_path = cps.save_path + cps.timeStamp + '\\' + 'newest\\'
            os.startfile ( file_path )  # "C:\\Users\\binli\\JupyterNotebook\\CreatePics_20221117\\newest"

            self.msg(itm)
        elif itm is self.listWidget.item(2):

            self.GX.hide()
            self.horizontalLayout_2.removeWidget(self.GX)
            # self.horizontalLayout_2.removeItem(self.GX)

            self.graphicsView.show()#显示graphicsView视图
            root = 'C:/Users/binli/JupyterNotebook/CreatePics_20230107/newest'
            scene = QGraphicsScene ()
            h = 0
            for rot,paths,files in os.walk(root):
                try:
                    for name in files:
                        f = join(rot,name)
                        img = QImage(f)
                        # img.setText('code',name)
                        h += img.height()
                        # img.scaledToWidth(self.graphicsView.width())
                        itx = QGraphicsPixmapItem(QPixmap.fromImage (img))
                        w = itx.shape()
                        itx.setFlags(QGraphicsPixmapItem.ItemIsSelectable )# | QGraphicsPixmapItem.ItemIsMovable)
                        itx.setY(h + 1)

                        scene.addItem ( itx )

                        # itb = QtWidgets.QGraphicsTextItem(name)
                        # itb.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
                        # itb.setX(self.graphicsView.width() / 2)
                        # itx.setY ( h )
                        # scene.addItem(itb)

                    # scene.addPixmap ( (QPixmap.fromImage ( QImage ( join ( rot, name ) ) ) for name in files) )
                except Exception as e:
                    print(f'Error:{e}')


            # scene.addPixmap(QPixmap.fromImage('C:/Users/binli/Pictures/Camera Roll/cachemem.png'))

            self.graphicsView.setScene(scene)
            self.horizontalLayout_2.addWidget ( self.graphicsView )
            # self.graphicsView.items().append()
            self.msg(itm)
        elif itm is self.listWidget.item(3):
            self.msg(itm)
        elif itm is self.listWidget.item(4):
            self.msg(itm)

    def msg(self,itm):
        QMessageBox.information ( self, 'info', 'you selected ->' + itm.text () )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())