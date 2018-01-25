# coding: utf-8
from ftplib import FTP
import time
import tarfile
import os

# !/usr/bin/python
# -*- coding: utf-8 -*-

from ftplib import FTP

def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    #ftp.set_debuglevel(0)
    #fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("192.168.2.22", "gz", "8899")
    #data = ftp.
    #ftp.close()
        # Prints out the directories and files, line by line
    #for i in data:
    #    print i
    #ftp.cwd('ThisMain')
    downloadfile(ftp, "ThisMain.dll", "E:\\ThisEye2012copy\\ThisMain.dll")
    downloadfile(ftp, "ThisMain.exe", "E:\\ThisEye2012copy\\ThisMain.exe")
    #调用本地播放器播放下载的视频


    ftp.quit()