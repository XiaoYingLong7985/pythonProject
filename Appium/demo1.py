import logging
import time
import os

import win32event
import win32process
from appium import webdriver
from selenium.webdriver.common.by import By
# from appium.webdriver.extensions.android.nativekey import AndroidKey
import subprocess as sp
import re

class AutoOpt:
    def __init__(self):
        self.mTime = "2022-12-13"
        self.isFirstOpen = False
        self._abs_path_ = 'C:\PycharmProjects\pythonProject\logs'
        self._log_name_ = 'Appium.log'
        self.g = self._get_logger()

    def _get_logger(self) :
        g = logging.getLogger ( '[.ZL Appium.]' )
        d = os.path.abspath(self._abs_path_)
        h = logging.FileHandler ( os.path.join ( d, self._log_name_ ) )

        m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )
        h.setFormatter ( m )

        g.addHandler ( h )
        g.setLevel ( logging.INFO )
        return g

    def _running_(self):
        self._connect_()
        # 延时10s等待app启动并进入初始化页面
        time.sleep ( 10 )
        self._logIn_ ()

        self._sell_()

        input ( '**** Press to quit..' )
        self.driver.quit ()


    def _connect_(self):
        desired_caps = {
            'platformName' : 'Android',  # 被测手机是安卓
            'platformVersion' : '8',  # 手机安卓版本
            'deviceName' : 'PD1818B',  # 设备名，安卓手机可以随意填写
            'appPackage' : 'com.plat.swhydyj.android.ShenWanHongYuanSecurity',
            # 启动APP Package名称 com.plat.swhydyj.android.ShenWanHongYuanSecurity/com.hexin.plat.android.AndroidLogoActivity
            'appActivity' : 'com.hexin.plat.android.AndroidLogoActivity',  # 启动Activity名称
            'skipServerInstallation' : True,
            'unicodeKeyboard' : True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard' : True,  # 执行完程序恢复原来输入法
            'noReset' : True,  # 不要重置App
            'newCommandTimeout' : 6000,
            'automationName' : 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
            }

        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote ( 'http://localhost:4723/wd/hub', desired_caps )
        # 设置缺省等待时间
        self.driver.implicitly_wait ( 2 )
        self.gst = SlideGestures ( self.driver )

    def findElementByID(self, id_values):
        try:
            return self.driver.find_element(By.ID, id_values)
        except Exception as e:
            self.g.info("执行 find_element(By.ID, 'id names') 方法")
            self.g.info(f'查找{id_values}失败, Error:{e}')
            return False

    def findElementByXpath(self, xPath):
        try:
            return self.driver.find_element(By.XPATH, xPath)
            # # 中文字符“交易”前有空格，另外，即使该控件属性clickable=false,仍然可以使用.click()方法触发
            # self.driver.find_element_by_xpath ( '//*[@class="android.widget.TextView" and @text=" 交易"]' )
        except Exception as e:
            self.g.info("执行 find_element(By.XPATH, 'xPath names') 方法")
            self.g.info(f'查找{xPath}失败, Error:{e}')
            return False

    def idFindAndSend(self, id_values, skeys):
        # 根据id定位元素
        elt =  self.findElementByID(id_values )
        if elt :
            elt.send_keys ( skeys )
        else :
            print ( f"{id_values} not exit!" )

    def idFindAndClick(self, id_values):
        # 根据id定位元素
        elt = self.findElementByID ( id_values )
        if elt :
            elt.click ()
        else :
            print ( f"{id_values} not exit!" )

    def pathFindAndClick(self, xPath):
        # 根据id定位元素
        elt = self.findElementByXpath ( xPath )
        if elt :
            elt.click ()
        else :
            print ( f"{xPath} not exit!" )

    def _filter_(self):
        #点击放大镜图标，进入搜索界面
        self.idFindAndClick(id_values='new_title_search')
        # 输入搜索的代码
        code = '600850'
        self.idFindAndSend(id_values='et_stock_search', skeys=code)

        time.sleep(2)
        self.gst.right_to_left()


    def _sell_(self):
        # 点击“持仓”按钮
        self.pathFindAndClick ( xPath='//*[@class="android.widget.TextView" and @text="卖出"]' )
        #自底向上滑动，确保所有数据都被载入
        self.gst.down_to_top ()
        #按盈亏比例查询
        eles = self.driver.find_elements ( By.ID, 'itemListYingKuiBi' )

        for ele in eles :
            # 如果收益大于3%
            if float ( (ele.text)[ :-1 ] ) > 3.0 :
                #点击一下
                ele.click ()
                # ele_temp = self.driver.find_element ( By.ID, 'llCCFunctionMC' )
                # if ele_temp :
                #     ele_temp.click ()
                # else :
                #     ele.click ()
                #     self.driver.find_element ( By.ID, 'llCCFunctionMC' ).click ()

                # driver.find_element ( By.ID, 'half_chicang' ).click () #[all_chicang,half_chicang,one_third_chicang,one_four_chicang]
                # self.driver.find_element ( By.ID, 'btn_transaction' ).click ()
                self.idFindAndClick ( id_values='half_chicang' )
                self.idFindAndClick ( id_values='btn_transaction' )

                # 确认卖出
                self.idFindAndClick ( id_values='tv_dialog_ok' )
                # 提交委托后，弹出的系统信息对话框
                self.idFindAndClick ( id_values='tv_dialog_ok' )
                # 取消
                # self.idFindAndClick(id_values='tv_dialog_cancel')

                # 返回
                # self.driver.back()

                # 回到持仓界面
                # self.pathFindAndClick ( xPath='//*[@class="android.widget.TextView" and @text="持仓"]' )

                print ( ele.text, "+++" )
            else :
                print ( ele.text, ':', float ( (ele.text)[ :-1 ] ) )

        # 返回，系统的返回导航键，回到 普通交易界面
        self.driver.back()


    def _logIn_(self):
        try:
            if self.isFirstOpen:
                # 根据id定位手机号码输入框，输入电话号码
                self.idFindAndSend(id_values='etPhoneLoginPhone', skeys='18642049801')
                # 根据id定位手机注册按钮，点击
                self.idFindAndClick(id_values='tvPhoneLoginGetCode')
                # 不要删除以下两行，也许有用
                # sbox = self.driver.find_element ( By.ID, 'etPhoneLoginPhone' )
                # sbox.send_keys ( '18642049801' )
            else:
                # driver.tap([(500,1400)],100)
                #中文字符“交易”前有空格，另外，即使该控件属性clickable=false,仍然可以使用.click()方法触发
                # self.driver.find_element_by_xpath ( '//*[@class="android.widget.TextView" and @text=" 交易"]' ).click()
                self.pathFindAndClick(xPath='//*[@class="android.widget.TextView" and @text=" 交易"]')

                # 点击登录按钮
                # self.driver.find_element ( By.ID, 'loginButton' ).click ()
                self.idFindAndClick(id_values='loginButton')

                s = str ( int ( "".join ( re.findall ( "\d+", self.mTime ) )[ 2 : ] ) - 73360 )
                # self.driver.find_element ( By.ID, 'weituo_edit_trade_password' ).send_keys ( s )
                self.idFindAndSend(id_values='weituo_edit_trade_password', skeys=s)

                #获得随机数字验证码，在验证栏中填写该验证码
                numbs = self.driver.find_element ( By.ID, 'wt_text_authenticode' ).text
                # self.driver.find_element ( By.ID, 'weituo_edit_authenticode' ).send_keys ( numbs )
                self.idFindAndSend(id_values='weituo_edit_authenticode', skeys=numbs)

                #点击“立即登录”按钮
                # self.driver.find_element ( By.ID, 'weituo_btn_login' ).click ()
                self.idFindAndClick(id_values='weituo_btn_login')

                #进入普通交易界面

                # #点击“持仓”按钮
                # # self.driver.find_element_by_xpath ( '//*[@class="android.widget.TextView" and @text="持仓"]' ).click()
                # self.pathFindAndClick(xPath='//*[@class="android.widget.TextView" and @text="持仓"]')


                # driver.swipe(200,1000,200,300,10)
                # time.sleep(3)

                # handles = driver.window_handles
                # cur_handle = driver.current_window_handle
                # for h in handles :
                #     driver.switch_to.window ( h )

                # 卖出


        except Exception as e:
            #打开cmd，执行一次 adb reconnect 命令，重新连接一次手机

            sp.Popen ( "adb reconnect", shell=True, stdout=None, stderr=None ).wait ()
            time.sleep(5)

            #回调函数，重新执行一次
            self._connect_()
            print(f'Error:{e}')


