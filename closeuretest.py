def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            #def g():
                return  j*j #当返回结果集时使用print (f1,f2,f3)
            #return g #当这里返回函数时，使用print(f1(),f2(),f3(0)
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print (f1,f2,f3)
#print (f1(),f2(),f3())
'''
多行注释
'''
