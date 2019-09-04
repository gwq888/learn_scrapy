import time

# 得到随机字母  a-z
nowtime= time.time()
zimu= int(nowtime%26)  #0-26之间，不包括26，这是取模运算的规律,浮点数也是可以取模运算的
print(zimu)
print(chr((ord('A')+zimu)))

print

