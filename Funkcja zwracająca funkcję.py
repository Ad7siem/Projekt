def Calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for a in args:
            result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result


print(Calculate('+', 1, 2, 3))
print(Calculate('-', 1, 2, 3))


def CreateFunction(kind='+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
    '''.format(kind)
    exec(source, globals())

    return f


f_add = CreateFunction('+')
print(f_add(1, 2, 3, 4))
f_subs = CreateFunction('-')
print(f_subs(10, 20, 30, 40))

print('-' * 30, '\n')

# ćwiczenia

from datetime import datetime


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

print('-' * 30, '\n')


def create_function(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]'''.format(sec)

    exec(source, globals())
    return f


f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

print(f_minutes(start,end))
print(f_hours(start,end))
print(f_days(start,end))
