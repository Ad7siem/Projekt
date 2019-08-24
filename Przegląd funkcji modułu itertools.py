import itertools
import operator
'''
# itertools.accumulate(iterable=[ ,func])

data = [1, 2, 3, 4, 5]

result = itertools.accumulate(data, operator.mul)   # accumulate jako pierwszy argument przyjmuje obiekt interable,
                                                    # drugi to funkcja ktora na tych obiektach nalezy wywolac . Operatory
                                                    # jakie mozna przekazac do funkcji sa wymienione w module operater
for each in result:
    print(each)

result = itertools.accumulate(data, max)
for each in result:
    print(each)

print('-' * 30)

for i in itertools.count(10, 3):    # count ma za zadanie generowac kolejne wartosci. Okreslamy od czego zaczac i o ile
                                    # powiekszac kolejne generowane wartosci
    print(i)
    if i > 20:
        break

print('-' * 30)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for m in itertools.cycle(months):   # cycle ma za zadanie przechodzic przez zbior danych przez obiekt iterable i
                                    # robic to w nieskonczonosc
    print(m)
    break

print('-' * 30)
color_basic = ['red', 'yellow', 'blue']
color_mix = ['green', 'orange', 'violet']
result = itertools.chain(color_basic, color_mix)  # chain ma za zadanie polaczyc ze soba dwa albo wiecej obiektow
# interable
for each in result:
    print(each)

print('-' * 30)

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)   # compress przyjmuje dwa argumenty. Pierwszym z nich jest obiekt z
                                                # danymi a drugi z nich zawiera wartosci True i False. Zadaniem
                                                # funkcji jest zwrocenie wylacznie tylko tych elementow z pierwszego argumentu ktore na pasujacych pozycjach w drugim
                                                # argumencie maja wartosc True
for each in result:
    print(each)

print('-'*30)

data = [1,2,3,4,5,6,7,8,9,10,1]
result = itertools.dropwhile(lambda x: x<5, data)   # drophwile nalezy opuszczac wartosci dopoki nie bedzie spelniony warunek. Argumenty to warunek i obiekt iterable
for each in result:
    print(each)

print('-'*30)

data = [1,2,3,4,5,6,7,8,9,10,1]
result = itertools.filterfalse(lambda x: x<5, data)  # bardzo podobny do dropwhile. opuszczamy wszystkie te ktore niespelniaja warunku
for each in result:
    print(each)

# nie chce mi sie dalej kodu pisac wiec pisze tylko funkcje

itertools.islice(months, 6, 8)  # bardzo podobna do zwyklego mechanizmu wyciagania pewnych wartosci z listy. ODwolujemy sie do listy i wybieramy ktore maja sie pojawic


itertools.product(spades, figures)  # iloczyn kartezjanski. Majac dwa zbiory laczymy biorac jedn obiekt z pierwszego zbioru i laczymy z reszta z drugiego zbioru

itertools.repeat('tell me more', 5)  # funkcja powtarzajaca, nieskonczenie jesli nie podamy w nawiasie ilosci razy powtorzen

data = [(1,2), (3,4)]
itertools.starmap(operator.add, data)  # nalezy wskazac na operator ktory ma byc zastosowany wzgledem przekazanych danych oraz obiekt iterable ktory musi byc zbudowany w specyficzny sposob. Operator add (dodawanie) pracuje na dwoch argumentach

itertools.takewhile(lambda x: x<5, data)  # pobiera element dopoki spelniany jest warunek. Na odwrot do dropwhile

cars = ['Ford', 'Opel', 'Skoda']
cars1, cars2 = itertools.tee(cars)  # typowy ulatwiacz zycia. Mozna utowrzyc pewna liczbe iteratorow nie bedace od siebie zalezne ale beda przechodzic przez jeden wspolny iterator

for each in cars1:
    print(each)
print('-'*10)
for each in cars2:
    print(each)


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free', 'free']
result = itertools.zip_longest(months, plan, fillvalue='unknown')  # laczenie dwoch list z rozna iloscia dlugosci.
for each in result:
    print(each)
    
# Obiekt islice jest stworzony w oparciu o generator.  Wiesz, że generatory często przypominają listy, a w listach można się odwoływać do podzbiorów za pomocą operacji cięcia (slice). Idea korzystania z operatora islice jest taka, że gerator wygeneruje liczby dopiero w momencie kiedy je wytniesz (operacja slice).  
'''

def get_factors(x):
    ret_list = []
    for i in range(1,x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print(get_factors(20))

candidate_list = list(range(1,10000))
filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))

for e in filtered_list:
    print('{} - {}'.format(e, get_factors(e)))