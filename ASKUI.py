import inspect
from concurrent.futures import ThreadPoolExecutor

import click
import matplotlib.pyplot as plt
import numpy as np
import pymysql
import pandas as pd
from PyQt5.QtGui import QPixmap
from PySide2.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPen
from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FCanvas

from ui_ASK import Ui_Dialog
import sys
from threading import Thread

# from PySide2 import QtWidgets
# from PySide2.QtWidgets import QMainWindow
# from PySide2 import QtGui
# from PySide2 import QtCore

from PySide2.QtWidgets import QVBoxLayout,QSizePolicy
import pyqtgraph as pg
# from pyqtgraph import QtGui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore

# from PyQt5.QtWidgets import QVBoxLayout,QSizePolicy

import time
from itertools import chain

from AnalysisFSS import FSS_V6,CandleChart
from mystocks import STRUS_RV5c as RSD

import logging
import os
import traceback
import subprocess
# from tool import bat,reg

# class Service ( object ) :
#
#     def __init__(self, name, dir, app) :
#         # 服务名称
#         self.name = name
#         # 服务程序路径
#         self.dir = dir
#         # 服务启动程序.bat或.exe
#         self.app = app
#
#         cwd = os.getcwd ()
#         self.instsrv = os.path.join ( cwd, r"\extra\instsrv.exe" )
#         self.srvany = os.path.join ( cwd, r"\extra\srvany.exe" )
#
#     def install(self) :
#         try :
#             self.remove ()
#
#             print ( "Install service .." )
#             # 管理员权限运行CMD命令
#             self.runAdmin ( "%s %s %s" % (self.instsrv, self.name, self.srvany) )
#             # 添加服务相关参数到注册表
#             self.addSrvParam ( self.name, self.dir, self.app )
#             print ( "%s install success" % self.name )
#         except Exception as e :
#             traceback.print_exc ()
#             raise e
#
#     def status(self) :
#         status = os.popen ( "sc query %s" % self.name ).read ()
#         if "未安装" in status :
#             return -1
#         elif "START_PENDING" in status :
#             return 0
#         if "RUNNING" in status :
#             return 1
#         elif "STOP_PENDING" in status :
#             return 2
#         elif "STOPPED" in status :
#             return 3
#         else :
#             return 4
#
#     def auto(self) :
#         try :
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc config %s start = auto" % self.name )
#         except Exception as e :
#             raise e
#
#     def start(self) :
#         status = self.status ()
#         if -1 == status :
#             print ( "%s is uninstalled" % self.name )
#             return
#         elif 0 == status :
#             print ( "%s is starting .." % self.name )
#             return
#         elif 1 == status :
#             print ( "%s is running" % self.name )
#             return
#         elif 2 == status :
#             print ( "%s is stopping .." % self.name )
#             time.sleep ( 10 )
#             while 2 == self.status () :
#                 time.sleep ( 10 )
#
#             print ( "Start service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc start %s" % self.name )
#             print ( "%s startup success" % self.name )
#         elif 3 == status :
#             print ( "%s is stopped" % self.name )
#
#             print ( "Start service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc start %s" % self.name )
#             print ( "%s startup success" % self.name )
#         else :
#             print ( "%s is in other status" % self.name )
#
#     def stop(self) :
#         status = self.status ()
#         if -1 == status :
#             print ( "%s is uninstalled" % self.name )
#             return
#         elif 0 == status :
#             print ( "%s is starting .." % self.name )
#             time.sleep ( 10 )
#             while 0 == self.status () :
#                 time.sleep ( 10 )
#
#             print ( "Stop Service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc stop %s" % self.name )
#             print ( "%s shutdown success" % self.name )
#         elif 1 == status :
#             print ( "%s is running" % self.name )
#
#             print ( "Stop Service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc stop %s" % self.name )
#             print ( "%s shutdown success" % self.name )
#         elif 2 == status :
#             print ( "%s is stopping .." % self.name )
#             return
#         elif 3 == status :
#             print ( "%s is stopped" % self.name )
#             return
#         else :
#             print ( "%s is in other status" % self.name )
#
#     def restart(self) :
#         status = self.status ()
#         if -1 == status :
#             print ( "%s is uninstalled" % self.name )
#             return
#         elif 0 == status :
#             print ( "%s is starting .." % self.name )
#             return
#         elif 1 == status :
#             try :
#                 print ( "Stop Service .." )
#                 # 管理员权限运行CMD指令
#                 self.runAdmin ( "sc stop %s" % self.name )
#             except :
#                 print ( str ( traceback.format_exc () ) )
#
#             print ( "Start service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc start %s" % self.name )
#             print ( "%s startup success" % self.name )
#         elif 2 == status :
#             print ( "%s is stopping .." % self.name )
#             time.sleep ( 10 )
#             while 2 == self.status () :
#                 time.sleep ( 10 )
#
#             print ( "Start service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc start %s" % self.name )
#             print ( "%s startup success" % self.name )
#         elif 3 == status :
#             print ( "%s is stopped" % self.name )
#
#             print ( "Start service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "sc start %s" % self.name )
#             print ( "%s startup success" % self.name )
#         else :
#             print ( "%s is in other status" % self.name )
#
#     def remove(self) :
#         try :
#             status = self.status ()
#             if -1 == status :
#                 print ( "%s is uninstalled" % self.name )
#                 return
#
#             self.stop ()
#
#             print ( "Remove service .." )
#             # 管理员权限运行CMD指令
#             self.runAdmin ( "%s %s remove" % (self.instsrv, self.name) )
#             print ( "%s remove success" % self.name )
#         except Exception as e :
#             raise e
#
#     def runAdmin(cmd, timeout=1800000) :
#         f = None
#         try :
#             bat = os.getcwd () + r"\tool\script\cmd.bat"
#             f = open ( bat, 'w' )
#             f.write ( cmd )
#         except Exception as e :
#             traceback.print_exc ()
#             raise e
#         finally :
#             if f :
#                 f.close ()
#
#         try :
#             shell = os.getcwd () + r"\tool\script\shell.vbs"
#             sp = subprocess.Popen (
#                 shell,
#                 shell=True,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE
#                 )
#             print ( "[PID] %s: %s" % (sp.pid, cmd) )
#             sp.wait ( timeout=timeout )
#
#             stderr = str ( sp.stderr.read ().decode ( "gbk" ) ).strip ()
#             stdout = str ( sp.stdout.read ().decode ( "gbk" ) ).strip ()
#             if "" != stderr :
#                 raise Exception ( stderr )
#             if stdout.find ( "失败" ) > -1 :
#                 raise Exception ( stdout )
#         except Exception as e :
#             raise e
#
#     def addSrvParam(self,srv, dir, app) :
#         # only \\ in path, / or \ is not allowed
#         dir = format ( dir ).replace ( "\\", "\\\\" )
#         app = format ( app ).replace ( "\\", "\\\\" )
#
#         # 版本声明
#         c = 'Windows Registry Editor Version 5.00\n'
#
#         # 必须空行
#         c += '\n'
#         # 添加主键
#         c += '[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\%s\Parameters]\n' % srv
#         # 添加键值
#         c += '"AppDirectory"="%s"\n' % dir
#         # 添加键值
#         c += '"Application"="%s"\n' % app
#
#         path = os.getcwd () + r"\tool\script\srv.reg"
#
#         f = None
#         try :
#             f = open ( path, 'w' )
#             f.write ( c )
#         except Exception as e :
#             traceback.print_exc ()
#             raise e
#         finally :
#             if f :
#                 f.close ()
#
#         self.command ( path, 1800000 )
#
#
#     def command(cmd, timeout=1800000) :
#         try :
#             sp = subprocess.Popen (cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#             print ( "[PID] %s: %s" % (sp.pid, cmd) )
#             sp.wait ( timeout=timeout )
#
#             stderr = str ( sp.stderr.read ().decode ( "gbk" ) ).strip ()
#             stdout = str ( sp.stdout.read ().decode ( "gbk" ) ).strip ()
#             if "" != stderr :
#                 raise Exception ( stderr )
#             if stdout.find ( "失败" ) > -1 :
#                 raise Exception ( stdout )
#         except Exception as e :
#             raise e
#
#
#     def format(path) :
#         if path is None :
#             return ""
#
#         path = path.lstrip ()
#         path = path.rstrip ()
#
#         while path.find ( "/" ) >= 0 :
#             path = path.replace ( "/", "\\" )
#         while path.find ( "\\\\" ) >= 0 :
#             path = path.replace ( "\\\\", "\\" )
#
#         return path



