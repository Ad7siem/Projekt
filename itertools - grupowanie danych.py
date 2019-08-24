'''
import itertools as it

filepath = r'E:\temp\data.txt'

data = []

with open(filepath) as file:

    for line in file:
        elements = line.rstrip('\n').split(':')
        d = {'type' : elements[0], 'actions' : elements[1]}
        data.append(d)

print(data)

data = sorted(data, key=lambda x: x['type'])

for key, elements in it.groupby(data, key=lambda  x: x['type']):
    print('The key is {} and the number of elements is {}'.format(key, len(list(elements))))
'''
print('-' * 30, '\n')

# ćwiczenia

import os
import itertools


def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


listing = scantree('E:/temp')
for l in listing:
    print('DIR' if l.is_dir() else 'FILE', l.path)

print('-'*30)

listing = scantree('E:/temp')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
