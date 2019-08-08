import time

source = 'reportLine += 1'

reportLine = 0

start = time.time()
for i in range(1000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start

start = time.time()
sourceComplited = compile(source, 'internal variablesource', 'exec') # w nawiasach trzeba użyć parametrów: co nalezy skompilowac = fragment tekstu do skompilowania || plik - plik z ktorego tekst zostal przeczytany, jezeli tekst nie byl przecztany tylko poprostu znajdowal sie w zmiennej to mozna umiescic dowolny tekst || tryb - wprowadzamy exec - moze zawierac dowolny fragment kodu ktory jest do wykonania lub eval - zawiera wyrazenie lub simple - do skompilowania jest jedna instrukcja
for i in range(1000):
    exec(sourceComplited)
stop = time.time()
time_compiled = stop - start

print(time_not_compiled)
print(time_compiled)
print(time_not_compiled / time_compiled)

print(reportLine)

# ćwiczenia

import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)
    i += 1

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('Minimalna wartość obliczeń wynosi:', min(results_list), ', a maksymalna to:', max(results_list))
    stop = time.time()
    print('Obliczenia trwały:', stop - start)

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('Minimalna wartość obliczeń wynosi:', min(results_list), ', a maksymalna to:', max(results_list))
    stop = time.time()
    print('Obliczenia trwały:', stop - start)