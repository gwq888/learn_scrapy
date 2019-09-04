
# 内部函数可以正常访问外部函数的局部变量
def outer():
    a = 10
    def inner():
        print("inner a:",a)  # 结果为10：内部函数是可以正常去访问外部函数的局部变量的，是没问题的
    inner()
    print("outer a:",a)  # 结果为10
outer()



# 内部函数可以通过nonlocal关键字来修改外部函数的局部变量
def outer2():
    a =10
    def inner2():
        nonlocal a  # 通过使用关键字nonlocal来修改外部函数的局部变量
        print("inner2 a",a)  #10
        a = 20
    inner2()
    print("outer2 a",a) # 20,外部函数已经被内部函数给修改了值

outer2()