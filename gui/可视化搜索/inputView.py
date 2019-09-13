import tkinter
from tkinter import ttk
from gui.可视化搜索.FindData import BigDataFind
class InputView:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.geometry("400x400+300+100")
        # 搜索框
        self.entry = ttk.Entry(self.main, show='', width=50)
        # 按钮
        self.button = tkinter.Button(self.main, text='点击搜索', command=self.search)

        # self.bigDataFind = BigDataFind("f:\\人员.txt")
        self.button.pack()
        self.entry.pack()

    def show(self):
        self.main.mainloop()

    # 点击按钮后，获取搜索框的内容，再进一步进行处理
    def search(self):
        # 获取搜索框的内容
        print(self.entry.get())
        self.bigDataFind = BigDataFind("f:\\人员.txt")

        self.bigDataFind.find(self.entry.get())


if __name__ == '__main__':
    i = InputView()
    # i.search()
    i.show()