import requests

url = "http://www.baidu.com"
response = requests.get(url)
'''
    content和text，2个都是返回网页上的内容
    但是content返回的是字节bytes，所以需要decode解码一下
    而text直接返回字符串，它并不需要decode，它完全是靠猜测的，所以中文下，出现乱码的概率很大
'''
content = response.content.decode("utf-8") # 获取网页上的内容
content = response.text
print(content)
