import urllib
import urllib.request
import re


# 抓取邮箱
allHtml = urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml")
for x in allHtml:
   result = re.findall("\w{6,10}@\w{2,5}\.\w{3,5}",x.decode("utf-8"))
   if result:
     print(result)

#
# 指的是必须要出现 _ 下划线，但是%由于 + ，至少需要出现一个%号，或者出现更多的%，但是不能没有%，否则匹配错误
#  - 指的是必须也出现一个 - 否则匹配错误
print(re.match("(_%+-)","_%-"))
# 点 下划线，百分号，加号， 减号 任意出现一个就行
print(re.match("[._%+-]","."))
#
