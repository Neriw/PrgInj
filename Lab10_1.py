import time
def timer_dec(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f'\nВремя выполнения {end_time - start_time} сек.')
        return result
    return wrapper
@timer_dec
def fibonachi():
    fib1=fib2=1
    for i in range(2,200):
        fib1,fib2=fib2,fib1+fib2
        print(fib2, end=" ")
fibonachi()