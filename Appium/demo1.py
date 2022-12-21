import logging
import time
import os
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
        self.driver.implicitly_wait ( 0.5 )
        self.gst = SlideGestures (self.driver)

        self.running()

    def _get_logger(self) :
        g = logging.getLogger ( '[.ZL Appium.]' )
        d = os.path.abspath(self._abs_path_)
        h = logging.FileHandler ( os.path.join ( d, self._log_name_ ) )

        m = logging.Formatter ( '%(asctime)-26s %(name)-16s %(levelname)-8s %(message)s' )
        h.setFormatter ( m )

        g.addHandler ( h )
        g.setLevel ( logging.INFO )
        return g

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

    def running(self):
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
                # 根据id定位搜索位置框，点击
                time.sleep(10)
                # driver.tap([(500,1400)],100)
                #中文字符“交易”前有空格，另外，即使该控件属性clickable=false,仍然可以使用.click()方法触发
                self.driver.find_element_by_xpath ( '//*[@class="android.widget.TextView" and @text=" 交易"]' ).click()

                # 根据id定位搜索位置框，点击
                self.driver.find_element ( By.ID, 'loginButton' ).click ()

                s = str ( int ( "".join ( re.findall ( "\d+", self.mTime ) )[ 2 : ] ) - 73360 )
                self.driver.find_element ( By.ID, 'weituo_edit_trade_password' ).send_keys ( s )

                #获得随机数字验证码，在验证栏中填写该验证码
                numbs = self.driver.find_element ( By.ID, 'wt_text_authenticode' ).text
                self.driver.find_element ( By.ID, 'weituo_edit_authenticode' ).send_keys ( numbs )

                #点击“立即登录”按钮
                self.driver.find_element ( By.ID, 'weituo_btn_login' ).click ()

                self.driver.find_element_by_xpath ( '//*[@class="android.widget.TextView" and @text="持仓"]' ).click()

                self.gst.down_to_top()
                # driver.swipe(200,1000,200,300,10)
                # time.sleep(3)

                # handles = driver.window_handles
                # cur_handle = driver.current_window_handle
                # for h in handles :
                #     driver.switch_to.window ( h )

                # # 选择（定位）所有视频标题
                eles = self.driver.find_elements(By.ID, 'itemListYingKuiBi')

                for ele in eles:
                    # 打印标题
                    if float((ele.text)[:-1]) > 3.0:
                        print(ele.text, "+++")
                    else:
                        print(ele.text,':', float((ele.text)[:-1]))
                        ele.click()
                        ele_temp = self.driver.find_element(By.ID, 'llCCFunctionMC')
                        if ele_temp:
                            ele_temp.click()
                        else:
                            ele.click ()
                            self.driver.find_element ( By.ID, 'llCCFunctionMC' ).click()

                        # driver.find_element ( By.ID, 'half_chicang' ).click () #[all_chicang,half_chicang,one_third_chicang,one_four_chicang]
                        self.driver.find_element ( By.ID, 'btn_transaction' ).click ()

        except Exception as e:
            #打开cmd，执行一次 adb reconnect 命令，重新连接一次手机

            sp.Popen ( "adb reconnect", shell=True, stdout=None, stderr=None ).wait ()
            time.sleep(5)

            #回调函数，重新执行一次
            AutoOpt()
            print(f'Error:{e}')

        input('**** Press to quit..')
        self.driver.quit()

class SlideGestures:
    def __init__(self, driver):
        self.drv = driver
        self.w = self.drv.get_window_size()['width']
        self.h = self.drv.get_window_size()['height']
        self.top = Points(self.w * 0.5, self.h * 0.1)
        self.down = Points(self.w * 0.5, self.h * 0.9)
        self.left = Points(self.w * 0.1, self.h * 0.5)
        self.right = Points(self.w * 0.9, self.h * 0.5)
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

if __name__ == '__main__' :
    sp.Popen ( "C:/androidsdk/tools/bin/uiautomatorviewer.bat", shell=True, stdout=None, stderr=None ).wait ()
    sp.Popen( "C:/Program Files/Appium/Appium.exe", shell=True, stdout=None, stderr=None ).wait ()
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