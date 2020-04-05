from functools import wraps
import numpy as np 
import time

def print_func(anyfunc):
    @wraps(anyfunc)
    def wrapper_func(*args,**kwargs):
        print('this decorator function calulate time taken to execute\n')
        t1 = time.time()
        result = anyfunc(*args,**kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f'total time taken by the program is {total_time} \n')
        return result
    return wrapper_func


@print_func
def matrix_mul(mat1,mat2):
    mat= np.matmul(mat1,mat2)
    return mat

a1 = np.arange(1,11).reshape(5,2)
a2 = np.arange(21,27).reshape(2,3)
print(matrix_mul(a1,a2))