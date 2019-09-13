import tkinter
from tkinter import ttk
main = tkinter.Tk()
myTreeView = ttk.Treeview(main)
'''
    第一个参数： "" 表示父节点
    第二个参数:  0 表示位置，这个值是可以觉得那个选项在前，哪个选项在后的，值越小，那么就越靠前，因为0就是第一个  1就是第二个
    第三个参数： text  表示选项的内容  
    第四个参数： value  表示该选项代表着的值，这个跟前端里的选项是一个意思， 
'''
china = myTreeView.insert("",0,text="中国",value=1)
'''
    其他参数，不说了，参考上面，就说第一个参数： china
    因为是树状结构： 
                china
                    南京
                    北京
    所以，南京肯定是要在china下面的，那么南京的父节点就是china
    还有第二个参数： 北京和南京分别是1和0 ，那么南京就会在北京的前面，原因见上面
'''
myTreeView.insert(china,1,text="北京",value=2)
myTreeView.insert(china,0,text="南京",value=3)


america = myTreeView.insert("",0,text="美国",value=4)
myTreeView.insert(america, 0,text="加州",value=5)


myTreeView.pack()


main.mainloop()