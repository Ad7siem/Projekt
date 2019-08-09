def BuyMe(what):
    print('Give me', what)


BuyMe('a new car')

StealForMe = BuyMe
print(type(StealForMe))
StealForMe('a new car')


def GoLeft(*args):
    print('PLACEHOLDER - turn left with', *args)


def GoRight(*args):
    print('PLACEHOLDER - turn right with', *args)


def GoForward(*args):
    print('PLACEHOLDER - turn forward with', *args)


def GoBack(*args):
    print('PLACEHOLDER - turn back with', *args)


def Start(*args):
    print('PLACEHOLDER - starting with', *args)


def Stop(*args):
    print('PLACEHOLDER - stopping', *args)


instructions = [Start, GoForward, GoForward, GoLeft, GoForward, GoRight, Stop]

dish = 'pizza'
for instr in instructions:
    instr(dish)


# ćwiczenia

def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
list_transformations = [double, root, div2, negative]
tmp_return_value = number

for list in list_transformations:
    tmp = list(tmp_return_value)
    print('{}:\t temporal result is:\t {}'.format(list.__name__, tmp))

list_transformations = [root,root,div2,double]

for list in list_transformations:
    tmp = list(tmp_return_value)
    print('{}:\t temporal result is:\t {}'.format(list.__name__, tmp))
