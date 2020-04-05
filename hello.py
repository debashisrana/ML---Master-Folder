from functools import wraps

def deco_func(anyfunc):
    @wraps(anyfunc)
    def warpper(*args,**kwargs):
        print('this is the warpper function')
        return anyfunc(*args,**kwargs)
    return warpper

@deco_func
def func(a,b):
    return a+b

print(func(5,6))