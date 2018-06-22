
def deco2(func):
    def in_deco(x,y):
        return func(x,y)
    return in_deco
@deco2
def bar2(x,y):
    return (x+y)
print(bar2(1,3))

