import os
import win32api
import win32con

try:
    # 获取APPDATA地址
    key_appdata = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Volatile Environment', 0, win32con.KEY_READ)
    path_appdata = win32api.RegQueryValueEx(key_appdata, "APPDATA")[0]
    # 获取存储时间的文件
    file = path_appdata + '\Francochinois\Frhelper\study.db'
    # 判断如果文件存在则删除
    if os.path.exists(file):
        os.remove(file)
except:
    pass
# 存储注册表地址
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'SOFTWARE\\Francophonie\\Frhelper\\Customer Info', 0,
                          win32con.KEY_ALL_ACCESS)
# 修改注册表地址
win32api.RegSetValueEx(key, 'TimesLeft3', 0, win32con.REG_DWORD, 9999)
