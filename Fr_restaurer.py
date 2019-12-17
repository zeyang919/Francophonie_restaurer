import os
import socket
import win32api
import win32con

# 获取当前主机名
hostname = socket.gethostname()
# 获取存储时间的文件
file = 'C:/Users/' + hostname + '/AppData/Roaming/Francochinois/Frhelper/study.db'
# 判断如果文件存在则删除
if os.path.exists(file):
    os.remove(file)
# 存储注册表地址
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'SOFTWARE\\Francophonie\\Frhelper\\Customer Info', 0,
                          win32con.KEY_ALL_ACCESS)
# 修改注册表地址
win32api.RegSetValueEx(key, 'TimesLeft3', 0, win32con.REG_DWORD, 9999)
