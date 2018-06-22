def deco(func):
    def in_deco(*args):
        return func(*args)
    return in_deco
@deco
def bar(*args):
    #print('in bar:', sum(*args))
    return sum(args)
print(bar(1,3))



