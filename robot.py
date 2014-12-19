import getpass
import sys
import telnetlib
import time
import re

tn = 1  # 連線物件
content = 1 # 全文
arti_desc = {
  'title': 1,
  'author': 1,
  'time': 1,
  'body': 1,
  'lineStart': 1,
  'lineEnd': 22,
  'pageStart': 1,
  'pageEnd': 1
}

top    = b'\x1b[A'
bottom = b'\x1b[B'
left   = b'\x1b[D'
right  = b'\x1b[C'

def connect(id, ps):

  global tn

  tn = telnetlib.Telnet("ptt.cc")
  sleep()

  print ("成功建立連線...")
  login(id, ps)


def login(id, ps):

  print ("[1;31m輸入帳號...[m")
  command(id)

  print ("[1;31m輸入密碼...[m")
  command(ps)

  print ("登入中...")

def close():
  tn.close()
  print ("結束連線...掰掰")

def enter():
  command('')

def sleep():
  time.sleep(1)

def command(com):
  com = (str(com) + '\r\n').encode('big5')
  tn.write(com)
  sleep()

def toBoard(boardName):
  com = 's' + boardName
  command(com)

def toArticle(num):
  command(num)

def read():
  global content
  content = tn.read_very_eager().decode('big5', 'ignore')
  print (content)

  return content

def readFromLine(ind):
  global content
  refresh()
  content = read()
  tmp     = content.split("\n")

  print (content)
  content = ""
  length = len(tmp)

  print ("length is:" + str(length))
  print ("ind is:" + str(ind))
  while ind < length:
    content += tmp[ind]
    ind += 1

  return content


def write(content, title):
  with open(title, "a") as text_file:
    print("{}".format(content), file=text_file)

def getArticleDesc():
  global arti_desc

  pattern = re.compile('作者 \[\d*;\d*m (.* .*\))')
  arti_desc['author'] = pattern.findall(content)[0]
  pattern = re.compile('標題 \[\d*;\d*m (.*)')
  arti_desc['title'] = pattern.findall(content)[0].strip()
  pattern = re.compile('時間 \[\d*;\d*m (.*)\[m')
  arti_desc['time'] = pattern.findall(content)[0].strip()
  pattern = re.compile('瀏覽 第 (\d*)/(\d*)')
  tmp = pattern.findall(content)
  arti_desc['pageStart'] = int(tmp[0][0])
  arti_desc['pageEnd']   = int(tmp[0][1])

def getLine():
  global arti_desc

  pattern = re.compile('[\[24;39H]*\[1;30;47m[目前顯示: 第]*(\d*)~(\d*)')
  tmp = pattern.findall(content)
  arti_desc['lineStart'] = int(tmp[0][0])
  arti_desc['lineEnd']   = int(tmp[0][1])


def refresh():
  content = read()
  com = "\x0c".encode('big5')
  # cannot use command function
  # cause \r\n will lead to move to next line or even next article
  tn.write(com)
  sleep()

def pressKey(com):
  tn.write(com)
  sleep()