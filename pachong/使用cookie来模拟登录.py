import urllib.request
import fake_useragent

'''
    cookie:我们都知道，现在的网站，当你第一次登录该网站的时候（注册了该网站的账号），
            网站都会将你的账号信息，保存到浏览器的cookie当中（这个其实是持久化到我们的电脑上的，硬盘上是可以看到这个cookie数据的）
    需求：
        现在，我们希望，在chrome浏览器登陆某个网站之后，  再直接使用python去访问这个网站（之前的cookie保存在chrome里，python
        程序肯定是没有的，所以，这里，我们去chrome浏览器里直接 复制cookie，粘贴到python程序中，以达到模拟登陆的需求
    
'''
def fun(url):
    header = {
        "User-Agent": fake_useragent.UserAgent().random,
        # 这个cookie，是我们先随便找了个浏览器去登录了药智网，之后，f12，拿到请求头里的 Cookie，复制到这里来，开始模拟登录药智网
        "Cookie": 'acw_tc=707c9fd715683765331873126e2367cd696812f78e223fd81f710c331a46d8; PHPSESSID=i4shm4j5pbek4agh00emmm97v5; _ga=GA1.2.1362096075.1568376534; _gid=GA1.2.1180976130.1568376534; _gat=1; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1568376534; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1568376537; yaozh_logintime=1568376582; yaozh_user=813035%09%E9%B1%BC%E5%84%BF%E5%95%8A; yaozh_userId=813035; db_w_auth=712360%09%E9%B1%BC%E5%84%BF%E5%95%8A; UtzD_f52b_saltkey=TIG0fqq8; UtzD_f52b_lastvisit=1568372982; UtzD_f52b_lastact=1568376582%09uc.php%09; UtzD_f52b_auth=c722oRD4YgVAG0KE9LApq7iStpiTEyShhLCHQhJNonKcgY8yFeLRREm7j%2FPQkuY4W4LzyU2GP3IL1ON6Smk1pmlkbuA; yaozh_uidhas=1; yaozh_mylogin=1568376584; acw_tc=707c9fd715683765331873126e2367cd696812f78e223fd81f710c331a46d8'
    }

    request = urllib.request.Request(url, headers = header)
    response = urllib.request.urlopen(request)
    print(response.read().decode("utf-8"))
# 使用cookie来登录药智网
fun("https://www.yaozh.com/member/")

