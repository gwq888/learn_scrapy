class A:
    def say(self):
        print("A",self)

class B(A):

    def say(self):
        print("B",self)
        super().say()  # 不使用super():A.say(self)

B().say()