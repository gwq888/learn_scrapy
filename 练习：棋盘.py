

import turtle
turtle.showturtle()

# 常规方式，不使用循环的方式来解决
# turtle.penup()
# turtle.goto(-350,200)
# turtle.pendown()
# turtle.forward(500)
#
# turtle.penup()
# turtle.goto(-350,180)
# turtle.pendown()
# turtle.forward(500)
#
# turtle.penup()
# turtle.goto(-350,160)
# turtle.pendown()
# turtle.forward(500)
#
# turtle.penup()
# turtle.goto(-350,140)
# turtle.pendown()
# turtle.forward(500)




turtle.speed(0)  # 画线的速度调到最大

y_zhou = 200   # y轴的初始高度


# while循环的方式来解决
# while y_zhou > -200:
#     turtle.penup()
#     turtle.goto(-350, y_zhou)
#     turtle.pendown()
#     turtle.forward(500)
#     y_zhou -= 20


# for循环的方式来解决
for x in range(200,-200,-20):
    turtle.penup()
    turtle.goto(-350, x)
    turtle.pendown()
    turtle.forward(500)


turtle.write('y轴为：{0}'.format(y_zhou))

# while循环的方式来解决
x_zhou = -350
# while x_zhou<170:
#     turtle.penup()
#     turtle.goto(x_zhou, 200)
#     if x_zhou == -350:turtle.right(90)
#     turtle.pendown()
#     turtle.forward(380)
#     x_zhou += 20

# for循环的方式来解决
for x in range(-350,170,20):
    turtle.penup()
    turtle.goto(x, 200)
    if x == -350: turtle.right(90)
    turtle.pendown()
    turtle.forward(380)







turtle.done()  #画完以后，窗口不关闭