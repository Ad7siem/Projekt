isOk = 'Python'
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = ''
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = 1
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = 0
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = [1,2,3]
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = []
print('Vartable isOk: ', isOk, type(isOk))
if isOk:
    print('TRUE')

# Jak widać zawsze gdy zmienna klasy str czy list jest pusta lub  w klasie int bedzie wartosc 0 to przyjmie w warunku wartosc logiczna False
# W przypadku gdy zmienne cos posiadaja lub sa wartosci innej niz 0 to przyjmie warunek True

listOfErrors = [100,101,102]
print('Vartable listOfErrors: ', listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0: # mozna takze zapisac if listOfErrors:
    print('TRUE')
print('#################################################','\n')

# ćwiczenia

def DisplayOptions(options):
    for i in range(len(opcions)):
        print('{} - {}'.format(i+1,opcions[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice

opcions = ['load data',1'export data','analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(opcions)

    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >= 0 and choice_num < len(opcions):
                print('you have selected {} - {}'.format(choice_num+1,opcions[choice_num]))
            else:
                print('choose a value from a list or press enter')
        except:
            print('You need to enter a number')
    else:
        print('-----END-----')
