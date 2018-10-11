
from ftplib import FTP


user = "victime"
pwd = "LaChancla!"
host = '127.0.0.1'
ftp = FTP(host)
ftp.login(user, pwd)
