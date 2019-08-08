listA = list(range(6))
listB = list(range(6))

print(listA,listB)

product = []

for a in listA:
    for b in listB:
        product.append((a,b))

print(product)

product = [(a,b) for a in listA for b in listB]
print(product)

product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

product = {a:b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)

gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-'*30)

for x in gen:
    print(x)

print('-'*30)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all value have been generated')
        break

# ćwiczenia

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

i = 0
gen = ((s,m) for s in ports for m in ports)
for x in gen:
    print(x)
    i += 1
print(i)

i = 0
gen = ((s,m) for s in ports for m in ports if s != m)
for x in gen:
    print(x)
    i += 1
print(i)

i = 0
gen = ((s,m) for s in ports for m in ports if s < m)
for x in gen:
    print(x)
    i += 1
print(i)