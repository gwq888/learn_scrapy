class Employee:
    def __init__(self, salary):
        self.__salary = salary

    # getter
    def get_Salary(self):
        return self.__salary

    # setter
    def set_Salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("对不起，工资非法")

em = Employee(4000)
print(em.get_Salary())

em.set_Salary(3000)
print(em.get_Salary())


print(Employee.mro().__doc__)