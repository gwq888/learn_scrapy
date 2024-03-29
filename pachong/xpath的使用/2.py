from lxml import etree

str = '''
    <ul>
        <li>1
            <a>1</a>
        </li>
        <li>2
            <a>2</a>
        </li>
        <li>3
            <a>3</a>
        </li>
        <li>4
            <a>4</a>
        </li>
        <li>5
            <a>5</a>
        </li>
    </ul>
        
   
'''
xpath_data = etree.HTML(str)
# 取出所有li标签下的所有a标签的内容
r = xpath_data.xpath("//li/a/text()")
print(r) # ['1', '2', '3', '4', '5']
# 查看li标签有几个
r = xpath_data.xpath("//li")
print(len(r)) # 5
# 拿到第二个li标签里的内容， ps：xpath中， 下表是从1开始的，不是从0
r = xpath_data.xpath("//li[2]/text()")
'''
    为什么结果是：['2\n            ', '\n        ']
    1.首先查看结构：
        <li>2
            <a>2</a>
        </li>
    2.我们的xpath再用text()取内容的时候，如果标签里还有标签，那么就会先取里面标签的前部分内容， 再取后部分内容
        如上面，
         <li>标签内容是： 2\n很多空格     然后由于有</a>标签后面还有空格，那么xpath就认为<li>标签还有内容没取完毕，
         所以还会取</a>标签后面的内容，也就是\n空格
         合起来就是：['2\n            ', '\n        ']
    3. 如果我们把a标签后面的空格去掉，那么说明li标签后半部就没有内容了
        例子：
             <li>2
            <a>2</a></li>
        输出：['2\n            ']
            
'''
print(r) # ['2\n            ', '\n        ']



# 既然 //li[2] 都可以指定取出第2个li标签，那么我们就会想当然的觉得 //a[2]也可以， 毕竟 a标签和li标签，同样都有一共5个标签
r = xpath_data.xpath("//a[2]")
'''
    发现是空的，为什么？
        因为，<li>标签一共有5个标签，这5个标签都是 平级的，就是说在一个层次上
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
        而我们的 <a>标签，并不在一个层次，不在一个平级
            <li>
                <a></a>
            </li>
            <li>
                <a></a>
            </li>
            <li>
                <a></a>
            </li>
            ........
        总结： 用[]取出指定的第几个标签，  该标签必须是平级的
'''
print(r) # []  发现是空的，


