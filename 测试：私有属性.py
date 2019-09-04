
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def __sayHello(self):
        print("我是私有方法")

s = Student("张三",14)
print(s.name)
# print(s.age) ------------>报错，s没有这个age属性，因为age是私有的
print(s._Student__age) # 通过 _类名__需要访问的私有属性名称  就可以成功访问私有属性


# s.__sayHello()  # 私有方法不可以这样访问，会报错
s._Student__sayHello()