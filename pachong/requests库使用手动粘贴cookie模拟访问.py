import requests
import fake_useragent
url = "http://www.yaozh.com/member/"

'''
# request库中，对 cookie的要求是dict字典，而不是字符串
    也就是要这样：    {
                        acw_tc:acw_tc=2f624a5d15683855598571166e1c8ef2893eea996c0d50d655ad26580a8d2e,
                        ga:GA1.2.1270812048.1568385560
                        .......
                    }
    所以，我们需要对cookie_str进行拆分成字典的样子
                    
'''
cookies_str = "acw_tc=2f624a5d15683855598571166e1c8ef2893eea996c0d50d655ad26580a8d2e; _ga=GA1.2.1270812048.1568385560; PHPSESSID=q5fck3d22g2723oa7e1johjgc7; _gid=GA1.2.574397917.1568518940; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1568518942; yaozh_logintime=1568518954; yaozh_user=813035%09%E9%B1%BC%E5%84%BF%E5%95%8A; yaozh_userId=813035; db_w_auth=712360%09%E9%B1%BC%E5%84%BF%E5%95%8A; UtzD_f52b_saltkey=fqBS90zI; UtzD_f52b_lastvisit=1568515354; UtzD_f52b_lastact=1568518954%09uc.php%09; UtzD_f52b_auth=721akoEc6ki1%2Fa0HDbNguKPhaRScJh9dJHSsB8DHkTgvpVcxoyVy8G80q7JdTJWuCyxd%2FCAQTB%2FA6C5Uh95%2FTZb6uLk; yaozh_uidhas=1; yaozh_mylogin=1568518956; acw_tc=2f624a5d15683855598571166e1c8ef2893eea996c0d50d655ad26580a8d2e; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1568376534%2C1568385561%2C1568518940"

# 使用字典推导式来完成
cookies_dict = {str.split("=")[0]: str.split("=")[1] for str in cookies_str.split("; ")}

# 或者不字典推导式，使用for循环的方式也可以
cookie_dict2 = {}
for str in cookies_str.split("; "):
    cookie_dict2[str.split("=")[0]] = str.split("=")[1]
print(cookie_dict2)


headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
print(cookies_dict) # {'acw_tc': '2f624a5d15683855598571166e1c8ef2893eea996c0d50d655ad26580a8d2e', '_ga': 'GA1.2.1270812048.1568385560', 'PHPSESSID': 'q5fck3d22g2723oa7e1johjgc7', '_gid': 'GA1.2.574397917.1568518940', '_gat': '1', 'Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94': '1568518942', 'yaozh_logintime': '1568518954', 'yaozh_user': '813035%09%E9%B1%BC%E5%84%BF%E5%95%8A', 'yaozh_userId': '813035', 'db_w_auth': '712360%09%E9%B1%BC%E5%84%BF%E5%95%8A', 'UtzD_f52b_saltkey': 'fqBS90zI', 'UtzD_f52b_lastvisit': '1568515354', 'UtzD_f52b_lastact': '1568518954%09uc.php%09', 'UtzD_f52b_auth': '721akoEc6ki1%2Fa0HDbNguKPhaRScJh9dJHSsB8DHkTgvpVcxoyVy8G80q7JdTJWuCyxd%2FCAQTB%2FA6C5Uh95%2FTZb6uLk', 'yaozh_uidhas': '1', 'yaozh_mylogin': '1568518956', 'Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94': '1568376534%2C1568385561%2C1568518940'}
response = requests.get(url, headers=headers, cookies=cookies_dict)

with open("yaozhi.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))
