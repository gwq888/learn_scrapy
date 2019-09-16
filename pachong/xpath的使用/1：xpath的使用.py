from lxml import etree
# lxml是第一个第三方库，它使用了xpath这个语法（xpath就是个语法）
import requests
import fake_useragent

headers = {
    "User-Agent": fake_useragent.UserAgent().random
}

response = requests.get("http://news.baidu.com/", headers=headers)
source_html = response.content.decode("utf-8")

# 将整个页面变成了一个 类似于 文档对象 了，然后就可以操作它的节点了
html_document = etree.HTML(source_html)

'''
    xpath语法：   
        1. /a 一层一层节点找过去，如下面的，title节点，在html/head下面
        2. //a 跨节点，我不需要按照上面的一样，一层一层节点的找过去，这样的话，很繁琐，效率很低，我直接//去整个页面上找节点
        3. //a[@属性=属性值]  精确标签 
        4. @属性 //a[@属性=属性值]/@href  拿到该标签的href属性
        5. text() 拿到标签的内容
'''
# text（）是找到指定节点的内容
result = html_document.xpath("/html/head/title/text()") # 找到网页里的title节点的 内容
print(result) # ['百度一下，你就知道']

# 跨节点去找a这个节点，会找到很多很多a节点
result = html_document.xpath("//a/text()")
print(result) # ['手写', '拼音', '关闭', '百度首页', '设置', '登录', '新闻' .........] 这些都是所有a节点的内容

# 跨节点找a这个节点，会将页面上的所有a节点给找出来，但是，我们只有一个想找的a节点，所以，可以把这个a节点的属性指定出来
# 用[@属性] 来指定找a标签
result = html_document.xpath('//a[@mon="ct=1&a=2&c=top&pn=8"]/text()')
print(result) # ['中国女排3比0战胜喀麦隆，郎平和队员这样点评']
# 拿到a标签的 href属性
result = html_document.xpath('//a[@mon="ct=1&a=2&c=top&pn=8"]/@href')
print(result)
