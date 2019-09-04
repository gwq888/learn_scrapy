class MyException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "年龄错误%s"%self.age   # 不要用print， 会发现：抛出异常的时候，这里自己定义的异常信息无法显示

def fun():
    age  = int(input("请输入年龄:"))
    if age<1 or age >200:
        raise MyException(age)
    else:
        print("pass")


__doc__
if __name__ == '__main__':
    fun()