class SlideGestures:
    def __init__(self, driver):
        self.drv = driver
        self.w = self.drv.get_window_size()['width']
        self.h = self.drv.get_window_size()['height']
        self.top = Points(int(self.w * 0.5), int(self.h * 0.1))
        self.down = Points(int(self.w * 0.5), int(self.h * 0.9))
        self.left = Points(int(self.w * 0.1), int(self.h * 0.5))
        self.right = Points(int(self.w * 0.9), int(self.h * 0.5))
        self.duration = 1000

    def right_to_left(self):
        self.drv.swipe(self.right.x, self.right.y, self.right.x, self.right.y, self.duration)

    def left_to_right(self):
        self.drv.swipe(self.left.x, self.left.y, self.right.x, self.right.y, self.duration)

    def top_to_down(self):
        self.drv.swipe(self.top.x, self.top.y, self.down.x, self.down.y, self.duration)

    def down_to_top(self):
        self.drv.swipe(self.down.x, self.down.y, self.top.x, self.top.y, self.duration)

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class OpenApplication:
    def __init__(self, aPath):
        self.AppPath = aPath
        self.__run__()

    def __run__(self):
        handle = win32process.CreateProcess(
            None,
            self.AppPath,
            None,
            None,
            0,
            win32process.CREATE_NO_WINDOW,
            None,
            None,
            win32process.STARTUPINFO()
            )
        rc = win32event.WaitForSingleObject(handle[0], 15 * 1000)
        return rc

