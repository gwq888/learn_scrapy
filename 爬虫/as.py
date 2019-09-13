import urllib
import urllib.request
import selenium  # 这是一个web自动化测试框架，他可以模拟浏览器
import selenium.webdriver # 模拟浏览器
import re

'''
# 正常访问，  如果出现Bad Gateway ，说明该网站屏蔽了urllib库，此时的话，我们 可以使用selenium框架来模拟浏览器登录，这样该网站就无法屏蔽了
url = "https://search.51job.com/list/070400,000000,0000,32,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
allHtml = urllib.request.urlopen(url).read()
# print (allHtml.decode("gb2312"))
a = "<div class=\"rt\">共102条职位</div>"
r = re.findall("<div class=\"rt\">\s*共(\d+)\S*\s*</div>",allHtml.decode("gb2312"))
# print(r)
'''
url = "https://search.51job.com/list/070400,000000,0000,32,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
# 这个是火狐的driver， 需要去网上下载一个
chrome_path = r"C:\firefox_dirver\geckodriver.exe"
chrome_path = r"C:\firefox_dirver\geckodriver.exe"
# 模拟使用chrome浏览器来登录 该网站
driver = selenium.webdriver.Firefox(executable_path=chrome_path)
driver.get(url)  # 模拟chrome去访问我们指定的url了
pageSource = driver.page_source # 获取该网页的源码
result = re.findall("共(\d+)条职位", pageSource)
print(result)
driver.close()


