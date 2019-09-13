

import os

index = 0
start = 0
def get(str,newfilename,newstart):
    global start
    if newstart!=0:
        for  x in range(0,newstart):
            print("------------------------",end='')
    if os.path.isfile(str):
        print(newfilename)
    else:
        if newstart == 0:
            print(str)
        else:
            print(newfilename)
        newstart += 1
        tempdir = os.listdir(str)
        for x in tempdir:
            get(str+'\\'+x,x,newstart)

# get("F:\\学习视频\\我的危险妻子")
# get(r"F:\学习视频\并发")
# get(r"F:\学习视频\并发")
# get(r"F:\a")
# get(r"D:\API\jdk api 1.8_google","",0)
get(r"D:\冒险岛2","",0)

# #
# print(os.path.isfile("F:\\a.text")) # True
# print(os.path.isfile("F:\\a.txt")) # False



a_str = b'\xe4\xb8\xad\xe5\x9b\xbd' # 中国 的utf-8编码
a2= a_str.decode('utf-8')
print(a2)

