import win32api
import win32con

key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'SOFTWARE\\Francophonie\\Frhelper\\Customer Info', 0,
                          win32con.KEY_ALL_ACCESS)
win32api.RegSetValueEx(key, 'TimesLeft3', 0, win32con.REG_DWORD, 9999)
