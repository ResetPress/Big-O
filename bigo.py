import time

def constant_time():
    print(0)
    time.sleep(0.5)
    print('kaboom')

def log_time(n):
    x = n

    while x > 0.9:
        print(round(x))
        x /= 2
        time.sleep(0.5)

    constant_time()

def linear_time(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(0.5)

    constant_time()

def nlog_time(n):
    for i in range(n):
        log_time(n)
        if i != (n-1):
            print(f'{i+1} and counting iterations...')
        else:
            print('Finally!!')

def poly_time(n,p):
    x = n**p

    for i in range(x,0,-1):
        print(i)
        print(f'only {i-1} more iterations...')
        time.sleep(0.25)

    print('kaboom')
    print('Finally!!')

def expo_time(n):
    x = 2**n

    for i in range(x,0,-1):
        print(i)
        print(f'only {i-1} more iterations...')
        time.sleep(0.25)

    print('kaboom')
    print('Finally!!')

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fact_time(n):
    x = factorial(n)

    for i in range(x,0,-1):
        print(i)
        print(f'only {i-1} more iterations...')
        time.sleep(0.25)

    print('kaboom')
    print('Finally!!')

#constant_time()
#log_time(32)
#linear_time(10)
#nlog_time(4)
#poly_time(3,2)
#expo_time(8)
fact_time(3)
