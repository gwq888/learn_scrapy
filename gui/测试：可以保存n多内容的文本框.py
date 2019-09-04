import tkinter
main = tkinter.Tk()
myText = tkinter.Text(main)
myText.pack()
# 往文本框插入内容   \r\n是换行
myText.insert(tkinter.INSERT, '这是一段内容，会显示在文本框里\r\n')
myText.insert(tkinter.INSERT, '这是一段内容，会显示在文本框里\r\n')
myText.insert(tkinter.INSERT, '这是一段内容，会显示在文本框里\r\n')



main.mainloop()