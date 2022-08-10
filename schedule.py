import os, random
from datetime import datetime, timedelta

if os.system("schtasks /query /tn SecurityScan"):
    os.system("schtasks /delete /f /tn SecurityScan")

print("I am doing malicious things")

filedir = os.path.join(os.getcwd(),"schedule.py")

interval = 1
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s" % (str(dt.hour).zfill(2), str(dt.minute).zfill(2))
d = "%s/%s/%s" % (dt.month, str(dt.day).zfill(2), dt.year)

os.system('schtasks /create /tn /SecurityScan /tr "' + filedir + '" /sc once /st '+t+' /sd '+d)
input()

"""
schtasks /? 

Yukarıkdaki komut ihtiyacın olan ve merak ettiğin her şeyi gösterecek
"""

"""
schtasks /create /tn SecurityScan /sc once /st 10:49 /sd 08/08/2022 /tr C:\Python\infosec_course\schedule.py

yukarıdaki komut her şeyi ayarlamaya yarar. 10:49 yerine istediğin bir saati gir.
"""


"""
schtasks /query /tn SecurityScan

Yukarıdaki komut ne zaman gerçekleşeceğini gösterecek
"""