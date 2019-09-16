import requests


'''
    requests库，会自动将参数进行 urlencoded的，不需要我们手动去转， 直接写中文即可
'''
# 这里的参数，可以直接写中文，不需要urlencoded，因为requests库内部在发送请求的时候，会自动urlencoded
# url = "http://www.baidu.com/s?wd=马刺"

url = "http://www.baidu.com/s"
data = {
    # 直接写中文
    "wd": "张三"
}
# params：用来加get请求的参数
res = requests.get(url, params=data).content.decode("utf-8")



with open("maci.html","w", encoding="utf-8") as f:
    f.write(res)


