import requests
import fake_useragent

url = "https://www.yaozh.com/login"
# 这个session，就好比我们之前urllib库里的 cookieJar， 它也是用来自动保存cookie的，只要有cookie，那么它会自动保存
session = requests.session()
headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
# 登陆所需要的参数,不需要手动urlencoded了，requests会自动转
data = {
    "username": "鱼儿啊",
    "pwd": "axxcsa",
    "formhash": "076CEFB2BD",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}
# 如果登陆成功，那么 cookie会自动被保存
response = session.post(url, headers=headers, data=data)

# 如果此时登陆成功，那么就会有cookie了， 然后，我们直接去访问药智网的个人中心
url = "https://www.yaozh.com/member"
# 去访问的时候，session会自动带着cookie，不需要我们手动添加了
res= session.get(url,headers=headers).content.decode("utf-8") # get请求即可，因为药智网的个人中心页面是get请求

with open("member.html", "w", encoding="utf-8") as f:
    f.write(res)







