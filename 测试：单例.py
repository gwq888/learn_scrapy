class MySignal:
    # 用来保存单例对象的
    __signalObj = None
    # 用来判断是否被重复初始化多次，我们只想要初始化一次
    __isInit = False  # False：表示还未被初始化

    # __new__是对象被创建的时候会被调用的
    def __new__(cls, *args, **kwargs):
        if cls.__signalObj == None:
            # object.__new__(cls)是创建对象的， 和 my = MySignal() 创建对象是一个 作用，只是写法不同而已
            cls.__signalObj = object.__new__(cls)
        return cls.__signalObj

    # __init__()实际上就对应着创建对象后的  （）2个圆括号，这就是在初始化
    def __init__(self):
        if not MySignal.__isInit:
            print("init...")
            MySignal.__isInit = True  # 表示已经被初始化过一次了

        # 如果已经被初始化过了，那么什么也不做

m1 = MySignal()
m2 = MySignal()
m3 = MySignal()
print(m1)
print(m2)
print(m3)




