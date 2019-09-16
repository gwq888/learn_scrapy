import urllib.request
import urllib.parse
import http.cookiejar
import fake_useragent


def logoin(url):
    # 随机生成User-Agent
    header = {
        "User-Agent": fake_useragent.UserAgent().random
    }
    # 登录药智网的用户名和密码，已经药智网自己设计用来验证的东西：formhash，backurl
    login_data = {
        "username": "鱼儿啊",
        "pwd": "axxcsa",
        "formhash": "1766301C66",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    # post请求也需要将参数给 转成url编码，这个是http规范
    login_data_encode = urllib.parse.urlencode(login_data)
    request = urllib.request.Request(url, data=login_data_encode.encode("utf-8"), headers=header)
    # CookieJar 是用来保存cookie的
    cookjar = http.cookiejar.CookieJar()
    # cookie的handler处理器
    cookie_hanler = urllib.request.HTTPCookieProcessor(cookjar)
    # cookie的opener
    cookie_opener = urllib.request.build_opener(cookie_hanler)
    ############登录药智网，如果登录成功，那么会自动将cookie给保存到内存中############################
    cookie_opener.open(request)


    # 执行到这里的话，说明已经成功登录药智网，并且cookie也已经自动保存好了，然后我们开始 直接登录到个人中心页面里去
    center_url = "https://www.yaozh.com/member/"  # 药智网个人中心页面
    center_request = urllib.request.Request(center_url, headers=header)
    # -----------------------注意：你可能会疑问，为什么这段代码，就没有看见cookie，实际上，我估计cookie是保存到内存中了，
    # -----------------------然后cookie_opener 这个opener，可以取到cookie的，然后open（）发送访问请求的时候，直接将cookie给带上了，当然这个是自动带上的
    response = cookie_opener.open(center_request)
    htmlsource = response.read().decode("utf-8")
    with open("yaozhiwang.html", "w", encoding="utf-8") as f:
        f.write(htmlsource)

logoin("https://www.yaozh.com/login/")







