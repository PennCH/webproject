#coding:utf-8
def dec(func):
    print('call dec')
    def in_dec(*arg):
        print('in dec arg=', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec
@dec
def my_sum(*arg):
    print('in my_sum')
    return sum(arg)
print(my_sum(1,2,3,4,5,6))
@dec
def my_average(*arg):
    print('in my_average')
    return sum(arg)/len(arg)
print(my_average(1,2,3,4,5,6))
#my_sum = dec(my_sum)