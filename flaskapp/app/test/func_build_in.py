
# L LOCAL函数内部作用域
# E enclosing 函数内部与内嵌函数
# G global 全局作用域
# B build-in 内置作用域
def func_150(val):# val是本地变量
    passline = 90
    if val >= passline:#全局变量
        print('%d pass'%val)
    else:
        print('failed')

def func_100(val):# val是本地变量
    passline = 60
    if val >= passline:#全局变量
        print('%d pass' % val)
    else:
        print('failed')

def set_passline(passline):#60
    def cmp(val):#
        if val >= passline:
            print('Pass')
        else:
            print('Failed')
    return cmp
f_100 = set_passline(60)
f_150 = set_passline(90)
#print(type(f_100))
#print(f_100.__closure__)
f_100(89)
f_150(89)
#f_150(89)
#f_150(59)

#func_150(89)
#func_100(89)

# 闭包
# 内部函数对enclosing作用域的变量进行引用