def my_decorator(func):
    def inner_func(*args, **kwargs):
        x = func(*args, **kwargs)

        for n in range(0, x):
            for m in range(0, n+1):
                print('x', end='')
            print('\r')
            
    return inner_func
    

@my_decorator
def add(x, y):
    sum = x + y
    return sum


add(10, 2)