class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str) #定义一个发送str的信号

    def __init__(self,parent=None):
        super(EmittingStr,self).__init__(parent)

    def write(self,text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass

class Plot_Chart(pg.GraphicsObject):
    def __init__(self,data:pd.DataFrame):
        pg.GraphicsObject.__init__(self)
        self.r, c = data.shape
        self.data = data
        self.chart()


    def chart(self):
        #pre-computing a QPicture object allows paint() to run much more quickly
        #rather than re-drawing the shapes every time.
        self.picture = pg.QtGui.QPicture()
        p = pg.QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('#FFFF00'))

        d = [ (self.data.iloc[ i ], i) for i in range ( self.r ) ]

        w = 0.25
        for ((dt,open,close,min,max),t) in d:
            p.drawLine(pg.QtCore.QPointF(t,min),pg.QtCore.QPointF(t,max))
            if open > close:
                p.setBrush(pg.mkBrush('#3498DB'))
            else:
                p.setBrush(pg.mkBrush('#E74C3C'))
            p.drawRect(pg.QtCore.QRectF(t-w,open,2*w,close-open))

        p.end()

    def paint(self,p,*args):
        p.drawPicture(0,0,self.picture)

    def boundingRect(self):
        return pg.QtCore.QRectF(self.picture.boundingRect())

        # self.picture = QtGui.QPicture()
        # p = QtGui.QPainter ( self.picture )
        # pg.setConfigOptions ( leftButtonPan=False, antialias=False )
        #
        # plt.rcParams['font.family'] = ['SumHei'] #正常显示中文
        # plt.rcParams['axes.unicode_minus'] = False #正常显示负号
        #
        # p.setPen ( QPen ( Qt.red, 1 ) )
        # p.setBrush ( QBrush ( Qt.green ) )
        #
        # w,i,open, close, max, min = 0.25,5,30,32,35,10
        # # self.candle = CandleChart.CandlestickItem ( data={'open' : [10,11], 'close' : [12,13], 'high' : [15,16], 'low' : [10,11]})
        # if open > close :
        #     p.drawLine ( QtCore.QPointF ( i, min ), QtCore.QPointF ( i, max ) )
        #     p.drawRect ( QtCore.QRectF ( i - w, open, w * 2, close - open ) )
        # else :
        #     if (max != close) :
        #         p.drawLine ( QtCore.QPointF ( i, max ), QtCore.QPointF ( i, close ) )
        #     if (min != open) :
        #         p.drawLine ( QtCore.QPointF ( i, open ), QtCore.QPointF ( i, min ) )
        #     if (close == open) :
        #         p.drawLine ( QtCore.QPointF ( i - w, open ), QtCore.QPointF ( i + w, open ) )
        #     else :
        #         p.drawLines (
        #             [ QtCore.QLineF ( QtCore.QPointF ( i - w, close ), QtCore.QPointF ( i - w, open ) ),
        #               QtCore.QLineF ( QtCore.QPointF ( i - w, open ), QtCore.QPointF ( i + w, open ) ),
        #               QtCore.QLineF ( QtCore.QPointF ( i + w, open ), QtCore.QPointF ( i + w, close ) ),
        #               QtCore.QLineF ( QtCore.QPointF ( i + w, close ), QtCore.QPointF ( i - w, close ) ) ] )
        # p.end ()
        # self.updateGeometry()



