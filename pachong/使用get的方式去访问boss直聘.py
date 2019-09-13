import urllib
import urllib.parse
import urllib.request
import re
import selenium.webdriver
from fake_useragent import UserAgent
# https://www.zhipin.com/job_detail/?query=python&city=101190200&industry=&position=


def find(language, city):
    useragent = UserAgent()
    searchStr = {'query': language, "city": city}
    agent  = {"user-agent":useragent.random}
    searchStrByUrlEncode = urllib.parse.urlencode(searchStr)
    needSearchUrl = urllib.request.Request("https://www.zhipin.com/job_detail?"+searchStrByUrlEncode+"&industry=&position=",headers=agent)
    # print("https://www.zhipin.com/job_detail/?"+searchStrByUrlEncode+'&industry=&position=')
    result = urllib.request.urlopen(needSearchUrl).read().decode()
    print(result)

print(find("python", "101190200"))



