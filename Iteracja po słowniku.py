workDays = [19,21,22,21,20,22]
months = ['I','II','III','IV','V','VI']

monthsDays = dict(zip(months,workDays))
print(monthsDays)

for key in monthsDays:
    print('Key is',key,'value is',monthsDays[key])

for value in monthsDays.values():
    print('The value is:',value)

# ćwiczenia

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

for d in banknotes_coins:
    dict_denominations[d]=0

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[2] += 1

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for k in sorted(dict_denominations.keys()):
    print('Denominate: {0:6.2f} - amount {1:5}'.format(k,dict_denominations[k]))
