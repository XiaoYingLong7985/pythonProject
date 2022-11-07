import os
import random
import struct
import sys
import time
import numpy as np
from datetime import datetime
from functools import wraps
from threading import Thread

import mplfinance as mpf  # 金融画图库
import pandas
import pandas as pd
import time

#计算函数耗时的装饰器
def timer(func):
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    @wraps( func )
    def func_wrapper(*args, **kwargs):
        start = time.time()
        re = func(*args, **kwargs)
        end = time.time()
        spend = end - start
        if spend * 1000 > 10:
            print(f'{func.__name__} cost {round(spend * 1000, 3)} ms')
        return re
    return func_wrapper

#记录函数调用信息的装饰器
def setlog(func) :
    """ what's this

    Args:

    Raises:
        error:

    """
    # 将funcs的元信息复制给run函数
    log_file = 'C:\PycharmProjects\pythonProject\logs\setlog.log'

    @wraps ( func )
    def run(*args, **kwargs) :
        with open ( log_file, 'a+' ) as f :
            f.write ( f'{func.__name__} run at: {datetime.fromtimestamp ( time.time () )} \r' )

        return func(*args, **kwargs)

    return run


# @setlog
def animation(*args, **kwargs) :
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    try :
        ani_str = '|/-\\'
        iterator = 0
        while (1) :
            i = iterator % 4
            print ( f'\r  程序正在运行： {ani_str[ i ]}', end='' )
            iterator += 1
            time.sleep ( 0.25 )
    except Exception as e :
        print ( f' animation cause Error : {e}' )

def openAnimation(open=True, *args, **kwargs):
    """ what's this

    Args:
        arg:
    Raises:
        error:

    """
    try:
        if open:
            # 通过arg='string'的形式传递字符串，只能显示第一个字符，应将arg=('string',)转化成tuple类型
            ani = Thread ( target=animation )
            # 通过setDaemon(true)来设置线程为“守护线程”
            ani.setDaemon ( True )
            ani.start ()
            ani.join ( timeout=0.2 )
    except Exception as e:
        print( f' openAnimation cause Error : {e}')


