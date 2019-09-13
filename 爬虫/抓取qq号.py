import urllib.request
import re
allHtml = urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml")
# print(allHtml.read().decode("utf-8"))
for x in allHtml:

    '''
    # 千万别忘了加 ？，取消贪婪模式，要不然， 它会尽可能的匹配更多的字符（在满足条件的情况下）
        例如：如果不加？，则会输出QQ:15706903 <br><br>--2--吉祥千禧  回复日期：2003-02-26 22:13:00   <br><br>\u3000\u3000高中，初中美术~<br>\u3000\u30002980530']
        为什么呢？ 原因就是 .* 已经去尽可能的匹配了更多的字符，而该字符串的结尾，恰恰满足]\d{5,11}的条件，
        所以，需要加上 ？ 来取消贪婪模式
    '''
    result = re.findall(r"^qq|QQ.*?\d{5,11}",x.decode("utf-8"))

    if result:
        print(result)

