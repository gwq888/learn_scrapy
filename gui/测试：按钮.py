import tkinter
main = tkinter.Tk()

def sayHello():
    print("你好!")

'''
    main: 把按钮放在窗口上，所以这里需要把窗口（也就是main）给放进去
    text：按钮叫什么
    command：点击按钮后，后台会显示什么内容
'''
myButton = tkinter.Button(main,text='点击我sayHello',command = sayHello)
# 压缩按钮，这样的话，按钮就会变成一个小按钮，否则的话，如果不调用pack()的话，那么按钮会霸占整个窗口，并且按钮点击了没有任何反应
myButton.pack()

main.mainloop()



