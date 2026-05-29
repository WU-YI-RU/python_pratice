def myfun(name,age):
    '''
    在這裡使用區塊註解，會變成這裡的說明文件(註解)
    '''
    print("name:",name)
    print("age:",age)

def myfun2(name = "請輸入姓名",age = 99):
    '''
    具名參數的傳遞，順序因有註明了，就不重要了
    對模組化提供其他開發者是好使用的
    '''
    print("name:",name)
    print("age:",age)

#具名和非具名參數可以混用，只是要小心
myfun("frank",38) 
myfun2(age = 38,name = "ddddd") 


