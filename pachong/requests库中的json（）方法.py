import requests
import re
import json
'''
gihub的一个网页，这个网页里，打开，就一个样东西： 
                    一个json串 ---> {
                                       "message": "Requires authentication",
                                      "documentation_url": "https://developer.github.com/v3/users/#get-the-authenticated-user"
                                     }
'''
url = "https://api.github.com/user"
response = requests.get(url)
# url网页里就只有json串，通过json（）函数，requests库会自动帮我们把json串，给转成python中的 dict字典
r = response.json()
print(r) # {'message': 'Requires authentication', 'documentation_url': 'https://developer.github.com/v3/users/#get-the-authenticated-user'}
print(r['message']) # Requires authentication

########如果没有requests库提供的  json（）函数的话，我们会这么做：
# 1.先拿到内容
a = response.content.decode("utf-8")
# 2.假设这里拿到了网页上的json串内容
json_str = re.findall("这里写正则，这个正则，需要拿到网页里的json串内容",a)
# 3.开始调用python提供的json模块中的，loads（）方法：该方法可以将json串给转成 dict字典
json_dict = json.loads(json_str)
# 4.此时已经将json串给转成了dict字典
print(json_str['message'])



