def double(x):
    return x * 2


x = 10
x = double(x)
print(x)

x = 10
f = lambda x: x * 2
print(f(x))


def power(x, y):
    return x ** y


x = 5
y = 3
print(power(x, y))

f = lambda x, y: x ** y  # wyrazenie funkcyjne
print(f(x, y))

list_number = [1, 2, 3, 4, 11, 14, 15, 20, 21]


def is_odd(x):
    return x % 2 != 0


print(is_odd(7), is_odd(4))

filtered_list = list(filter(is_odd, list_number))  # funkcja filter przyjmuje dwa argumenty: nazwa funkcji sprawdzajaca
# czy warunek jest spelniony, obiekt interable ktorym jest lista

print(filtered_list)

filtered_list = list(filter(lambda x: x % 2 != 0, list_number))
print(filtered_list)

print(list(filter(lambda x: x % 2 != 0, list_number)))


def generate_mutiply_function(n):
    return lambda x: n * x


mul_2 = generate_mutiply_function(2)
mul_3 = generate_mutiply_function(3)

print(mul_2(13), mul_3(8))
print('-' * 30)
# ćwiczenia

text_list = ['x', 'xxx', 'xxxx', 'xxxxxxx', '']

f = lambda x: len(x)

print(f('co tu ma on do tego'))
print(list(map(f, text_list)))
print(list(map(lambda t: len(t), text_list)))
