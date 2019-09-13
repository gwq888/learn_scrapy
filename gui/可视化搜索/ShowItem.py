import tkinter
class ItemShowByList:
    def __init__(self):
        self.main = tkinter.Tk()
        self.listBox = tkinter.Listbox(self.main)

        self.listBox.pack()
    def showData(self, item):
        self.listBox.insert(tkinter.END, item)

    def show(self):
        self.main.mainloop()


# 测试
if __name__ == '__main__':
    i =ItemShowByList()
    i.showData("assssssssssssa")
    i.showData("assssssssssssa")
    i.showData("assssssssssssa")
    i.show()
