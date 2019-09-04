import tkinter
main = tkinter.Tk()



myListBox = tkinter.Listbox(main, width=100)
myListBox.pack()

for x in ["我是谁啊","我是你a",'avc','asdad']:
    # tkiner.End：将内容一直插入到尾部
    # x:要在列表框所显示的内容
    myListBox.insert(tkinter.END,x)





main.mainloop()