import tkinter

def sayHello():
    pass

main = tkinter.Tk()

# 按钮
myButton = tkinter.Button(main,text='点击我',width=20,command = sayHello)
myButton.pack()


'''
    main:将文本框给放到窗口中
    show:文本框输入内容后，显示什么， 比如show='*'，那么在文本框输入完内容后，内容就全部显示*，这样就可以做密码来用的
    width:宽度50，height：不可以设置，会报错，因为没有这个height属性
    bg:文本框的背景颜色
    fg:文本框输入的内容颜色
'''
# 文本框
myEntry = tkinter.Entry(main,show='*',width=50,bg='red',fg='yellow')
myEntry.pack()

main.mainloop()
