import time
from functools import reduce


def performance(f):# 装饰器函数 原函数作为参数的函数为装饰器函数
    def fn(*arg, **kw):
        t1 = time.time()
        r = f(*arg, **kw)
        t2 = time.time()
        print ('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r #调用原函数
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print (factorial(10))