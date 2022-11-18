import win32api as wp
import pyautogui as pag
import time

import win32con
import win32gui



print(pag.position())
# wp.mouse_event()
# pag.moveTo(x=2490,y=2120, duration=0.25)
pag.click(x=2490,y=2120)

#鼠标移动到x,y坐标点，经历时间为2s
pag.moveTo(x=1800, y=1055, duration=3)
# time.sleep(2)

pag.click()
#键盘输入‘abc’键值，每次输入间隔时间0.25s
pag.write('147853', interval=0.25)
pag.press('enter')
#取屏幕x,y点的RGB颜色值
# print(pag.screenshot().getpixel((2000,2000)))

hwnd = win32gui.WindowFromPoint((1800, 1055))
print(f'{hwnd}, {win32gui.GetWindowText(hwnd)}')
# #当前所有窗口的句柄和句柄名称
# def _hwnd_(hwnd, mouse):
#     try:
#         # win32gui.SetForegroundWindow(str(hwnd))
#         # time.sleep(1)
#         print(f'{hwnd}, {win32gui.GetWindowText(hwnd)}')
#     except Exception as e:
#         print(f'error:{e}')
# win32gui.EnumWindows(_hwnd_, 0)

#显示窗口
win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
# #隐藏窗口，不要轻易隐藏，找不到了
# win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

time.sleep(3)

pag.press('esc')

#去掉打新股的对话框
time.sleep(10)
pag.press('esc')

#点击设置按钮
pag.moveTo(x=3679, y=23, duration=10)
pag.click()
#点击“盘后数据下载”
pag.moveTo(x=3633, y=381, duration=3)
pag.click()
#点击“日线和实时数据”
pag.moveTo(x=1537, y=879, duration=3)
pag.click()
#点击“开始下载”
pag.moveTo(x=2150, y=1332, duration=3)
pag.click()