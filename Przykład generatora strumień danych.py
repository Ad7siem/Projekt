# file = open(r'E:\temp\data.txt')

# data = file.read()

# file.close()

# for line in data.splitlines():
#    if line.startswith('ACTION'):
#        print(line)

# file = open(r'E:\temp\data.txt')

# for line in file:
#    if line.startswith('ACTION'):
#        print(line.replace('\n',''))

# file.close()


# file = open(r'E:\temp\data.txt')

# records = []

# for line in file:
#    if ':' in line:
#        type, action = line.rstrip('\n').split(':',1)
#        record = (type, action)
#        records.append(record)

# print(records)

# file.close()

def Get_Records(filePath):
    print('-= opening file =-')
    file = open(filePath)

    for line in file:
        if ':' in line:
            type, action = line.rstrip('\n').split(':', 1)
            record = (type, action)
            yield record

    print('-= closing file =-')
    file.close()


for record in Get_Records(r'E:\temp\data.txt'):
    print('The type is - {} - and the action is -{}'.format(record[0], record[1]))

print('-' * 30)
# ćwiczenia


import random


def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    numbers = list(range(number_of_values))
    while True:

        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 101)

        if sum(numbers) == asserted_sum:
            yield ((trial, numbers))
            trial = 0


for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)
