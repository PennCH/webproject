
def deco2(func):
    def in_deco(x,y):
        func(x,y)
    return in_deco
@deco2
def bar2(x,y):
    print ('',x+y)
bar2(1,4)
#print(bar2(1,3))

