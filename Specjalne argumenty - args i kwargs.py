def BuyMe(prefix='Please buy me', what='something nice', *args, **kwargs):  # po * moze byc dowolna nazwa zmiennej
    print(prefix, what)
    print(args)
    print(kwargs)


BuyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shope='market', color='any')

products = ['milk', 'bread', 'flakes']
parameters = {'price': 'low', 'time': 'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)

print('#' * 30)


# ćwiczenia

def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint


print(calculate_paint(0.25, 42, 28, 30))

rooms = [42, 28, 30]
print(calculate_paint(0.25, *rooms))

print('#' * 30)


def log_it(*args):
    path = r'D:\temp\log_it.txt'
    with open(path, 'a+') as f:
        for line in args:
            f.write(line)
            f.write(' ')
        f.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
