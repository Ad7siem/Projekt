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

print('Status of cars:', car_01._Car__GetIsOnSale(), car_02._Car__GetIsOnSale()) # nie powinno się tak zmieniac wartosci zmiennych funkcji
'''
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())
'''
car_01.IsOnSale = True
car_02.IsOnSale = True
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)
