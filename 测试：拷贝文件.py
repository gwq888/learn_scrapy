import io
with io.open("a.png",'rb') as r :
    with io.open("b.png",'wb') as w:
        w.writelines(r.readlines())