import struct
import sys
import time
from functools import wraps
from threading import Thread
import pandas as pd
import os


def setlog(func):
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    #将funcs的元信息复制给run函数
    log_file = 'C:\PycharmProjects\pythonProject\logs\setlog.log'
    @wraps(func)
    def run(*args) :
        with open(log_file, 'a+') as f:
            f.write(f'{func.__name__}, {log_file}')
            pass
        return func
    return run

# @setlog
def animation(func_name, *args, **kwargs):
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    try:
        ani_str = '|/-\\'
        while (1) :
            for i in range ( len ( ani_str ) ) :
                print ( f'\r {func_name}正在运行： {ani_str[ i ]}', end='' )
                time.sleep ( 0.25 )
    except Exception as e:
        print( f' animation cause Error : {e}')


class CreatePics():

    def __init__(self, columns_list=None, trade_days_limit=1000, root_path='c:\\zd_swhy\\vipdoc',):
        if columns_list==None:
            self.columns_list = [ 'Open', 'High', 'Low', 'Close', 'Volume' ]
        else:
            self.columns_list = columns_list

        self.trade_days_limit = trade_days_limit
        self.root_path = root_path

    def readBinaryAsDataFrame(self, file, *args, **kwargs)->pd.DataFrame:
        """ what's this
            每次从本都读取文件的方式都是一样的，对于不同的数据需求，可以在输出的dataFrame中切片
            这样做的好处是，不需要每读一条记录都取判断一下是否相应的列被选中，提高读取效率
        Args:
            arg:
        Raises:
            error:

        """
        try:
            lst = [ ]
            rec = 0
            with open ( file, 'rb' ) as o :  # 'rb'代表以二进制形式的字节类型读入
                while (1) :
                    content = o.read ( 32 )
                    lens = content.__len__ ()
                    if lens >= 32 and rec <= self.trade_days_limit:
                        dic = {}
                        b_tup = struct.unpack_from ( '<IIIIIIII', content, 0 )  # fmt- <代表小端，I代表无符号int类型
                        dic[ 'date' ] = '-'.join ([ str ( b_tup[ 0 ] )[ :4 ], str ( b_tup[ 0 ] )[ 4 :6 ], str ( b_tup[ 0 ] )[ 6 : ] ] )
                        dic[ 'open' ] = round ( b_tup[ 1 ] / 100, 2 )
                        dic[ 'pmax' ] = round ( b_tup[ 2 ] / 100, 2 )
                        dic[ 'pmin' ] = round ( b_tup[ 3 ] / 100, 2 )
                        dic[ 'clos' ] = round ( b_tup[ 4 ] / 100, 2 )
                        dic[ 'tnov' ] = round ( float ( b_tup[ 6 ] ) / 1000000, 2 )

                        tup = (dic[ 'open' ], dic[ 'pmax' ], dic[ 'pmin' ], dic[ 'clos' ], dic['tnov' ])
                        lst.append ( tup )
                        rec += 1

                    else :
                        break
            o.close ()
            #默认最多读取1000条记录
            return pd.DataFrame(lst, self.columns_list)

        except Exception as e:
            print( f'readBinaryAsDataFrame cause Error : {e}')

    def getStocksFileWithPathAsList(self, *args, **kwargs)->list:
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try:
            lst = [ ]
            for root, dirs, files in os.walk ( self.root_path ) :
                if files :
                    for file in files :
                        if file[ :4 ] == 'sh60' or file[ :4 ] == 'sz00' :
                            lst.append ( root + '\\' + file )
            return lst

        except Exception as e:
            print( f'getStocksFileWithPathAsList cause Error : {e}')




if __name__ == '__main__':


    ani = Thread(target=animation,args='sys')
    # time.sleep ( 5 )
    ani.start()
    ani.join(timeout=5)

    sys.exit()