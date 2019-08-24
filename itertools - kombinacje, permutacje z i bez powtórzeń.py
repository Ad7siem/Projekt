import itertools as it

# mylist = ['a','b','c','d']

# for combination in it.combinations(mylist, 3):  # kombinacja 3 elementowe z listy mylist, kolejnosc jest nie istotna.
#    # Jesli miala by miec znaczenie trzeba uzyc funkcji permutations. W przypadku kombinacji z powtorzeniami to
#    # combinations_with_replacement
#    print(combination)

'''
money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

results = []

for i in range (1,101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            results.append(combination)

results = set(results)

for result in results:
    print(result)
'''
import math

money = [50, 20, 10]

for i in range(1,101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)


print('-'*30)

# ćwiczenia

notes = ['C', 'D','E','F','G','A','H']

for permutation in it.permutations(notes, 4):
    print(permutation)


print('4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities'.format(math.factorial(len(notes))/math.factorial(len(notes) - 4)))

print('-'*30)

for p in it.product(notes, repeat=4):
    print(p)

print('4-notes melody - notes can repeat = it is variation with repeating - there are {} possibilities'.format(pow(len(notes), 4)))