class CreatePics () :
    classes_list = [ 'rise', 'climb', 'drop', 'slide', 'uncertain', 'riseX', 'dropX' ]

    def __init__(self, columns_list=None,
                 trade_days_limit=1000,
                 root_path='C:\\zd_swhy\\vipdoc',
                 stocks_need=30,
                 draw_days=50,
                 save_path='C:\\Users\\binli\\JupyterNotebook\\',
                 w=2.7, h=2.7,
                 bac_ratio=1.06,
                 ris_ratio=1.30,
                 climb_ratio=1.15,
                 pics_limit=3
                 ) :
        if columns_list == None :
            self.columns_list = [ 'Date', 'Open', 'High', 'Low', 'Close', 'Volume' ]
        else :
            self.columns_list = columns_list

        self.trade_days_limit = trade_days_limit
        self.root_path = root_path
        self.stocks_need = stocks_need
        self.draw_days = draw_days
        self.idx_open = self.columns_list.index( 'Open' )
        self.idx_low = self.columns_list.index ( 'Low' )
        self.idx_high = self.columns_list.index ( 'High' )
        self.idx_close = self.columns_list.index ( 'Close' )
        self.idx_volume = self.columns_list.index('Volume')
        self.save_path = save_path
        self.timeStamp = self.__class__.__name__ + '_' + datetime.today ().strftime ( '%Y%m%d' )
        self.w = w
        self.h = h
        self.bck_ratio = bac_ratio
        self.ris_ratio = ris_ratio
        self.climb_ratio = climb_ratio
        self.pics_limit = pics_limit

        self.createFolders ()

    def makeFolder(self, path, folder, *args, **kwargs) :
        """ what's this
        
        Args:
            arg:
        Raises:
            error:
            
        """
        try :
            folderWithPath = path + '\\' + folder
            if os.path.exists ( path=folderWithPath ) :
                pass
            else :
                os.mkdir ( path=folderWithPath )

        except Exception as e :
            print ( f' makeFolder cause Error : {e}' )

    @setlog
    def createFolders(self, *args, **kwargs) :
        """ what's this
        
        Args:
            arg:
        Raises:
            error:
            
        """
        try :
            self.makeFolder ( self.save_path, self.timeStamp )
            path = self.save_path + '\\' + self.timeStamp
            self.makeFolder ( path, 'train' )
            self.makeFolder ( path, 'random' )
            self.makeFolder ( path, 'newest' )

            trainPath = path + '\\' + 'train'
            for cls in self.classes_list :
                self.makeFolder ( trainPath, cls )

        except Exception as e :
            print ( f' createFolders cause Error : {e}' )

    # @timer
    def readBinaryAsDataFrame(self, file, *args, **kwargs) -> pd.DataFrame :
        """ what's this
            每次从本都读取文件的方式都是一样的，对于不同的数据需求，可以在输出的dataFrame中切片
            这样做的好处是，不需要每读一条记录都取判断一下是否相应的列被选中，提高读取效率
        Args:
            arg:
        Raises:
            error:

        """
        try :
            lst = [ ]
            # rec = 0
            with open ( file, 'rb' ) as o :  # 'rb'代表以二进制形式的字节类型读入
                while (1) :
                    content = o.read ( 32 )
                    lens = content.__len__ ()
                    if lens >= 32 :# and rec <= self.trade_days_limit :
                        dic = {}
                        b_tup = struct.unpack_from ( '<IIIIIIII', content, 0 )  # fmt- <代表小端，I代表无符号int类型
                        dic[ 'date' ] = '-'.join (
                            [ str ( b_tup[ 0 ] )[ :4 ], str ( b_tup[ 0 ] )[ 4 :6 ], str ( b_tup[ 0 ] )[ 6 : ] ] )
                        dic[ 'open' ] = round ( b_tup[ 1 ] / 100, 2 )
                        dic[ 'pmax' ] = round ( b_tup[ 2 ] / 100, 2 )
                        dic[ 'pmin' ] = round ( b_tup[ 3 ] / 100, 2 )
                        dic[ 'clos' ] = round ( b_tup[ 4 ] / 100, 2 )
                        dic[ 'tnov' ] = round ( float ( b_tup[ 6 ] ) / 1000000, 2 )

                        tup = (dic[ 'date' ], dic[ 'open' ], dic[ 'pmax' ], dic[ 'pmin' ], dic[ 'clos' ], dic[ 'tnov' ])
                        lst.append ( tup )
                        # rec += 1

                    else :
                        break
            o.close ()
            # 默认最多读取1000条记录
            return pd.DataFrame ( data=lst, columns=self.columns_list ).tail(n=self.trade_days_limit)

        except Exception as e :
            print ( f'readBinaryAsDataFrame cause Error : {e}' )

    # @timer
    def getStocksFileWithPathAsList(self, *args, **kwargs) -> list :
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try :
            lst = [ ]
            for root, dirs, files in os.walk ( self.root_path ) :
                if files :
                    for file in files :
                        if file[ :4 ] == 'sh60' or file[ :4 ] == 'sz00' :
                            lst.append ( root + '\\' + file )
            return lst

        except Exception as e :
            print ( f'getStocksFileWithPathAsList cause Error : {e}' )

    @setlog
    @timer
    def checkFilterPolicy(self, *args, **kwargs):
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try:
            self.ant, self.vnt = 0, 0
            for file_name_with_path in self.getStocksFileWithPathAsList () :
                file_name = file_name_with_path.split ( '\\' )[ -1 ].split ( '.' )[ -2 ]
                dfi = self.readBinaryAsDataFrame ( file_name_with_path )
                # dfi = dfi.reset_index(drop=True)

                rows = dfi.shape[ 0 ]
                # ant, vnt = 0, 0
                for i in range(rows - 10 - 1):
                    # #每循环一次，去掉最后一行
                    df = dfi.iloc[ :rows - i - 1, ]
                    # dfi.drop(axis=0, index=(rows - i - 1), inplace=True)
                    # # print( f'last line of df = {dfi.iloc[ -1 ]} \n last line of dfi = {dfi.iloc[ -1 ]}')
                    # # 最后10行用作验证
                    # dfv = dfi.tail ( n=10 )
                    # dfv = dfv.reset_index(drop=True)
                    # open_pri = dfv.iloc[0, self.idx_open]
                    # close_pri = dfv.iloc[0, self.idx_close]
                    # # 取出不含最后10行的数据
                    # dfc = dfi.iloc[:-10,]
                    # dfc = dfc.reset_index(drop=True)
                    # today_close_pri = dfc.iloc[-1, self.idx_close]
                    # today_low_pri = dfc.iloc[-1, self.idx_low]

                    # if (open_pri >= today_close_pri and close_pri > today_low_pri) or (open_pri < today_close_pri and close_pri > today_close_pri):
                    #     if self.filterPolicyAsBool(dfc):
                    #         ant += 1
                    #         if dfv.iloc[:,self.idx_high].max() >= today_close_pri * 1.05:
                    #             vnt += 1
                    self.splitOnceForSpendTimeMeasure(df, file_name)

                # print(f'{file_name} , {vnt}/{ant} , {vnt/ant if ant else 1}')
            print(f'vnt / ant = {self.vnt}/{self.ant} = {self.vnt/self.ant}')

        except Exception as e:
            print( f'  cause Error : {e}')

    #@timer
    def splitOnceForSpendTimeMeasure(self, df, file_name, *args, **kwargs):
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try:
            # 每循环一次，去掉最后一行
            # df = dfi.iloc[ :rows - i - 1, ]
            # dfi.drop ( axis=0, index=(rows - i - 1), inplace=True )
            # print( f'last line of df = {dfi.iloc[ -1 ]} \n last line of dfi = {dfi.iloc[ -1 ]}')
            # 最后10行用作验证
            dfv = df.tail ( n=10 )
            dfv = dfv.reset_index ( drop=True )
            open_pri = dfv.iloc[ 0, self.idx_open ]
            close_pri = dfv.iloc[ 0, self.idx_close ]
            # 取出不含最后10行的数据
            dfc = df.iloc[ :-10, ]
            ## dfc = dfc.reset_index ( drop=True )
            today_close_pri = dfc.iloc[ -1, self.idx_close ]
            today_low_pri = dfc.iloc[ -1, self.idx_low ]

            if (self.filterPolicyAsBool ( dfc ) ) and ((open_pri >= today_close_pri and close_pri > today_low_pri) or (
                    open_pri < today_close_pri and close_pri > today_close_pri)) :
            # if self.filterPolicyAsBool ( dfc ) :
                self.ant += 1

                # if dfv.iloc[ :, self.idx_high ].max () >= close_pri * 1.05 :
                if dfv.iloc[ :, self.idx_high ].max () >= today_close_pri * 1.05 :
                    self.vnt += 1
                    portfolio = self.save_path + 'CreatePics_20221107\\'#gain+5
                    self.draw_pics(df.iloc[-60:,], pic_name=''.join([file_name,'_',str(self.ant)]), save_portfolio_abs=portfolio, lab=True)
                else:
                    pass
                    portfolio = self.save_path + 'CreatePics_20221107\\'#gain+5nan
                    self.draw_pics(df.iloc[-60:,], pic_name=''.join([file_name,'_',str(self.ant)]), save_portfolio_abs=portfolio, lab=True)
            # return ant, vnt
        except Exception as e:
            print( f' splitOnceForSpendTimeMeasure cause Error : {e}')

    # @timer
    def filterPolicyAsBool(self, df:pandas.DataFrame, *args, **kwargs)->bool:
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try:
            flg = False
            lft = int (df.iloc[ -10 :, self.idx_low : self.idx_low + 1 ].reset_index ( drop=True ).idxmin ( axis=0 )[ 0 ] )
            # print ( f'lft = {lft}, types = {type(lft), type(8)}, isTrue = {lft == 8}' )
            # cnt += 1

            # 昨日最低价是最近10日中的最低价
            if lft == 8 :  # 从0开始计数
                per2 = df.iloc[ -3, self.idx_low ]
                per3 = df.iloc[ -4, self.idx_low ]
                per4 = df.iloc[ -5, self.idx_low ]
                per5 = df.iloc[ -6, self.idx_low ]
                # 大前天、前天、昨日的最低价越来越低
                lft_mean =  (per2 + per3) * 0.5#np.mean ( list ( df.iloc[ -4 : -3, self.idx_low ] ) )
                rht_mean =  (per4 + per5) * 0.5#np.mean ( list ( df.iloc[ -6 :-5, self.idx_low ] ) )
                # print(f'{type(lft_mean),lft_mean} is < {rht_mean,type(rht_mean)}, {lft_mean < rht_mean}')
                if lft_mean < rht_mean :
                    # print('aaa')
                    day0 = df.iloc[-1,self.idx_volume]
                    day1 = df.iloc[-2,self.idx_volume]
                    day2 = df.iloc[-3,self.idx_volume]
                    day3 = df.iloc[-4,self.idx_volume]
                    day4 = df.iloc[-5,self.idx_volume]
                    # 最近2天交易量突然增大
                    lft_sum = day0 + day1 #np.sum ( list ( df.iloc[ -2 :-1, self.idx_volume ] ) )
                    rht_sum = day2 + day3 + day4 #np.sum ( list ( df.iloc[ -5 :-3, self.idx_volume ] ) )
                    # print ( f'{type ( lft_sum ), lft_sum} is > {rht_sum, type ( rht_sum )}, {lft_sum > rht_sum}' )
                    if (lft_sum > rht_sum) and (day0 > day1):
                        # 保持到本地磁盘
                        flg = True
            return flg

        except Exception as e:
            print( f' filterPolicy cause Error : {e}')


    @setlog
    @timer
    def saveNewestPics(self, offset_days=None, *args, **kwargs):
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try:
            pass
            #1、最近2天交易量突然增大，同时此前的约10天内快速下跌，趋势很陡峭
            #2、当日最低价>昨日最低价
            #3、昨日最低价是最近5日中的最低价
            #4、大前天、前天、昨日的最低价越来越低
            #5、
            # cnt = 0
            for file_name_with_path in self.getStocksFileWithPathAsList () :
                if self.stocks_need:
                    file_name = file_name_with_path.split ( '\\' )[ -1 ].split ( '.' )[ -2 ]
                    dfi = self.readBinaryAsDataFrame ( file_name_with_path )

                    if offset_days is not None:
                        df = (dfi.iloc[:(-1 * offset_days),]).tail(n=self.draw_days)
                    else:
                        df = dfi.tail(n=self.draw_days)
                    # df = df.tail(n=self.draw_days)
                    # df.reset_index(drop=True)

                    rows = df.shape[ 0 ]
                    if rows > 10 :#至少有10个交易日的数据记录
                        portfolio = self.save_path + self.timeStamp + '\\' + 'newest\\'

                        # # if (df.iloc[:-10, self.idx_low: self.idx_low + 1].reset_index(drop=True).idxmax(axis=0)[0]) == 25:
                        # #     print('\n',f'portfolio = {portfolio}')
                        # # print('\n',f'{df.iloc[:-10, self.idx_low: self.idx_low + 1].reset_index(drop=True).idxmax(axis=0)[0]}')
                        # # self.stocks_need -= 1
                        # # print ( '\n', f'{self.draw_days - 2}' )
                        # lft = int(df.iloc[-10:, self.idx_low: self.idx_low + 1].reset_index(drop=True).idxmin(axis=0)[0])
                        # # print ( f'lft = {lft}, types = {type(lft), type(8)}, isTrue = {lft == 8}' )
                        # # cnt += 1
                        #
                        # # 昨日最低价是最近10日中的最低价
                        # if lft == 8:#从0开始计数
                        #     #大前天、前天、昨日的最低价越来越低
                        #     lft_mean = float(np.mean(list(df.iloc[-4: -3, self.idx_low])))
                        #     rht_mean = float(np.mean(list(df.iloc[-6:-5,self.idx_low])))
                        #     # print(f'{type(lft_mean),lft_mean} is < {rht_mean,type(rht_mean)}, {lft_mean < rht_mean}')
                        #     if lft_mean < rht_mean:
                        #         # print('aaa')
                        #         #最近2天交易量突然增大
                        #         lft_sum = float(np.sum(list(df.iloc[-2:-1, self.idx_volume])))
                        #         rht_sum = float(np.sum(list(df.iloc[-5:-3, self.idx_volume])))
                        #         # print ( f'{type ( lft_sum ), lft_sum} is > {rht_sum, type ( rht_sum )}, {lft_sum > rht_sum}' )
                        #         if lft_sum > rht_sum:
                        if self.filterPolicyAsBool(df):
                            #保持到本地磁盘
                            self.draw_pics ( df=df, pic_name=file_name, save_portfolio_abs=portfolio )
                            self.stocks_need -= 1

            # print(f'cnt = {cnt}')
        except Exception as e:
            print( f' saveNewestPics cause Error : {e}')


    @setlog
    def saveTrainingPics(self, *args, **kwargs) :
        """ what's this
        
        Args:
            arg:
        Raises:
            error:
            
        """
        try :
            # cnt = 0
            for file_name_with_path in self.getStocksFileWithPathAsList () :
                if self.stocks_need :
                    file_name = file_name_with_path.split ( '\\' )[ -1 ].split ( '.' )[ -2 ]
                    dfx = self.readBinaryAsDataFrame ( file_name_with_path )
                    self.classification (file_name=file_name, df=dfx )

                    # 转圈显示程序正在运行
                    # animation(inspect.stack()[0][3])
                    # cnt += 1

                    self.stocks_need -= 1

                else :
                    break
        except Exception as e :
            print ( f' saveTrainingPics cause Error : {e}' )

    @setlog
    def saveTestingPics(self, *args, **kwargs) :
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try :
            # cnt = 0
            for file_name_with_path in self.getStocksFileWithPathAsList () :
                file_name = file_name_with_path.split ( '\\' )[ -1 ].split ( '.' )[ -2 ]
                df = self.readBinaryAsDataFrame ( file_name_with_path )

                # # 转圈显示程序正在运行
                # animation ( inspect.stack ()[ 0 ][ 3 ], cnt )
                # cnt += 1

                rows = df.shape[ 0 ]
                if rows > self.draw_days :
                    rdm = int ( random.uniform ( self.draw_days, rows - self.draw_days ) )

                    portfolio = self.save_path + '\\' + 'random\\'
                    maxPrice_pre = df.iloc[ rdm : rdm + 10, self.idx_high ].max ()
                    close_price = df.iloc[ rdm, self.idx_close ]
                    if maxPrice_pre - close_price > 0 :
                        sign = '+'
                    else :
                        sign = '-'
                    percent = round ( (maxPrice_pre - close_price) / close_price * 100, 1 )
                    pic_name = file_name + '_' + sign + str ( percent )
                    self.draw_pics ( df=df.iloc[ rdm - self.draw_days :rdm ], pic_name=pic_name,
                                     save_portfolio_abs=portfolio )
        except Exception as e :
            print ( f' saveTestingPics cause Error : {e}' )

    def draw_pics(self, df:pandas.DataFrame, pic_name, save_portfolio_abs, lab = False, *args, **kwargs) :
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try :
            if lab:
                x_lst = [np.nan for i in range(60)]
                x_lst[49] = df.iloc[49, self.idx_low]
                # add_plot = [mpf.make_addplot ( x_lst, scatter=True, markersize=100, marker='$\clubsuit$', color='m', alpha=0.5 ),]#mpf.make_addplot ( df[['Low']]) $\circledR$
                add_plot = [ mpf.make_addplot ( x_lst, scatter=True, markersize=200, marker='$\clubsuit$', color='lime', alpha = 0.9
                                                ), ]
            else:
                add_plot = []
            # print ( 'draw_pics ... \r', end='\r' )
            df.index = pd.DatetimeIndex ( df[ 'Date' ] )  # 用Data列的Datatime格式数据作为索引
            # save_path = "C:\\Users\\binli\\JupyterNotebook\\" + self.folder + "\\"
            mpf.plot ( df,
                       type='candle',
                       addplot=add_plot,
                       figsize=(self.w, self.h),
                       volume=True,
                       mav=(5, 10, 20),
                       figscale=1.0,  # 放大倍数
                       # xrotation=15,
                       # datetime_format='%Y-%m-%d',
                       tight_layout=True,
                       style=mpf.make_mpf_style ( base_mpf_style='nightclouds',
                                                  gridstyle='',
                                                  rc={'font.size' : '0'},
                                                  marketcolors=mpf.make_marketcolors ( up='white',  # white
                                                                                       down='red',
                                                                                       # edge='white',
                                                                                       wick='i',
                                                                                       volume={'up' : 'white',
                                                                                               'down' : 'cyan'}
                                                                                       )
                                                  ),
                       ylabel=' ',
                       ylabel_lower=' ',
                       show_nontrading=False,
                       volume_alpha=0.5,
                       volume_panel=0,

                       axisoff=True,
                       #              savefig=''.join(["C:\\Users\\binli\\JupyterNotebook\\pic\\",'f_',f[:8],'_',draws,'.jpg'])

                       savefig=''.join ( [ save_portfolio_abs, pic_name, '.jpg' ] )

                       )
            pass
        except Exception as e :
            print ( f' draw_pics cause Error : {e}' )

    def classification(self, file_name, df, *args, **kwargs) :
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try :
            rows = df.shape[ 0 ]
            if rows >= 2 :
                maxPrice_high = df.iloc[ -2, self.idx_high ]
                maxPrice_high_id = -2
                minPrice_high = df.iloc[ -1, self.idx_high ]
                minPrice_high_id = -1

                maxPrice_low = df.iloc[ -1, self.idx_low ]
                maxPrice_low_id = -1
                minPrice_low = df.iloc[ -2, self.idx_low ]
                minPrice_low_id = -2

                i, pics_r, pics_u, pics_c, pics_d, pics_s = 3, 0, 0, 0, 0, 0  # , 0, pics_ud
                cnt_r = 0  # 避免以1day的间隔连续保存多张图片, cnt_d, 0

                while i < (rows - 1) :
                    # temp = df.iloc[ -i ]
                    temp_high = df.iloc[ -i, self.idx_high ]  # 向左取出一个临近交易日的最高价
                    temp_low = df.iloc[ -i, self.idx_low ]  # 向左取出一个临近交易日的最低价

                    if temp_low > maxPrice_low :  # 如果临时价高于当前最高价，则刷新最高价，最低价默认为刷新后的最高价左侧临近交易日的最低价，更新最高、最低价格和他们的ID
                        maxPrice_low = temp_low
                        maxPrice_low_id = -i
                        minPrice_low_id = -(i + 1)
                        minPrice_low = df.iloc[ minPrice_low_id, self.idx_low ]
                    elif temp_low < minPrice_low :  # 如果临时价低于当前最低价，则刷新最低价及其ID
                        minPrice_low = temp_low
                        minPrice_low_id = -i
                    else :  # 如果临时价介于最低价和最高价之间时
                        if ((minPrice_low_id + 2) < 0) and (-1 * (minPrice_low_id - 48) <= df.shape[ 0 ]) :  # 满足df切片条件
                            dfs = df.iloc[ minPrice_low_id - 48 :minPrice_low_id + 2 ]

                            l_dfs_max = dfs.iloc[ :, self.idx_low ].max ()
                            l_dfs_min = dfs.iloc[ :, self.idx_low ].min ()
                            l_delta = l_dfs_max - l_dfs_min

                            if temp_low > ((2 - self.bck_ratio) * maxPrice_low) \
                                    and cnt_r >= 0 and pics_u < self.pics_limit \
                                    and (maxPrice_low_id - minPrice_low_id) > 25 :  # 如果临时价高于最高价的94%
                                # self.append_uncertain ( df=dfs )  # drawing_pic_uncertain_rise
                                self.savePicsByClassification ( self.classes_list[ 4 ], pics_u, file_name, dfs )

                                pics_u += 1
                                cnt_r = -1 * self.draw_days

                            elif temp_low < (self.bck_ratio * minPrice_low) :  # 如果临时价低于最低价的106%
                                pass
                            else :  # 临时价介于[1.06 * min, 0.94 * max]
                                if (maxPrice_low > self.ris_ratio * minPrice_low) and (pics_r < self.pics_limit) :  # 如果最高价已经超过最低价30%，就跳出循环体并返回他们的ID
                                    if temp_low < (l_dfs_min + 0.33 * l_delta):
                                        # self.append_rise ( df=dfs )  # drawing_pic_rise
                                        self.savePicsByClassification ( self.classes_list[ 0 ], pics_r, file_name, dfs )
                                    else:
                                        self.savePicsByClassification ( self.classes_list[ 5 ], pics_r, file_name, dfs )
                                        #classes_list = [ 'rise', 'climb', 'drop', 'slide', 'uncertain', 'riseX', 'dropX' ]
                                    pics_r += 1

                                elif (maxPrice_low > self.climb_ratio * minPrice_low) \
                                        and (temp_low < l_dfs_min + 0.5 * l_delta) \
                                        and (pics_c < self.pics_limit) :  # 如果最高价已经超过最低价15%，就跳出循环体并返回他们的ID
                                    # self.append_climb ( df=dfs )  # drawing_pic_climb
                                    self.savePicsByClassification ( self.classes_list[ 1 ], pics_c, file_name, dfs )
                                    # classes_list = [ 'rise', 'climb', 'drop', 'slide', 'uncertain' ]
                                    pics_c += 1

                                # else :# 否则，说明中间价格回升超过6%，为避免最大、最小价格之间有很多起伏，放弃之前确定的最高价，继续向左搜索
                                maxPrice_low = temp_low
                                maxPrice_low_id = -i
                                minPrice_low_id = -(i + 1)
                                minPrice_low = df.iloc[ minPrice_low_id, self.idx_low ]
                            cnt_r += 1
                        else :
                            pass

                    if temp_high > maxPrice_high :  # 如果临时价高于当前最高价，则刷新最高价
                        maxPrice_high = temp_high
                        maxPrice_high_id = -i
                    elif temp_high < minPrice_high :  # 如果临时价低于当前最低价，则刷新最低价及其ID# ，最高价默认为刷新后的最低价左侧临近交易日的价格，更新最高、最低价格和他们的ID
                        minPrice_high = temp_high
                        minPrice_high_id = -i
                        maxPrice_high_id = -(i + 1)
                        maxPrice_high = df.iloc[ maxPrice_high_id, self.idx_high ]
                    else :  # 如果临时价介于最低价和最高价之间时
                        if ((maxPrice_high_id + 2) < 0) and (
                                -1 * (maxPrice_high_id - 48) <= df.shape[ 0 ]) :  # 满足df切片条件
                            dfs = df.iloc[ maxPrice_high_id - 48 :maxPrice_high_id + 2 ]

                            h_dfs_max = dfs.iloc[ :, self.idx_high ].max ()
                            h_dfs_min = dfs.iloc[ :, self.idx_high ].min ()

                            h_delta = h_dfs_max - h_dfs_min

                            # if temp_high < (self.bck_ratio * minPrice_low) and cnt_d >= 0 and pics_ud < self.pics_limit: #如果临时价低于最低价的106%
                            #     self.savePic_uncertain_drop ( save_path=save_path, file_name=file_name, pics=pics_ud,
                            #                                   df=dfs )  # drawing_pic_uncertain_drop
                            #     pics_ud += 1
                            #     cnt_d = -50 #避免以1day的间隔连续保存多张图片
                            if temp_high > ((2 - self.bck_ratio) * maxPrice_high) or temp_high < (
                                    self.bck_ratio * minPrice_high) :  # 如果临时价高于最高价的94%
                                pass
                            else :  # 临时价介于[1.06 * min, 0.94 * max]
                                if (maxPrice_high > self.ris_ratio * minPrice_high) and (pics_d < self.pics_limit) :  # 如果最高价已经超过最低价30%，就跳出循环体并返回他们的ID
                                    if temp_high > (h_dfs_min + 0.66 * h_delta):
                                        # self.append_drop ( df=dfs )  # drawing_pic_drop
                                        self.savePicsByClassification ( self.classes_list[ 2 ], pics_d, file_name, dfs )
                                    else:
                                        self.savePicsByClassification ( self.classes_list[ 6 ], pics_d, file_name, dfs )
                                    pics_d += 1

                                elif (maxPrice_high > self.climb_ratio * minPrice_high) \
                                        and (temp_high > h_dfs_min + 0.5 * h_delta) \
                                        and (pics_s < self.pics_limit) :  # 如果最高价已经超过最低价15%，就跳出循环体并返回他们的ID
                                    # self.append_slide ( df=dfs )  # drawing_pic_slide
                                    self.savePicsByClassification ( self.classes_list[ 3 ], pics_s, file_name, dfs )
                                    # classes_list = [ 'rise', 'climb', 'drop', 'slide', 'uncertain' ]
                                    pics_s += 1

                                # else :# 否则，说明中间价格回落超过6%，为避免最大、最下价格之间存在很多波动，放弃之前确定的最高价，继续向左搜索
                                minPrice_high = temp_high
                                minPrice_high_id = -i
                                maxPrice_high_id = -(i + 1)
                                maxPrice_high = df.iloc[ maxPrice_high_id, self.idx_high ]
                            # cnt_d += 1
                        else :
                            pass
                    i += 1
        except Exception as e :
            print ( f' classification cause Error : {e}' )

    def savePicsByClassification(self, classes, picsX, file_name, df, *args, **kwargs) :
        """ what's this

        Args:
            arg:
        Raises:
            error:

        """
        try :
            pic_name = file_name + '_' + str ( picsX )
            portfolio = self.save_path + self.timeStamp + '\\train\\' + classes + '\\'
            self.draw_pics ( df=df, pic_name=pic_name, save_portfolio_abs=portfolio )
        except Exception as e :
            print ( f' savePicsByClassification cause Error : {e}' )



if __name__ == '__main__' :
    # # 通过arg='string'的形式传递字符串，只能显示第一个字符，应将arg=('string',)转化成tuple类型
    # ani = Thread ( target=animation )
    # # 通过setDaemon(true)来设置线程为“守护线程”
    # ani.setDaemon ( True )
    # ani.start ()
    # ani.join ( timeout=0.2 )
    openAnimation(open=True)

    cps = CreatePics (stocks_need=100,w=8,h=5)
    # cps.saveTrainingPics()
    cps.saveNewestPics(offset_days=None)
    # cps.checkFilterPolicy()

    sys.exit ()
