passline = 60#G 全局变量
# L LOCAL函数内部作用域
# E enclosing 函数内部与内嵌函数
# G global 全局作用域
# B build-in 内置作用域
def func(val):# val是本地变量
    print('%x'%id(val))
   # passline = 90
    if val >= passline:#全局变量
        print('pass')
    else:
        print('failed')
    def in_func():
        print(val)
    in_func()
    return in_func
#def Max(val1, val2):
    #return max(val1,val2) #max在build-in中
f = func(89)
f()#in_func
print(f.__closure__)
#print(Max(90,100))

# 闭包
# 内部函数对enclosing作用域的变量进行引用