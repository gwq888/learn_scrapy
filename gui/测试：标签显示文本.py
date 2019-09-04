import tkinter
main = tkinter.Tk()
# 主窗口的宽600高600 离屏幕左边距离300 离屏幕上边距离100
main.geometry("600x600+300+100")

mylabel = tkinter.Label(main,
                # 上北下南，左西右东
                # East：东  North：北 South：南 West：西
              anchor=tkinter.N,   # lable的位置
              fg="blue", # label标签上内容 的颜色
              bg='yellow', # label标签的整个背景色
              text='label上的内容：哈哈哈嘻嘻',  # label标签上的内容
              # lable标签的宽度和高度
              width=30,
              height=30
              )

# 将 lable标签收缩，其实，就是让label标签正常显示，要不然的话，label标签会跟屏幕一样大
mylabel.pack()
# 进入事件循环
main.mainloop()




