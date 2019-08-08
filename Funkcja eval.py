var_x = 10
password = "My super secret password"

source = '__import__("os").getcwd()'

#globals = globals().copy()
#del globals['password'] # ze słownika została usunięta zmienna wskazujaca na haslo

globals = {}

result = eval(source,globals)
print(result)

#print(globals())

# ćwiczenia

import math

argument_list = []

for i in range(100) :
    argument_list.append(i/10)
    i += 1

formula = input('Proszę o wprowadzenie wzoru używając zmienej x:')

for x in argument_list:
    print('{0:3.1f} {1:6.2f}'.format(x,eval(formula)))
# print(argument_list)