import requests
import fake_useragent

class MySpider():
    def __init__(self, url):
        ua = fake_useragent.UserAgent().random
        header = {"User-Agent": ua}
        self.response = requests.get(url, headers=header)

    def run(self):
        # 请求头的一些方法  获取请求头：  response.request
        print(self.response.request.headers) # 请求头
        '''
            1.低版本的requests库里，找请求头的cookie，属性是cookies,没有下划线的，我们的是高版本的requests库，所以需要加下划线
            2.经过打印发现：[<Cookie BAIDUID=1F51D9FFA63723F7028DFAC7107E706C:FG=1 for .baidu.com/>等一些cookie
                实际上这些cookie，是浏览器在访问百度的时候生成的，并不是百度的服务器生成的，所以这个cookie没用
            
        '''
        print(self.response.request._cookies) # 请求头的cookie

        # 响应头的一些方法
        print(self.response.status_code) # 状态码
        print(self.response.cookies) # 响应头的cookie


my = MySpider("http://www.baidu.com")
my.run()
