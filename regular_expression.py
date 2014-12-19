import re

file = open('Output.txt', encoding='utf-8')
content = file.read()


# pattern = re.compile('[\[24;39H]*\[1;30;47m[目前顯示: 第]*(\d*)~(\d*)')
# pattern = re.compile('瀏覽 第 (\d*)/(\d*)')


#content = pattern.findall(content)
content = content.split("\n")

# for i in content:
#   print (i)
# print (content)
# content[0] = content[0].strip()
# print (content[23][47])
# print (len(content))
# print (content.encode('big5'))



# with open("after_re1.txt", "w") as text_file:
#   print("{}".format(content), file=text_file)

