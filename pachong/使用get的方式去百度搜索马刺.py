import  urllib.request
import urllib.parse
# wd=”马刺“  wd是百度搜索内容时候的key
searchStr = {"wd": "马刺"}
# 进行url编码
searchStrByUrlEncode = urllib.parse.urlencode(searchStr)
# print(searchStrByUrlEncode)  # wd=%E9%A9%AC%E5%88%BA
# 拼接来就是: http://www.baidu.com\s?wd="%E9%A9%AC%E5%88%BA"   我们要在百度搜索‘马刺‘
searchUrl = urllib.request.Request("http://www.baidu.com/s?"+searchStrByUrlEncode)
htmlSource = urllib.request.urlopen(searchUrl).read().decode("utf-8")
print(htmlSource)





