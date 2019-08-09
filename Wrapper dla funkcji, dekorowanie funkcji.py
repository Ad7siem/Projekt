import datetime
import functools


def CreaterFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return func_with_wrapper


@CreaterFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary


print(ChangeSalary('Johnson', 20000, True))

'''
def CreaterFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" started at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return func_with_wrapper
'''

# ChangeSalary = CreaterFunctionWithWrapper(ChangeSalary)

print(ChangeSalary('Johnson', 20000, is_bonus=True))

print('-' * 30, '\n')

# ćwiczenia

import time


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print('Funkcja {} wykonana w czasie {}'.format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(18))

wrapper_get_sequence = wrapper_time(get_sequence)

print(wrapper_get_sequence(18))

print('-'*30,'\n')

import time
import functools


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print('Funkcja {} wykonana w czasie {}'.format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function

@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(18))
