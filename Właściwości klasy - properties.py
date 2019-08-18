brandOnSale = 'Opel'


class Car:
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status InOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status InOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to time, the car is avaliable in sale/prowo')  #
    # funkcja przejmujaca kilka parametrow. (przy pomocy jakiej metody klasy pobieramy wartosc zmienna, jaka metoda
    # sluzy do zmiany wartosci, funkcja ktora moze usunac atrybut, definiuje dokumentacjie dla tej wlasciwosci (
    # opcjonalnie))


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print('Status of cars:', car_01._Car__GetIsOnSale(),
      car_02._Car__GetIsOnSale())  # nie powinno się tak zmieniac wartosci zmiennych funkcji
'''
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())
'''
car_01.IsOnSale = True
car_02.IsOnSale = True
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)


# ćwiczenia

class Cake:
    known_types = ['ciasto', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
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
        if kind == 'ciasto' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('Warunki zmiennej w {} niespełniają warunków'.format(name))

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('{}'.format(self.kind))
        print('{}'.format(self.taste))
        if len(self.additives) > 0:
            for a in self.additives:
                print('{}'.format(a))
        if len(self.filling) > 0:
            print('{}'.format(self.filling))
        print('Gluten free: {}'.format(self.__gluten_free))
        if len(self.__text) > 0:
            print('Text:    {}'.format(self.__text))
        print('-' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, addtitives):
        self.additives.extend(addtitives)

    def __get_text(self):
        return __text

    def __set_text(self, new_text):
        if self.kind == 'ciasto':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake_01 = Cake('Sernik', 'ciasto', 'ser tortowy', ['rodzynki', 'posypka'], '', False, 'Happy Birthday Margaret!')
cake_02 = Cake('Zakonnica', 'ciasto', 'kako', ['polewa kakowa', 'gorzka czekolada'],
               'kieliszek rumu lub kieliszek wódki i kropleolejku migdałowego lub rumowego', False, '')
cake_03 = Cake('Galareciak', 'tort', 'galaretki', ['truskawki', 'banan', 'brzoskiwnia'], '', False, '')
cake_04 = Cake('Wafel Kakaowy', 'wafel', 'kakao', [], 'kakao', False, '')

print('Today in our offer:')
for cake in Cake.bakery_offer:
    cake.show_info()

print('-' * 30)

cake_01.Text = 'Happy birthday!'
cake_02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()
