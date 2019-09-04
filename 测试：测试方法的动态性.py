class Student:
    def sayHello(self):
        print("你好")



s = Student()
s.sayHello()

# 由于Python是动态语言，所以，我们可以动态的添加新的方法进去，比如此时，Student中可是没有sayGoodBye（）方法的
def sayGoodBye(c):   # 准备将这个方法给动态的添加到Student类中，现在定义方法
    print("再见",id(c))   # 这个c是s这个对象

Student.byebye = sayGoodBye
s.byebye()     #--->为什么这里s可以去掉bytebyte方法呢？ 因为底层其实就是这么调的： Student.byebye(s)


print(id(s))
print("Student类：",id(Student))

Student.sayHello = sayGoodBye
s.sayHello()