from functools import wraps

def print_function_data(anyfunc):
    @wraps(anyfunc)
    def wrapper_function(*args,**kwargs):
        print(f'you are calling {anyfunc.__name__} function')
        print(anyfunc.__doc__)
        return anyfunc(*args,**kwargs)
    return wrapper_function

@print_function_data
def add(a,b):
    '''this function takes two arguments and return their sum'''
    return a+b

print(add(5,6))