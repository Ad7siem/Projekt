'''import time
import functools


@functools.lru_cache()
def Factorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Czas obliczeń:', stop - start)

print(Factorial.cache_info())

start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Czas obliczeń:', stop - start)
'''
# ćwiczenia

import time
import functools


def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


@functools.lru_cache(100)
def fib_optimal(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 35):
    print('{} = {}'.format(i, fib(i)))
stop = time.time()
print('Czas obliczeń: ', time1=stop - start)

start = time.time()
for i in range(1, 35):
    print('{} = {}'.format(i, fib_optimal(i)))
stop = time.time()
print('Czas obliczeń: ', time2=stop - start)

print(fib_optimal.cache_info())
print('Różnica czasu obliczen wynosi:', time1-time2)