import robot
import json

f = open('user.json', 'r')
user = json.loads(f.read())

print (user)

robot.connect(user['id'], user['ps'])
content = robot.read() #請按任意鍵繼續
robot.enter()
robot.enter()

content = robot.read()
robot.toBoard('Gossiping')
content = robot.read()  # 請按任意鍵繼續
robot.enter() # 進入文章列表

begin = 156865
end = 156869

while begin <= end:

  robot.toArticle(begin)
  content = robot.read()  # 清除buffer
  robot.enter() # 進入文章

  content = robot.read() # 讀取文章第一頁內容
  robot.getArticleDesc() # 讀取文章資訊
  robot.write(content, "Output" + str(begin) + ".txt")

  i = 1
  j = 23
  while i < robot.arti_desc['pageEnd']:
    com = ":" + str(j)
    robot.command(com)


    i += 1

    if i == robot.arti_desc['pageEnd']:
      content = robot.read()
      robot.getLine()
      shift   = j - robot.arti_desc['lineStart'] + 1
      content = robot.readFromLine(shift)
      robot.write(content, "Output" + str(begin) + ".txt")
      print("lineStart is " + str(robot.arti_desc['lineStart']))
      print("page is " + str(robot.arti_desc['lineStart']))
    else:
      content = robot.read()
      robot.write(content, "Output" + str(begin) + ".txt")
    j += 23

  robot.pressKey(robot.left) # 退出文章
  content = robot.read() # 讀取文章列表
  begin += 1

robot.close()