class AskUI(QtWidgets.QDialog):#QMainWindow

    table_name = 'count_benefit_statics_V6'

    # observe_0 = FSS_V6.TST( id=0, name=table_name, text='ui.textBrowser.append(str(self.observe_0.text))' )
    observe_1 = FSS_V6.Observe()
    ui = Ui_Dialog ()

    # data = [  ## fields are (time, open, close, min, max).
    #     (1., 10, 13, 5, 15),
    #     (2., 13, 17, 9, 20),
    #     (3., 17, 14, 11, 23),
    #     (4., 14, 15, 5, 19),
    #     (5., 15, 9, 8, 22),
    #     (6., 9, 15, 8, 16),
    # ]
    # table_column = np.array([
    # (1,   1.6,   'x'),
    # (3,   5.4,   'y'),
    # (8,   12.5,  'z'),
    # (443, 1e-12, 'w'),
    # ], dtype=[('Date', str), ('Code', str), ('Probably', str)])
    table_column = np.array ( [
        (' ', ' ', ' ')
        ], dtype=[ ('Date', str), ('Code', str), ('Probably', str) ] )

    conn = pymysql.connect ( user='root', host='localhost', port=3306, password='123321', db='a_stocks' )

    def __init__(self):
        # super(AskUI,self).__init__(parent=parent)
        super().__init__()

        self.ui.setupUi(self)
        # self.ui.retranslateUi(self)

        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)


        self.ui.pBtn_1.clicked.connect ( lambda : self.task_update() )
        # self.ui.pBtn_1.clicked.connect ( lambda : self.observe_0.add_id() )
        # self.ui.pBtn_1.clicked.connect ( lambda : self._wish_Btn ( self.ui.pBtn_1 ) )

        self.ui.pBtn_2.clicked.connect ( lambda : self.task_find_stocks() )
        self.ui.pBtn_3.clicked.connect ( lambda : self.task_statics_count() )
        self.ui.pBtn_4.clicked.connect ( lambda : self.task_statics_present())

        self.tw = self.ui.tableWidget

        self.tw.setData ( data=self.table_column )
        self.tw.cellClicked.connect ( self.candle )


        # plt = pg.plot()


        # self.ui.tableWidget.setFormat(float,column=('time', 'open', 'close', 'min', 'max'))
        # self.ui.tableWidget.setHorizontalHeaderLabels()
        # self.ui.tableWidget.verticalHeadersSet = ('time', 'open', 'close', 'min', 'max')
        # self.ui.tableWidget.horizontalHeadersSet

        # layout =QtWidgets.QHBoxLayout()
        # layout.addWidget ( ppp, 1 )

        # plt.addItem(item)
        # self.ui.widget.addItem(item)
        # self._widget()



        # self.ui.tableWidget.itemClicked.connect(lambda : self._widget())



    def _widget(self):

        # x = self.ui.tableWidget
        # r = self.ui.tableWidget.SelectColumns
        # w = self.ui.tableWidget.SelectRows
        # c = self.ui.tableWidget.cellClicked.connect(self.tprint)
        #
        # selected = self.ui.tableWidget.item(1,1)
        # print(f'第1行第1列的值为： {selected.value}')
        #
        #
        # item = Plot_Chart ( self.data )
        # self.ui.graphicsView.addItem ( item )
        #
        # for i in self.ui.tableWidget.items :
        #     print ( f'item is: {i.value}:{i.value}' )
        pass

    def candle(self,row, col) :
        code = self.tw.item(row,1)
        print ( f'\nselected code is = {code}\n' )
        name = "s_" + code.value

        print(f'\nselected code is = {code.value}\n')

        cursor = self.conn.cursor ()

        cmd1 = "SELECT `date`,`startPrice`,`endPrice`,`minPrice`,`maxPrice` FROM " + name + " ORDER BY `date` DESC LIMIT 50"
        cursor.execute ( cmd1 )
        df = pd.DataFrame ( cursor.fetchall (), columns=[ "time", "open", "close", "min", "max" ],
                            dtype=float )
        # 先进行数据清洗
        df.dropna ( axis=0, how='any', thresh=None, subset=[ "time", "open", "close", "min", "max"  ],
                    inplace=False )
        # r, c = df.shape
        df_reverse = df.iloc[ : :-1 ]  # 最近20个交易日数据逆序
        df_reverse.reset_index(drop=True)

        # print(f'\ndf_reverse type = {type(df_reverse)}\n')

        # data = [ df_reverse.iloc[i] for i in range(r)]
        # print ( f'\ndata type = {type ( data )}\n' )
        # print ( f'\ndata = { data }\n' )
        item = Plot_Chart ( df_reverse )#self.data
        self.ui.graphicsView.addItem ( item )
        # self.ui.graphicsView.removeItem ()

        print ( f'selected cells rows is {row}, columns is {col}' )

    def outputWritten(self,text):
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition ( QtGui.QTextCursor.End )
        cursor.insertText ( text )
        self.ui.textBrowser.setTextCursor ( cursor )
        self.ui.textBrowser.ensureCursorVisible ()

    def task_update(self):
        t = Thread ( target=Data_update()._update )
        t.start ()

    def task_find_stocks(self):
        # from multiprocessing.pool import Pool
        # _pool = Pool(processes=3)
        # r1 = _pool.apply_async(self.observe_1.investment_v6)
        # # print(f'r1 = {r1}\nr2 = {r2}\nr3 = {r3}\nr4 = {r4}\n')
        # print ( f'r1 = {r1}\n' )
        pool = ThreadPoolExecutor(max_workers=2)
        t = pool.submit(self.observe_1.investment_v6)
        t.done()
        r1,r2,r3,r4 = t.result()
        [ self.tw.appendRow(s) for s in r1 ]
        [ self.tw.appendRow ( s ) for s in r2 ]
        [ self.tw.appendRow ( s ) for s in r3 ]
        [ self.tw.appendRow ( s ) for s in r4 ]
            # _pool.close()
        pool.shutdown()
        # r1 = r2 = r3 = r4 = []
        # t = Thread(target=self.observe_1.investment_v6,args=(r1,r2,r3,r4))
        # t.start()
        # t.join()    #等待进程结束后退出
        # [ self.tw.appendRow ( s ) for s in r1 ]
        # [ self.tw.appendRow ( s ) for s in r2 ]
        # [ self.tw.appendRow ( s ) for s in r3 ]
        # [ self.tw.appendRow ( s ) for s in r4 ]

    def task_statics_count(self):
        t = Thread ( target=FSS_V6.count_benefit_statics_V6,args=(self.table_name,) )
        t.start ()

    def task_statics_present(self):
        t = Thread ( target=self.observe_1.present_statics_V6 )
        t.start ()

