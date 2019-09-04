
class Person:
    def eat(self):
        print("我是人类，我要吃饭")

class Student(Person):
    def eat(self):
        print("我是学生，我要吃饭")

class Man(Person):
    def eat(self):
        print("我是男人，我要吃饭")


def eat(m):
    if isinstance(m,Person):
        m.eat()
    else:
        print("你不是人，没资格 吃饭")
eat(Student())
eat(Man())
object