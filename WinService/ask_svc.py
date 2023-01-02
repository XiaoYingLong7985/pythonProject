# import win32con,mmap,socketserver,inspectimport datetimeimport win32event,win32timezone,win32service,win32serviceutil,logging,time,os,sys,servicemanager,socket,threading,randomclass Svc(win32serviceutil.ServiceFramework):    _svc_name_ = 'ask'    _svc_display_name_ = 'A ZL Service'    _svc_description_ = 'This is a windows service updating data each trading day!'    _log_name_ = _svc_display_name_ + '.log'    _abs_path_ = 'C:\PycharmProjects\pythonProject\logs'    #1.停止服务，2.手动控制更新股票数据，3.手动控制查找今日推荐股票，4.手动控制新选股策略的分析，5.手动控制选股策略的统计结果，6.以10天周期跟踪选出的股票胜率    def __init__(self, args) :        self._cmd_dict_ = {'stop' : 'stop......', 'update' : 'update....', 'recommend' : 'recommend.',                      'strategy' : 'strategy..', 'statics' : 'statics...', 'observe' : 'observe...',                      'clear' : '..........'}        win32serviceutil.ServiceFramework.__init__ ( self, args )        self.hWaitStop = win32event.CreateEvent ( None, 0, 0, None )        # self.t = 60        self.g = self._get_logger ()        self.s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )        # 监听端口        self.s.bind ( ('127.0.0.1', 9999) )        self.s.listen ( 3 )        self.g.info ( 'Waiting for connection...' )        self.re = self._cmd_dict_[ 'clear' ]        # self._mm_ = mmap.mmap ( -1, 32, access=mmap.ACCESS_WRITE, tagname='ZLS' )        # self.run = True    def SvcStop(self) :        self.g.info ( 'Service is stop...\n' )        self.ReportServiceStatus ( win32service.SERVICE_STOP_PENDING )        # 设置事件        # self._mm_.seek(0)        # self._mm_.write(self._cmd_dict_['stop'].encode())   #.encode()转成byte类型        # self._mm_.close()        win32event.SetEvent ( self.hWaitStop )        self.ReportServiceStatus ( win32service.SERVICE_STOPPED )        # self.run = False    def SvcDoRun(self) :        # 等待服务被停止        self.g.info ( f'Service start up...' )        self.g.info(f'Waiting for MySql 6 s ...')        # while self.t :        #     self.t += -1        # time.sleep(20)        # host, port = "localhost", 9999        # server = socketserver.ThreadingTCPServer ( (host, port), MyTCPHandle )  # 通过多线程实现多个客户端连接，每个客户端连接都是一个线程        # server.serve_forever ()  # 一直运行服务        time.sleep ( 6 )        self.g.info ( f'Import STRUS_RV5c as r5...' )        from mystocks import STRUS_RV5c as r5        #延时6s后启动一个更新数据的线程，在该线程调用的函数结尾，递归调用该函数本身，实现定时循环        threading.Timer(6,function = Rv5,args = (r5, self.g)).start()        # Rv5 ( r5, self.g )        #write command "update" into memory        # self._mm_.seek ( 0 )        # self._mm_.write ( self._cmd_dict_[ 'update' ].encode () )  # .encode()转成byte类型        self.g.info ( f'Waiting for mission command ...' )        # 创建新线程来处理TCP连接：        t = threading.Thread ( target=self._tcp_link )        t.start ()        # t_up = threading.Timer(7200,self._update_tigger_)        # t_up.start()        while (win32event.WaitForSingleObject ( self.hWaitStop, win32event.QS_ALLEVENTS ) != win32event.WAIT_OBJECT_0):            pass            # # # self._mm_.seek ( 0 )            # # # re = self._mm_.read ( 10 ).decode ()  # .decode()将byte类型转成str类型            # # # 接受一个新连接            # # sock, addr = self.s.accept () #默认阻塞进程，每次进入循环后，如果没有建立新连接，将始终阻塞在此处            # # # 创建新线程来处理TCP连接：            # # t = threading.Thread ( target=self._tcp_link,args=(sock,addr) )            # # t.start ()            # #            # # # self.g.info ( f'In the memory of _mm_ is {re} ...' )            # # # win32event.WaitForSingleObject ( self.hWaitStop, win32con.WM_QUERYENDSESSION )            # #            # # # if win32con.WM_QUERYENDSESSION == 17 :            # # #     self.g.info ( f'Receive Windows10 power off command...called by SvcDoRun()' )            # # #     win32event.SetEvent ( self.hWaitStop )            #            # # self.g.info ( f'win32con.WM_QUERYENDSESSION = {win32con.WM_QUERYENDSESSION} [svcRun]' )            # if (win32event.WaitForSingleObject ( self.linked, 2 ) == win32event.WAIT_OBJECT_0):#说明listen监听进程已经退出，此时就重开一个link进程            #     self.g.info(f'New thread to listen TCP link...')            #     t_i = threading.Thread ( target=self._tcp_link )            #     t_i.start ()            # else:            #     pass            #            # # if (win32event.WaitForSingleObject ( self.tigger, 2 ) == win32event.WAIT_OBJECT_0):            # #     self.g.info ( f'New thread to waiting for (7200 + 1000*random())s then update trade data again...' )            # #     t_k = threading.Timer (( 7200 + 1000 * (random.random())),function=self._update_tigger_ )            # #     t_k.start ()            # # else :            # #     pass            # # time.sleep(6)            # # if (win32event.WaitForSingleObject ( self.hWaitStop, win32event.INFINITE ) != win32event.WAIT_OBJECT_0):            # #     break    def _get_logger(self) :        g = logging.getLogger ( '[.ZL Service.]' )        d = os.path.abspath(self._abs_path_)        h = logging.FileHandler ( os.path.join ( d, self._log_name_ ) )        m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )        h.setFormatter ( m )        g.addHandler ( h )        g.setLevel ( logging.INFO )        return g    # def _update_tigger_(self):    #     self.tigger = win32event.CreateEvent(None,0,0,None)    #     from mystocks import STRUS_RV5c as r5    #     Rv5 ( r5, self.g )    #     win32event.SetEvent(self.tigger)    #     self.g.info(f'win32event.tigger has been setted...')    def _tcp_link(self):#,sock,addr        # self.linked = win32event.CreateEvent ( None, 0, 0, None )        # 接受一个新连接        sock, addr = self.s.accept ()  # 默认阻塞进程，每次进入循环后，如果没有建立新连接，将始终阻塞在此处        self.g.info ( f'Accept new connection from {addr}...' )#%s:%s        while True :  # 和每个接入的客户端进行多次数据通信            try:                self.re = sock.recv ( 1024 ).decode('utf-8')  # 接收客户端数据                if not self.re or self.re == 'exit' :  # 如果客户端不发送数据或发送的是exit                    self.g.info ( 'client disconnected!' )                    break                self.g.info ( f'Answer:{self.re}')                sock.send ( self.re.encode ( 'utf-8' ) )  # 发送数据                self.g.info ( 'send finished.' )                if self.re == self._cmd_dict_ ['stop']:                    win32event.SetEvent ( self.hWaitStop )                self._execute_command_()                #如果建立有TCP连接，在这个循环进程中第一时间能收到windows关机的                # if win32con.WM_QUERYENDSESSION == 17:                #     self.g.info(f'Receive Windows10 power off command...called by _tcp_link()')                #     win32event.SetEvent ( self.hWaitStop )                # self.g.info ( f'win32con.WM_ENDSESSION = {win32con.WM_ENDSESSION} [_tcp_link]' )            except ConnectionError as e:                self.g.info('ConnectionError:',e)        sock.close ()        # win32event.SetEvent ( self.linked )        self.g.info ( f'Connection from {addr} closed...' ) #%s:%s % addr        threading.Timer (6, function = self._tcp_link ).start()        self.g.info(f'New threading of timer is setted, after 6s listening TCP link...')    def _execute_command_(self):        from mystocks import STRUS_RV5c as r5        if self.re == self._cmd_dict_[ 'update' ] :            self.g.info ( f'Receive command `update` to download newest trade data...' )            # from mystocks import STRUS_RV5c as r5            t_1 = threading.Thread ( target=Rv5, args=(r5, self.g) )            t_1.start ()            # Rv5 ( r5, self.g )            self.re = self._cmd_dict_[ 'clear' ]            # clear command memory            # self._mm_.seek ( 0 )            # self._mm_.write ( self._cmd_dict_[ 'clear' ].encode () )  # .encode()转成byte类型        if self.re == self._cmd_dict_[ 'recommend' ] :            self.g.info ( f'Receive command `recommend` to get today`s focal point...' )            self.g.info ( f'Import FSS_V6 as f6...' )            from AnalysisFSS import FSS_V6 as f6            t_2 = threading.Thread ( target=f6.Observe ().investment_v6 )            t_2.start ()            # f6.Observe().investment_v6()            self.re = self._cmd_dict_[ 'clear' ]            # clear command memory            # self._mm_.seek ( 0 )            # self._mm_.write ( self._cmd_dict_[ 'clear' ].encode () )  # .encode()转成byte类型        if self.re == self._cmd_dict_[ 'strategy' ] :            self.g.info ( f'Receive command `strategy` to analysis given strategy`s benefits...' )            self.g.info ( f'Import FSS_V6 as f6...' )            from AnalysisFSS import FSS_V6 as f6            table_name = 'count_benefit_statics_V6'            t_3 = threading.Thread ( target=f6.count_benefit_statics_V6, args=(table_name) )            t_3.start ()            # f6.count_benefit_statics_V6(table_name)            self.re = self._cmd_dict_[ 'clear' ]            # clear command memory            # self._mm_.seek ( 0 )            # self._mm_.write ( self._cmd_dict_[ 'clear' ].encode () )  # .encode()转成byte类型        if self.re == self._cmd_dict_[ 'statics' ] :            self.g.info ( f'Receive command `statics` to calculate benefits statics...' )            self.g.info ( f'Import FSS_V6 as f6...' )            from AnalysisFSS import FSS_V6 as f6            t_4 = threading.Thread ( target=f6.Observe ().present_statics_V6 )            t_4.start ()            # f6.Observe ().present_statics_V6()            self.re = self._cmd_dict_[ 'clear' ]            # clear command memory            # self._mm_.seek ( 0 )            # self._mm_.write ( self._cmd_dict_[ 'clear' ].encode () )  # .encode()转成byte类型        if self.re == self._cmd_dict_[ 'observe' ] :            self.re = self._cmd_dict_[ 'clear' ]            pass        if self.re == self._cmd_dict_[ 'stop' ] :            returnclass Rv5():    def __init__(self,args,logger):        self.dbname = 'a_stocks'        self.stocksListTable = 'list_a_stocks'  # 存储深交所和上交所A股列表，并添加相应的字段标识状态        self.holidays = [ '2022-01-03', '2022-01-31', '2022-02-01', '2022-02-02', '2022-02-03', '2022-02-04',                     '2022-04-04', '2022-04-05', '2022-05-02', '2022-05-03', '2022-05-04', '2022-06-03', '2022-09-12',                     '2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07' ]  # 当年的法定假日        self.tableColumns = [ 'date', 'code', 'name', 'endPrice', 'maxPrice', 'minPrice', 'startPrice', 'preEndPrice',                         'diffPrice', 'diffPercent', 'turnoverPercent', 'tradeVolume', 'tradeAmount',                         'totalMarketValue', 'MCAP', 'PE' ]        # 更新数据库中的记录，需要用到conn.commit()，执行后conn只能关闭后再重新开启了        # resetUpdatedFlag ( stocksListTable ) #重置数据库中的标志位        # self.logger.info ( "complete step 1: running into while ...." )        # while self.run :        # open DB        try:            self._update_(args,logger)            i = 1            tint = i * 7200 + random.random() * 1000            nxt = (datetime.datetime.now () + datetime.timedelta ( seconds=tint )).hour            #判断当前时刻 + tint之后的时间是否在0:00-15:00之间，如果在此时间段内，就继续再 +2h，直到下一次启动预计时间在15：00-24：00之间            while nxt < 15:                tint = i * 7200 + random.random() * 1000                nxt = (datetime.datetime.now () + datetime.timedelta ( seconds=tint )).hour            threading.Timer ( tint, function=Rv5, args=(args, logger) ).start ()            logger.info(f'New threading of timer is setted, after {tint} s to update trade data...')        except Exception as e:            logger.info(f'Update Error:{e}')            return    def _update_(self,args,logger):        from itertools import chain        self.start = time.time ()        connection = args.connect_mysql ()        ways: tuple = args.distinguish_update_way_list ( connection, self.stocksListTable, self.holidays, self.tableColumns )        logger.info ( "complete step 1: complete  r5.distinguish_update_way_list...." )        oneday_more_list: list = ways[ 0 ]        oneday_list: list = ways[ 1 ]        nearst_day_str: str = ways[ 2 ]        # 读取数据之前，先去除冗余        # clean redundant rows for every tables        e1 = args.clean_redundant_rows ( connection, self.stocksListTable )        logger.info ( "complete step 2: connect to mysql and clean redundant ...." )        if e1 : logger.info ( f"step 2 ERROR: {e1}" )        if len ( oneday_more_list ) > 10 :#少量的股票需要进行独立的更新时，先不处理，累计到一定数量之后再统一处理            # update_oneday_mare            for slt in oneday_more_list :                upd_tuple = args.update_oneday_more ( slt, self.holidays, nearst_day_str )                upd_list = upd_tuple[ 0 ]                s_table_name = upd_tuple[ 1 ]                logger.info ( f"complete step 3: complete  r5.update_oneday_more....for table: {s_table_name}" )                e2 = args.add_record ( connection, upd_list, s_table_name, self.tableColumns )                if e2 : logger.info ( f"step 4: call  r5.add_record....\n ERROR: {e2}" )                # e3 = RSD.reflash_stocks_list_table ( connection, s_table_name, stocksListTable )                # if e3:self.logger.info (                #     f"step 5: call  RSD.reflash_stocks_list_table....\n ERROR: {e3}" )                # self.logger.info ( f"complete step 3: complete  RSD.update_oneday_more...." )                # self.logger.info ( f"complete step 4: complete  RSD.add_record...." )                # self.logger.info ( f"complete step 5: complete  RSD.reflash_stocks_list_table....{stocksListTable}\n Exception e = {e}" )        if len ( oneday_list ) > 0 :            e3 = args.update_oneday ( connection, oneday_list, self.tableColumns, self.stocksListTable, self.holidays )            logger.info ( f"complete step 5: r5.update_oneday...." )            if e3 : logger.info ( f"step 5...... ERROR: {e3}" )        logger.info ( ">>> 数据库中的股票交易数据已经更新到最新状态 ！\n" )        # # clean redundant rows for every tables        # e4 = args.clean_redundant_rows ( connection, self.stocksListTable )        # logger.info ( f'清除冗余数据......' )        # if e4 : logger.info ( f'clean redundant...... ERROR：{e4}' )        # 更新list_a_stocks列表        cmd = "SELECT `tablename` FROM " + self.stocksListTable + " WHERE `delisted` NOT LIKE '1'"        cursor = connection.cursor ()        cursor.execute ( cmd )        stable_list = list ( chain.from_iterable ( cursor.fetchall () ) )        for s_table_name in stable_list :            e5 = args.reflash_stocks_list_table ( connection, s_table_name, self.stocksListTable )            if e5 : logger.info (                f"step 6: call  r5.reflash_stocks_list_table...... ERROR: {s_table_name}->>>{e5}" )        # # 放量锤头形态的捕获功能        # hammer_list = args.find_hammer_head_line ( connection, self.stocksListTable )        # logger.info ( f'近期出现放量锤头的股票共{len ( hammer_list )}只请关注：\n {hammer_list} ！' )        # close DB        connection.close ()        # 服务启动之后，执行一次更新，之后等待6个小时        # self.logger.info ( "complete step ?: waiting for 6 hours ...." )        self.end = time.time ()        logger.info ( f"update data commission completed....Used {round ( self.end - self.start, 3 )}s \n" )        # win32event.WaitForSingleObject ( self.hWaitStop, win32event.INFINITE )  # 等待服务被停止        # win32event.WaitForSingleObject ( self.hWaitStop, win32event.QS_ALLEVENTS )  # 等待服务被停止        # time.sleep ( 3600 * 6 )if __name__ == '__main__':    if len ( sys.argv ) == 1 :        try :            evtsrc_dll = os.path.abspath ( servicemanager.__file__ )            servicemanager.PrepareToHostSingle ( Svc )  # 如果修改过名字，名字要统一            servicemanager.Initialize ( 'Svc', evtsrc_dll )  # 如果修改过名字，名字要统一            servicemanager.StartServiceCtrlDispatcher ()        except win32service.error as details :            import winerror            if details == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT :                win32serviceutil.usage ()    else :        win32serviceutil.HandleCommandLine ( Svc )  # 如果修改过名字，名字要统一# 理想的状态，在UI界面上可以描述、添加策略，及策略的组合，然后由服务进程完成该策略的价值分析，根据被选中的策略，推荐观察股票，并在未来的10天内跟踪观察，形成观察统计报告# 代码自动补全提示的类别：P-parameter;m-method;c-class;v-variable;f-function