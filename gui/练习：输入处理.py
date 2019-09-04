import os
import tkinter
main = tkinter.Tk()

# 输入框
myEntry = tkinter.Entry(main, show='*', fg='red', bg='yellow')
myEntry.pack()

def search():
    '''
        可以通过get()方法来取得在输入框输入的内容
    '''
    print(myEntry.get())
    if myEntry.get() == '记事本':
        os.system('notepad')
    else:
        pass

# 按钮
myButton = tkinter.Button(main, text="点击搜索", command=search)
myButton.pack()




main.mainloop()
