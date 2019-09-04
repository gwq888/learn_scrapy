class Studeng:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sayHello(self):
        print("{0}今年{1}岁".format(self.name,self.age))

stu1 = Studeng("张三",12)
stu1.sayHello()