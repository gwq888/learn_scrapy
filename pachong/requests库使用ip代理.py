import requests
import fake_useragent

header = {
    "User-Agent": fake_useragent.UserAgent().random
}

proxy = {
    "http": "120.83.108.77:9999"
}
response = requests.get("https://www.yaozh.com/", proxies=proxy, headers=header)
print(response.status_code) # 如果是200，说明ip代理使用成功
