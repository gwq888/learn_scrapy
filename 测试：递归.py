# 算阶乘   5！=5*4*3*2*1

def test(m):
    if m == 1:
        return 1
    else:
        return m*test(m-1)
n=5
print("{0}!的阶乘是:{1}".format(n,test(n)))

