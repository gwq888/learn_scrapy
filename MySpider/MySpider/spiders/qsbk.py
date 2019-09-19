# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.selector import Selector

'''
    不论使用urllib还是使用requests库经常会遇到中文编码错误的问题，我就经常遇到，因为python安装在windows平台上，cmd的默认编码为GBK，所以在cmd中显示中文时会经常提示gbk编码错误，后来找到了贴在，完美的解决了该问题，下面我分享给大家

UnicodeEncodeError: 'gbk' codec can't encode character '\xbb' in position 0: illegal multibyte sequence
在cmd中我们输出data.read()时，中文乱码，大部分时候是因为print函数，其实print()函数的局限就是Python默认编码的局限，因为系统是win7的，python的默认编码不是'utf-8',改一下python的默认编码成'utf-8'就行了，
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码 
可以看到该语句修改了python的默认编码为utf8，并赋予了我们的stdout输出，使得python的输出默认编码为utf8，但是当我们在cmd中输出还是中文乱码，这是cmd的锅，cmd不能很好地兼容utf8，而IDLE就可以，甚至在IDLE下运行，连“改变标准输出的默认编码”都不用，因为它默认就是utf8。
如果一定要在cmd下运行，那就改一下编码，比如我换成“gb18030”，就能正常显示了：
'''
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') #为了在cmd中显示不乱码

class QsbkSpider(scrapy.Spider):

    name = 'qsbk'
    allowed_domains = ['qsbk.com']
    # 要爬取的网址
    start_urls = ['https://dig.chouti.com/']

    def parse(self, response):
        # 可以同body来获取页面上的所有内容
        # print(response.body)
        #

        """
            Selector底层用的是lxml解析库， 就把这个Selector理解为是xpath就行了
            1.Selector(response=response)：整个文档对象
                response是网页的整个内容， 这不就是文档吗，这不就是之前学的etree（）一样的用法吗
            2.后面的xpath，就是用的xpath的语法

        """
        a_html = Selector(response=response).\
            xpath('//div[@class="link-detail"]/a[@class="link-title link-statistics"]/text()').extract()

        for x in a_html:
            print(x)
