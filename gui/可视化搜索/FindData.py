import codecs
import  io
# import gui.可视化搜索.ShowItem
from gui.可视化搜索.ShowItem import ItemShowByList
class BigDataFind:
    def __init__(self, path):
        self.itemShowByList = ItemShowByList()
        # self.file = codecs.open(path, 'r', 'utf-8', 'ignore')
        self.file = io.open(path, 'r', encoding='gb2312')
        # self.file = path

    def find(self, keyword):
        while True:
            line = self.file.readline()
            if not line:   # 如果读完了，那么line='' 空字符串就是False
                break
            else:
                # 如果不等于-1，说明找到了我们要找的内容
                key = line.find(keyword)
                if key != -1:
                    print(line)
                    self.itemShowByList.showData(line)
        self.itemShowByList.show()

    # 程序结束后，该对象就死了，那么就会调用该方法，来释放资源
    def __del__(self):
        self.file.close()