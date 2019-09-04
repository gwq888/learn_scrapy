

# 1
# 如果有多行内容可以加上 """ ，它可以解决换行问题
# print("""
# 你好啊你阿豪
# asdsadasda
# asdasd
# asdasdas
# dassad
# """)


# 2 多行注释，可以使用   '''
# 2.1 单行注释，可以使用 #


# /（精确除法，有小数点） 和 //（整除）
# /:整数和整数则结果为有小数点， 有小数点的和整数，则结果为有小数点的
# //:整数和整数则结果为整数，没有小数点， 有小数点和整数，则结果为有小数点的
# 4/2=2.0  和  4//2=2


# 使用turtle交互式画图板
'''
    1 import turtle 导入画图板
    2 turtle.showturtle() 显示画图板
    3 turtle.write("hello world") 在画图板上写内容
    4 turtle.forward(100)  将画图板上的箭头往前移动100
    5 turtle.right(60)  将画图板上的箭头右转60度
    6 turtle.left(60)  将画图板上的箭头左转60度
'''


# type()和id()
'''
    type(var):可以得到这个var得类型， 例如：type(4) -----> <class 'int'>   type("中")---->  <class 'str'>
    id(var):可以得到这个var在内存中存放的地址
'''


# int
# python3中只有int类型来表达数字，而python2中有long类型

# del：删除指定的变量，此后，该变量不可以再被使用，否则报错：找不到这个变量
'''
    num =10
    print(num) --->10
    del num  删除num这个变量
    print(num) --->报错
'''


# 连续赋值
'''
    num1=20
    num2=20
    print(num1,num2)====>输出 20，20
    
    使用连续赋值：
    num1=num2=20
'''

# 交互赋值
'''
    num1=10
    num2=21

    使用交互赋值，左右必须对称，不多左边多，右边少，左边有2个变量，那么右边也必须有2个
    num1,num2=10,21
    print(num1,num2) ====>10,21
'''

# eval() 函数用来将字符串 当成 有效的表达式 来求值 并 返回计算结果
'''


num = "2" #将字符串转成int类型
print(type(eval(num)))<class 'int'>
 
In [1]: eval("1 + 1")  # 基本的数学计算
Out[1]: 2

In [2]: eval("'*' * 10")  # 字符串重复
Out[2]: '**********'

In [3]: type(eval("[1, 2, 3, 4, 5]"))  # 将字符串转换成列表
Out[3]: list

In [4]: type(eval("{'name': 'xiaoming', 'age': 18}"))  # 将字符串转换成字典
Out[4]: dict

'''


# 用\将多行链接，当成一行,最终输出的结果还是一行，只是看起来分成多行了，实际上还是一行。这也是为了显的好看清楚一点
'''
   print("jsokdnmlksndlqwkdmqlwkmdq \
            aslkdjaslkdjqlkwmdql;dmqw \
            aslkdjaslkdjqlkwmdql;dmqw \
            aslkdjaslkdjqlkwmdql;dmqw \
    ad")

'''


# 多行归并为一行
'''
    可以用分号来进行分割，最后一个不需要分号
    num1=1;num2=4;num3=5;print(num1,num2,num3) 

'''


# **表示次方，  *表示乘号，**表示次方。
# print(100**3)   100的3次方====1000000


# 科学计数法
'''
    data = 1.5e3    //这个相当于是 1.5 （乘以1000,也就是10的三次方，  e3就表示1后面有3个0）
    print(data) ====> 1500.0
    
    data = 1.5e-4   //这个相当于是1.5 （除以10000，也就是10的四次方，e-4就表示1后面有4个0）
    print(data)====>0.00015

'''


# str()
'''
    将整数转换成字符串类型
    num=21
    num=str(num)
    print(type(num)) =====> <class 'str'>
'''

# int()
'''
    将有小数点的数字 取整（去除小数点）  ps：必须是数字类型的小数点，不可以是字符串
    num=4.2
    int(num) =====>结果为4
'''




# round()
'''
    四舍五入（最终会去除小数点的）
    例如：num=4.64
    round(num) =====>结果为：5
    
    也可以指定四舍五入的浮点数：
    例如：print(round(10.02436,4))   4:指定四舍五入的小数点为4   ===》结果为10.0244
    print(round(10.02999999,4))  ===》结果还是为10.03   计算的规律和上面是一样的，但是别忘了，2后面全是9，+1就是 0
'''


# None
'''
    一个变量如果没有赋值，那么该变量，最开始就是None
    
'''


# **0.5=====》平方根   **2 ====》2次方



# 需要导入math包
# abs(-4) ===>4  得到绝对值
# max(1,2,4) ===>4  得到其中最大的值
# min(1,2,4) ===>1  得到其中最小的值
# pow(2,4) ===>16 得到   相当于是2**4，2的4次方，也就是2^4=2*2*2*2
# math.sqrt(4)===> 2（4的开方当然为2）   得出指定值的平方根   math.sqrt(9) ===>3



# \u统一码


# print的高级用法
'''
1：end
end="" 可以用来指定，print末尾的内容，不管末尾是换行，还是空格，还是指定的字符串，都可以
//print默认就会换行，你可以不写 end="\n"，当然写了也是一样的效果 ，都是换行
print("wo",end="\n")   
print("rs")


print("wo",end="****")  =====> wo****




2：sep：指定间隔内容
sep不写的话，默认是空格

例如：print(1,2,3,sep="*")======>  1*2*3
print(1,2,3)====>1 2 3  有空格的中间
'''



'''
    90:宽度的意思，说白了，就是我设定了前面整数可以有90个，
    >:向右对齐，默认不写的话，就是向右对齐，
    1f:保留1位小数点，注意，这个是会四舍五入的比如：  512.25====>最终结果为：521.3
'''
# print(format(533,"10d"))
# print(format(512121.26,">30.1f"))
# print(type(format(51241214.23,">30.1f")))
#
#
# print(ord('A'))


# 浮点数转成整数后所产生的误差
'''
    例如： num=5.45
    print(int(num)) ====>结果为5，而后面的0.45就被舍弃了，这就造成了误差
'''




name =()
if not name:
    print("heh")
age =3
if  age==3:
    print("ss")


num=0
sum=0
while num<=100:
    sum+=num
    num+=1
print(sum)



for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}".format(x,y,x*y),end='\t')
    print("\n")



# 集合是无序，可变的，元素不能重复



def g():
    '''
        这段方法的注释，在调用方法对象（方法也是对象）的 __doc__后，就会出现这个注释，还是比较方便的，方便其他人观看这个方法的用处
    '''

print(g.__doc__)