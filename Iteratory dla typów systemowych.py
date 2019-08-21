'''
aTuple = (1,2,3,4,5)

for x in aTuple:
    print(x)

#print(next(aTuple))
it = iter(aTuple)
print(next(it))
print(next(it))
print(next(it))
print('-'*30)
aList = [1,2,3,4,5]

for i in aList:
    print(i)

it = iter(aList)
print(next(it))
print(next(it))
print(next(it))
print('-'*30)
aSet = {1,2,(3,4), 'another element', 3,4}

for i in aSet:
    print(i)

it = iter(aSet)
print(next(it))
print(next(it))
print(next(it))
print('-'*30)

with open('E:/temp/lines.txt', 'r') as file:
    for line in file:
        print(line)

with open('E:/temp/lines.txt', 'r') as file:
    while True:
        try:
            print(next(file))
        except StopIteration:
            break
'''
# ćwiczenia

import csv

with open('E:/temp/export_Class.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    for row in csvreader:
#        print('|'.join(row))
    #print(next(csvfile))
    #print(next(csvfile))
    #print(next(csvfile))
    while True:
        try:
            print(next(csvfile))
        except StopIteration:
            break
