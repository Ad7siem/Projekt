def Bake(what):
    print('Baking {}'.format(what))


def Add(what):
    print('Adding {}'.format(what))


def Mix(what):
    print('Mixing {}'.format(what))


cookbook = [(Add, 'milk'), (Add, 'eggs'), (Add, 'flour'), (Add, 'sugar'), (Mix, 'ingredients'), (Bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)

print('#' * 30)


def Cook(activity, obj):
    activity(obj)


Cook(Bake, 'brownies')

print('-' * 30)

for activity, obj in cookbook:
    Cook(activity, obj)


# ćwiczenia

def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(how, list_number):
    value_list = []
    for x in list_number:
        value_list.append(how(x))
    return value_list


list_number = list(range(11))

print(generate_values(double, list_number))
print(generate_values(root, list_number))
print(generate_values(negative, list_number))
print(generate_values(div2, list_number))
