import urllib
import urllib.request
url = "http://www.baidu.com"
header = {"user-agent":"Mozilla/5.0 (Android 9.0; Mobile; rv:63.0) Gecko/63.0 Firefox/63.0"}
request = urllib.request.Request(url,headers=header)
print(request.get_method())  #  GET 请求的方式，是get还是post
print(request.get_full_url()) # http://www.baidu.com 网页的整个链接
print(request.host) # www.baidu.com 该网站的域名或者主机
print(request.type) # http 网页的类型，有http https ftp


urllib.request.quote()
response = urllib.request.urlopen(request)
print(response.getcode()) # 200 响应码
print(response.info()) # 网页的 header信息
print(response.read().decode("utf-8")) # 网页的整个源代码

