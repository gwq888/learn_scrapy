import tkinter
from tkinter import ttk
main = tkinter.Tk()

myTreeView = ttk.Treeview(main)
myTreeView.pack()

# 声明表格有几个属性，注意：只是先声明，此时并不会显示在表格里面
# 这里的话，有3个属性，说明：表格有3列
myTreeView['columns'] = ("姓名", '年龄', '性别')

# 开始给每一列指定宽度，此时，并不会显示在表格里面
myTreeView.column('年龄',width=100)
myTreeView.column('性别',width=100)
myTreeView.column('姓名',width=100)

# 开始显示在表格里，text：每一列的名称
myTreeView.heading('年龄', text='年龄---')
myTreeView.heading('姓名', text='姓名---')
myTreeView.heading('性别', text='性别---')

# 往表格里插入内容
#  0:第一列名称  1：第二列名称  2：第三列名称
#  text:行名称
# values ：每行的内容，需要对应着列
myTreeView.insert("",0, text='行1',values=('张三','男','12'))
myTreeView.insert("",1, text='行2',values=('里斯','男','12'))
myTreeView.insert("",2, text='行3',values=('王五','男','12'))




main.mainloop()