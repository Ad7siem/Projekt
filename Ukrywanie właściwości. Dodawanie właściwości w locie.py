class Car:
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale  # dzieki __ atrybut zostal ukryty
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -     {}'.format(self.isAirBagOK))
        print('Painting  - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic  - ok -     {}'.format(self.isMechanicOK))
        print('IS ON SALE           {}'.format(self.__isOnSale))
        print('-' * 30)


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

car_02._Car__isOnSale = False
car_02.YearOfProduction = 2005  # dodawno nowy atrybut w klasie
del car_02.YearOfProduction  # usunieto

setattr(car_02,'TAXI',False)  # dedykowana metoda dodawania w locie atrybutu (obiekt modyfikacji, nazwa atrybutu, wartosc atrybutu
delattr(car_02,'TAXI')  # usuwanie atrybut
print(hasattr(car_02,'TAXI'))  # sprawdza czy obiekt posiada atrybut

car_02.GetInfo()
print(vars(car_02))

# ćwiczenia

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
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
        print('{}'.format(self.__gluten_free))
        print('-' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, addtitives):
        self.additives.extend(addtitives)


cake_01 = Cake('Sernik', 'ciasto', 'ser tortowy', ['rodzynki', 'posypka'], '', False)
cake_02 = Cake('Zakonnica', 'ciasto', 'kako', ['polewa kakowa', 'gorzka czekolada'],
               'kieliszek rumu lub kieliszek wódki i kropleolejku migdałowego lub rumowego', False)
cake_03 = Cake('Galareciak', 'tort', 'galaretki', ['truskawki', 'banan', 'brzoskiwnia'], '', False)
cake_04 = Cake('Wafel Kakaowy','wafel','kakao',[],'kakao', False)

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

cake_03.__gluten_free = True
print(dir(cake_03))
cake_03._Cake__gluten_free = True
cake_03.show_info()