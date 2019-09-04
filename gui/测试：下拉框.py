import tkinter
from tkinter import ttk
main = tkinter.Tk()
# 将选项框给放到窗口上
myComboboxList = ttk.Combobox(main)
# 设置选项中的 选项内容，这里我们给了4个选项内容
myComboboxList['value'] = ('选项1', '选项2', '选项3', '选项4')
# 这里需要给出一个参数用来接受页面上选中 选项后，将选项内容（其实是一个事件）给传进来
def show(str):
    # 当页面上选中了某个选项的时候，可以通过下面的函数来得到页面上选中的内容
    print(myComboboxList.get())
    # 这个是一个事件对象，如果要拿到选项中选中的值，那么只能用上面的方式
    # print(type(str)) # <class 'tkinter.Event'>

# 这里是在给选项框绑定事件：选中选项内容触发事件，触发事件后，调用show（）函数
myComboboxList.bind('<<ComboboxSelected>>',show)

# 打开窗口是，选项框默认选中什么内容，这里给了0，表示默认选中选项框的第一个内容
myComboboxList.current(0)
# 压缩选项框，使他在页面上正常显示
myComboboxList.pack()

main.mainloop()