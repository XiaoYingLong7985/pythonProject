import inspect
import os
import sys

import numpy as np
import pandas as pd
import pymysql
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import mmap

f = inspect.getfile ( inspect.currentframe () )
d = os.path.abspath ( os.path.dirname ( f ) )
c = os.path.join ( d, 'ZLService.log' )
conn = pymysql.connect ( user='root', host='localhost', port=3306, password='123321', db='a_stocks' )
cursor = conn.cursor ()

cmd1 = "SELECT `date`,`startPrice`,`endPrice`,`minPrice`,`maxPrice` FROM " + "s_000021" + " ORDER BY `date` DESC LIMIT 20"
cursor.execute ( cmd1 )
df = pd.DataFrame ( cursor.fetchall (), columns=[ "time", "open", "close", "min", "max" ],
                    dtype=float )
# 先进行数据清洗
df.dropna ( axis=0, how='any', thresh=None, subset=[ "time", "open", "close", "min", "max"  ],
            inplace=False )
r, c = df.shape
df_reverse = df.iloc[ : :-1 ]  # 最近20个交易日数据逆序
df_reverse.reset_index(drop=True)

data = [ (df_reverse.iloc[i],i) for i in range(r)]

for ((dt,open,close,min,max),t) in data:
    print(f'dt,open,close,min,max,t = {dt},{open},{close},{min},{max},{t}')

mm = mmap.mmap(-1,1024,tagname='mm',access=mmap.ACCESS_WRITE,offset=0)
mm.seek(0)
mm.write('start')
os.chdir(sys.path[0])
os.system('ASKUI.py')
mm.seek(0)
mm.write('quite')
mm.close()



picture = pg.QtGui.QPicture()
p = pg.QtGui.QPainter(picture)
p.setPen(pg.mkPen('#FFFF00'))

random_str = lambda : (''.join([chr(np.random.randint(ord('A'),ord('z'))) for i in range(np.random.randint(1,5))]), np.random.randint(0, 360))
x = pg.PlotDataItem ()

x.sigClicked.connect (lambda :con())
print('hahaha...')

n=300

def con():
    n=300
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]


