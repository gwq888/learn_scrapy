import urllib
import urllib.request

# read()是一次性读取全部内容
a  = urllib.request.urlopen("http://www.baidu.com").read()
# a会是以  b“百度网页里的内容”， 以b开头的说明是 字节，我们需要进行解码成utf-8
print(a.decode("utf-8"))


print("--"*100)
b = urllib.request.urlopen("http://www.baidu.com")
for x in b:
    print(x.decode("utf-8"))
