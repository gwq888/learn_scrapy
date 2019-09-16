import urllib.request


def money_proxy(url):
    proxy = {
        # ps：收费ip代理的话，是有用户名和密码的，反正格式如下，剩下的操作就会免费ip代理是一模一样的了
        "http": "用户名:密码@ip地址:端口号"
    }
    handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(handler)
    result = opener.open(url).read()
    print(result)


# money_proxy("http://www.baidu.com")



def money_proxy2(url):
    # 你去购买收费ip代理的时候， 对方会给你用户名和密码，还有收费ip地址和端口号
    # 私密代理授权的账户
    username = "收费ip代理的 用户名"
    # 私密代理授权的密码
    password = "收费ip代理的 密码"
    # 私密代理 IP
    proxy_ip = "收费的ip地址"

    # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
    user_password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
    user_password_manager.add_password(None, proxy_ip, user=username, passwd=password)

    # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
    #   注意，这里不再使用普通ProxyHandler类了
    handler = urllib.request.ProxyBasicAuthHandler(user_password_manager)

    # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
    opener = urllib.request.build_opener(handler)

    # 5. 使用自定义opener发送请求
    result = opener.open(url).read().decode("utf-8")

    # 6. 打印响应内容
    print(result)

money_proxy2("http://www.baidu.com")