if __name__ == '__main__' :
    # OpenApplication("C:/androidsdk/tools/bin/uiautomatorviewer.bat")
    # OpenApplication("C:/Program Files/Appium/Appium.exe")
    # os.system("C:/androidsdk/tools/bin/uiautomatorviewer.bat")
    # os.system("C:/Program Files/Appium/Appium.exe")
    # sp.Popen ( "C:/androidsdk/tools/bin/uiautomatorviewer.bat", shell=True, stdout=None, stderr=None )
    # sp.Popen( "C:/Program Files/Appium/Appium.exe", shell=True, stdout=None, stderr=None )
    AutoOpt()
#


# from appium import webdriver
# from selenium.webdriver.common.by import By
# from appium.webdriver.extensions.android.nativekey import AndroidKey
#
# desired_caps = {
#     'platformName': 'Android', # 被测手机是安卓
#     'platformVersion': '8', # 手机安卓版本
#     'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
#     'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
#     'appActivity': '.MainActivityV2', # 启动Activity名称.ui.splash.SplashActivity
#     'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
#     'resetKeyboard': True, # 执行完程序恢复原来输入法
#     'noReset': True,       # 不要重置App
#     'newCommandTimeout': 6000,
#     'automationName' : 'UiAutomator2',
#     'skipServerInstallation': True #避免重复安装 io.appium.uiautomator2.server 和 io.appium.uiautomator2.server.test
#     # 'app': r'd:\apk\bili.apk',
# }
#
# # 连接Appium Server，初始化自动化环境
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# # 设置缺省等待时间
# driver.implicitly_wait(5)
#
# # 如果有`青少年保护`界面，点击`我知道了`
# iknow = driver.find_elements(By.ID, "text3")
# if iknow:
#     iknow.click()
#
# # 根据id定位搜索位置框，点击
# driver.find_element(By.ID, 'expand_search').click()
#
# # 根据id定位搜索输入框，点击
# sbox = driver.find_element(By.ID, 'search_src_text')
# sbox.send_keys('白月黑羽')
# # 输入回车键，确定搜索
# driver.press_keycode(AndroidKey.ENTER)
#
# # 选择（定位）所有视频标题
# eles = driver.find_elements(By.ID, 'title')
#
# for ele in eles:
#     # 打印标题
#     print(ele.text)
#
# input('**** Press to quit..')
# driver.quit()