class Data_update():
    dbname = 'a_stocks'
    stocksListTable = 'list_a_stocks'  # 存储深交所和上交所A股列表，并添加相应的字段标识状态
    holidays = [ '2022-01-03', '2022-01-31', '2022-02-01', '2022-02-02', '2022-02-03', '2022-02-04',
                 '2022-04-04', '2022-04-05', '2022-05-02', '2022-05-03', '2022-05-04', '2022-06-03', '2022-09-12',
                 '2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07' ]  # 当年的法定假日
    tableColumns = [ 'date', 'code', 'name', 'endPrice', 'maxPrice', 'minPrice', 'startPrice', 'preEndPrice',
                     'diffPrice', 'diffPercent', 'turnoverPercent', 'tradeVolume', 'tradeAmount',
                     'totalMarketValue', 'MCAP', 'PE' ]
    def __init__(self):
        self.logger = self._getLogger()


    def _update(self):

        # 更新数据库中的记录，需要用到conn.commit()，执行后conn只能关闭后再重新开启了
        # resetUpdatedFlag ( stocksListTable ) #重置数据库中的标志位
        # self.logger.info ( "complete step 1: running into while ...." )
        # while self.run :
        # open DB
        self.start = time.time ()
        connection = RSD.connect_mysql ()

        ways: tuple = RSD.distinguish_update_way_list ( connection, self.stocksListTable, self.holidays, self.tableColumns )
        self.logger.info ( "complete step 1: complete  RSD.distinguish_update_way_list...." )
        print('complete step 1: complete  RSD.distinguish_update_way_list....')
        oneday_more_list: list = ways[ 0 ]
        oneday_list: list = ways[ 1 ]
        nearst_day_str: str = ways[ 2 ]

        # 读取数据之前，先去除冗余
        # clean redundant rows for every tables
        e1 = RSD.clean_redundant_rows ( connection, self.stocksListTable )
        self.logger.info ( "complete step 2: connect to mysql and clean redundant ...." )
        print('complete step 2: connect to mysql and clean redundant ....')
        if e1 :
            self.logger.info ( f"step 2 ERROR: {e1}" )
            print(f'step 2 ERROR: {e1}')

        if len ( oneday_more_list ) > 0 :
            # update_oneday_mare
            for slt in oneday_more_list :
                upd_tuple = RSD.update_oneday_more ( slt, self.holidays, nearst_day_str )
                upd_list = upd_tuple[ 0 ]
                s_table_name = upd_tuple[ 1 ]
                self.logger.info ( f"complete step 3: complete  RSD.update_oneday_more....for table:{s_table_name}" )
                print(f'complete step 3: complete  RSD.update_oneday_more....for table:{s_table_name}')
                e2 = RSD.add_record ( connection, upd_list, s_table_name, self.tableColumns )
                if e2 :
                    self.logger.info ( f"step 4: call  RSD.add_record....\n ERROR: {e2}" )
                    print(f'step 4: call  RSD.add_record....\n ERROR: {e2}')

                # e3 = RSD.reflash_stocks_list_table ( connection, s_table_name, stocksListTable )
                # if e3:self.logger.info (
                #     f"step 5: call  RSD.reflash_stocks_list_table....\n ERROR: {e3}" )
                # self.logger.info ( f"complete step 3: complete  RSD.update_oneday_more...." )
                # self.logger.info ( f"complete step 4: complete  RSD.add_record...." )
                # self.logger.info ( f"complete step 5: complete  RSD.reflash_stocks_list_table....{stocksListTable}\n Exception e = {e}" )
        if len ( oneday_list ) > 0 :
            e3 = RSD.update_oneday ( connection, oneday_list, self.tableColumns, self.stocksListTable, self.holidays )
            self.logger.info ( f"complete step 5: RSD.update_oneday...." )
            print('complete step 5: RSD.update_oneday....')
            if e3 :
                self.logger.info ( f"step 5...... ERROR: {e3}" )
                print(f'step 5...... ERROR: {e3}')
        self.logger.info ( ">>> 数据库中的股票交易数据已经更新到最新状态 ！" )
        print('>>> 数据库中的股票交易数据已经更新到最新状态 ！')
        # clean redundant rows for every tables
        e4 = RSD.clean_redundant_rows ( connection, self.stocksListTable )
        self.logger.info ( f'清除冗余数据......' )
        print('清除冗余数据......')
        if e4 :
            self.logger.info ( f'clean redundant...... ERROR：{e4}' )
            print(f'clean redundant...... ERROR：{e4}')

        # 更新list_a_stocks列表
        cmd = "SELECT `tablename` FROM " + self.stocksListTable + " WHERE `delisted` NOT LIKE '1'"
        cursor = connection.cursor ()
        cursor.execute ( cmd )
        stable_list = list ( chain.from_iterable ( cursor.fetchall () ) )
        for s_table_name in stable_list :
            e5 = RSD.reflash_stocks_list_table ( connection, s_table_name, self.stocksListTable )
            if e5 :
                self.logger.info (
                f"step 6: call  RSD.reflash_stocks_list_table...... ERROR: {s_table_name}->>>{e5}" )
                print(f'step 6: call  RSD.reflash_stocks_list_table...... ERROR: {s_table_name}->>>{e5}')
        self.logger.info ( f'列表{self.stocksListTable}完成更新......' )
        print(f'列表{self.stocksListTable}完成更新......')
        # # 放量锤头形态的捕获功能
        # hammer_list = RSD.find_hammer_head_line ( connection, stocksListTable )
        # self.logger.info ( f'近期出现放量锤头的股票共{len ( hammer_list )}只请关注：\n {hammer_list} ！' )
        # # close DB
        connection.close ()
        # 服务启动之后，执行一次更新，之后等待6个小时
        # self.logger.info ( "complete step ?: waiting for 6 hours ...." )
        self.end = time.time ()
        self.logger.info ( f"ASK commission completed....Used {round ( self.end - self.start, 3 )}s \n" )
        print(f'ASK commission completed....Used {round ( self.end - self.start, 3 )}s \n')
        # win32event.WaitForSingleObject ( self.hWaitStop, win32event.INFINITE )  # 等待服务被停止
        # win32event.WaitForSingleObject ( self.hWaitStop, win32event.QS_ALLEVENTS )  # 等待服务被停止

    def _getLogger(self):
        logger = logging.getLogger('[AskUI]')
        this_file = inspect.getfile(inspect.currentframe())
        dir_path = os.path.abspath(os.path.dirname(__file__))
        handler = logging.FileHandler(os.path.join(dir_path,"ASK.log"))
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger


