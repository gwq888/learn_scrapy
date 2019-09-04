
import  os
list_files = os.listdir("F:\work\linux_file")



def find(path):
    all_file = os.listdir(path)
    for file in  all_file:
        while os.path.isdir(file):
            os.listdir(file)

