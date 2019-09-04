import  os
path = os.getcwd()
list_files = os.walk(path)
print(list_files)
# x:指定目录的路径，这个是字符串，   y：该目录下的所有文件，这是个列表， z：该目录下的所有文件夹，这是个列表
for x,y,z  in list_files:
    for files in y :
        print(x,files,end=" ")
    print("\t")