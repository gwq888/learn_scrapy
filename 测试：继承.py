class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Student(Person):
    def __init__(self, name, age, score):
        # 定义子类时，必须要在子类的构造方法中，也调用父类的构造函数
        '''
            调用父类的构造方法的语法：  父类.__init__(self,参数列表)
            1:疑问：首先，Person.__init__(self)，为什么类可以直接调用该方法呢？ 其实，正常情况下，我们是这么调用的：
                person.方法名(参数列表)，  而python解释器呢！实际上底层是这么调用的： Person.方法名(person,参数列表)
                总之： Person.sayHello(self)  就相当于是： person.sayHello()
            2:疑问：Person.__init__(self, name, age) 里面的self是谁呢？
                自然是student了，其实首先Student类自己的__init__(self)中，self就是student，而在程序执行到
                Person.__init__(self,name,age)的时候，就已经把上面的self给当作参数一样，给传进去了。所以，此时Perosn类的__init__
                (self)中的self，就是Student的对象，所以，如果是继承的情况下，那么父类的name和age，是直接邦给了子类，父类没有参数了，因为用的是self

        '''
        Person.__init__(self, name, age)  # 必须显示的调用，否则解释器不会去调用
        self.score = score


student = Student("张三",21,98)
person = Person("a",12)
print(student.name,student.age,student.score)







# print(Student.mro())
# 结果：[<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]