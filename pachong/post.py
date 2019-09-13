import urllib
import urllib.request
import urllib.parse

# 可以提交表单数据的网页
url = "https://umbra.nascom.nasa.gov/cgi-bin/eit-catalog.cgi"
data = {"name":"zhangsan",'age':12}
dataByUrlEncod = urllib.parse.urlencode(data)
# Request()中，第二个参数默认就是传递 数据的（post请求）
request = urllib.request.Request(url, dataByUrlEncod.encode("gb2312"))
res = urllib.request.urlopen(request).read().decode("utf-8")
print(res)


