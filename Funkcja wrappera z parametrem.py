import datetime
import functools


# logFilePath = r'D:\temp\function_log.txt'

def CreaterFunctionWithWrapper_LogToFile(logFilePath):
    def CreaterFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, 'a+')
            file.write('-' * 20 + '\n')
            file.write('Function "{}" started at {}\n'.format(func.__name__, datetime.datetime.now().isoformat(' ')))
            file.write('Following arguments were used:\n')
            file.write('\t'.join('{}'.format(x) for x in args))
            file.write('\n')
            file.write('\t'.join('{}={}'.format(k, v) for (k, v) in kwargs.items()))
            file.write('\n')
            result = func(*args, **kwargs)
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result

        return func_with_wrapper

    return CreaterFunctionWithWrapper


@CreaterFunctionWithWrapper_LogToFile(r'D:\temp\change_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary


@CreaterFunctionWithWrapper_LogToFile(r'D:\temp\change_position_log.txt')
def ChangePosition(emp_name, new_position):
    print('CHANGING POSITION FOR {} TO {}'.format(emp_name, new_position))
    return new_position


print(ChangeSalary('Johnson', 20000, True))
print(ChangeSalary('Johnson', 20000, is_bonus=True))
print(ChangePosition('Micheal', 'Salesman'))
print(ChangePosition('Anke', 'Manager'))

print('-' * 30, '\n')
# ćwiczenia

import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with open(log_file_path, 'a') as f:
                f.write('Action {} executed on {} on {} \n'.format(logged_action, path,
                                                                   datetime.datetime.now().isoformat(' ')))
            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'D:\temp\file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', r'D:\temp\file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'D:\temp\dummy_file.txt')
delete_file(r'D:\temp\dummy_file.txt')
create_file(r'D:\temp\dummy_file.txt')
delete_file(r'D:\temp\dummy_file.txt')
