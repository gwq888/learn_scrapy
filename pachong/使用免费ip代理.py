import urllib
import urllib.request


# 使用ip代理来访问 百度
def create_free_proxy(url):

    # 这个是网上找到的免费代理
    proxy = {"http": "http://120.83.120.68:9999"}
    '''
        # 如果有多个ip代理：
        proxy = [
                {"http":"ip"},{"http":"ip"},{"http":"ip"},
        ]
            
    '''


    # 代理服务器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    html_source = opener.open(url).read().decode("utf-8")
    print(html_source)

# csdn 可以通过免费ip代理来访问， 百度就不行
create_free_proxy("https://blog.csdn.net/dengachao/article/details/97923053")
