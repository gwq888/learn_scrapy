import turtle
turtle.showturtle()


# 使用goto的时候，其实不需要调 角度的，也就是可以不使用right()和left()来调角度，只要给定了，x轴，y轴，直接使用goto就可以去到指定的地点
turtle.goto(50, -200)
turtle.goto(-100, -80)
turtle.goto(100, -80)
turtle.goto(-50, -200)
turtle.goto(0, 0)

turtle.done()