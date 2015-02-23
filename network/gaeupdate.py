#!/usr/bin/env python
# coding:utf-8
'''
Created on Feb 22, 2015

@author: wangcl
'''
import sys
import os
import socket
import requests

def println(s, file=sys.stderr):
    assert type(s) is type(u'')
    file.write(s.encode(sys.getfilesystemencoding(), 'replace') + os.linesep)

try:
    socket.create_connection(('127.0.0.1', 8087), timeout=1).close()
    os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8087'
except socket.error:
    println(u'警告：建议先启动 goagent 客户端或者 VPN 然后再上传，如果您的 VPN 已经打开的话，请按回车键继续。')
    raw_input()
    
    
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer
from StringIO import StringIO

downloadURL = "https://nodeload.github.com/goagent/goagent/legacy.zip/3.0"
location = "/wangcl/soft"
chunk_size = 1024 * 1024 / 2

response = requests.get(downloadURL, stream=True)
total_length = int(response.headers.get('content-length'))

widgets = ['goagent: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=total_length).start()

zipdata = StringIO()
dl = 0
total_length = int(total_length)
for data in response.iter_content(chunk_size=chunk_size):
    dl += len(data)
    zipdata.write(data)
    pbar.update(dl)
    
# extract file
import zipfile

myzipfile = zipfile.ZipFile(zipdata)
topdirectory = myzipfile.namelist()[0]
myzipfile.extractall(location)

# move
import shutil
from distutils import dir_util
dir_util.copy_tree(os.path.join(location, topdirectory), os.path.join(location, "goagent"))

# remove
shutil.rmtree(os.path.join(location, topdirectory))
print "完成"