class Print_str(object):



    def _wish_Btn(self,btn):
        print(f'点击Button名为{btn.text()}')
        # print(f'observe id = {self.observe_0.id}' )
        # print ( f'observe name = {self.observe_0.name}' )
        # print ( f'observe text = {self.observe_0.text}' )

    def _show_tex(self,btn):
        self.ui.textBrowser.append ( btn.text() )


if __name__=="__main__":
    # import sys
    # if (sys.flags.interactive != 1) or not hasattr ( QtCore, 'PYQT_VERSION' ) :
    #     QtGui.QApplication.instance ().exec_ ()

    app = QtWidgets.QApplication(sys.argv)
    win = AskUI()
    # win = Plot_widget()
    win.show()
    sys.exit(app.exec_())

# 升版方向包括：
# 1.下载交易数据功能仍然由服务程序完成，本GUI程序开机自启动，本程序启动后首先启动服务程序
# 2.针对各种策略的本日数据分析和今日推荐股票代码，也由本程序运行后启动的服务进程完成，筛选的股票代码被存储在数据库特定的表中
# 3.GUI程序界面只完成快速响应的交互操作，能够从已经筛选的数据表中读取数据，并在图形化界面上进行展示
# 4.继续扩大选股策略，重点分析股价低的数据和交易量随着股票下跌而持续收缩，随着股价反弹而放量的现象
# 5.下一步突破自动交易的实现方式
# 6.考虑在Nexus5上安装Linux系统，并将交易数据库及更新程序转移到Nexus5上
# 7.针对虚拟选出的股票，持续更新5-10天，统计成功率，模拟交易盈亏概率，虚拟交易
# 8.今日推荐的股票信息，自动通过微信、邮箱等渠道发送到手持终端
# 9.不断重构代码，提高代码复用率，提高代码编写熟练度和相关技巧
