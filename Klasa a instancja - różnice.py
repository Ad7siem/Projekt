'''class Car:
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -     {}'.format(self.isAirBagOK))
        print('Painting  - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic  - ok -     {}'.format(self.isMechanicOK))
        print('-' * 30)


print('Class level variables BEPORE creating instances:', Car.numberOfCars, Car.listOfCars)

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print('Class level variables AFTER creating instances:', Car.numberOfCars, Car.listOfCars)

print('Id of class is:', id(Car))
print('Id of instances are:', id(car_01), id(car_02))

print('Check if object belomge to class:', isinstance(car_01, Car))  # sprawdza czy objekt należy do klasy
print('Check if object belomgs to class using type:',
      type(car_01) is Car)  # sprawdza czy objekt należcy do klasy za pomocą funkcji type
print('Check class of an object using __class__:',
      car_01.__class__)  # dzieki wlasciwosci __class__ dowiemy sie czy objekt nalezy do klasy. Ta wlasciwosc jest
# dostepna w kazdej instancji klasy i mowi jak obiekt powstal, do jakiej klasy nalezy

print('List of instance attributes with valume',
      vars(car_01))  # vars pozwala pokazac objekt od srodka w sposób słownika
print('List of class attributes with values:  ',
      vars(Car))  # vars w klasie zwraca informacje o tej klasie ale nie o instancjach klasy

print('List of instance attributes with values', dir(car_01))  # wykrywa metody ktore sa przed nami schowane
print('List of class attributes with values', dir(Car))

Car.numberOfCars = 123  # wada klasy to ze moge w kazdym momencie na sztywno zmienic wartosc danej

print('Value taken from instance:', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)

'''
# ćwiczenia

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('{}'.format(self.kind))
        print('{}'.format(self.taste))
        if len(self.additives) > 0:
            for a in self.additives:
                print('{}'.format(a))
        if len(self.filling) > 0:
            print('{}'.format(self.filling))
        print('-' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, addtitives):
        self.additives.extend(addtitives)


cake_01 = Cake('Sernik', 'ciasto', 'ser tortowy', ['rodzynki', 'posypka'], '')
cake_02 = Cake('Zakonnica', 'ciasto', 'kako', ['polewa kakowa', 'gorzka czekolada'],
               'kieliszek rumu lub kieliszek wódki i kropleolejku migdałowego lub rumowego')
cake_03 = Cake('Galareciak', 'tort', 'galaretki', ['truskawki', 'banan', 'brzoskiwnia'], '')
cake_04 = Cake('Wafel Kakaowy','wafel','kakao',[],'kakao')


cake_03.set_filling('krem waniliowy')
cake_01.add_additives(['czkolada', 'kokos'])

print('Today in our offer:')
for cake in Cake.bakery_offer:
    print('{} - ({}) main taste: {} with additives of {},filled with: {}'.format(cake.name, cake.kind, cake.taste,
                                                                                 cake.additives, cake.filling))
    cake.show_info()

    print('Czy obiekt: {} znajduje się w instancji: {}:'.format(cake.name,Cake.__name__),isinstance(cake_04,Cake),'\n')
    print('Czy obiekt: {} znajduje się w instancji: {}:'.format(cake.name, Cake.__name__), type(cake) is Cake, '\n')

print('-'*30)
print(vars(cake_01))
print(vars(Cake))
print(dir(cake_04))
print(dir(Cake))

