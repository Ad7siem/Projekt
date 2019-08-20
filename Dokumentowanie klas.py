brandOnSale = 'Opel'


class Car:
    '''
    Car - class operating on cars available in the dealer
    '''

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        '''
            init - arguments accepted
            brand - the brand of the car is Fiat
            model - the model of the car is Multipla
            isAirBagOk - is the AirBag not used
            isPaintingOK - is the car paint original/no corrections
            isMechanicOK - is the car free of any mechanics failure
            isOnSale - is the car covered by extra promotion (some additional conditions apply)
        '''
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintigOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        '''IsOnSale - the car is on extra promotion that is limited in time (only selected cars may be "On Sale\")'''
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarrTitle(self):
        return 'Brand: {}, Model: {}'.format(self.brand, self.model).title()


car_01 = Car('Seat', 'Ibiza', True, True, True, False)

help(Car)
help(Car.IsOnSale)


print('-'*30)

# ćwiczenia

class Cake:
    bakery_offer = []

    '''
    Cake - Oto klasa operacji w dziedzinie wypieków cukierniczych
    '''

    def __init__(self, name, kind, taste, additives, filling):
        '''
        name: nazwa ciasta
        kind: glowny skladnik
        taste: juz nie pamietam :P
        additives: dodatki do ciasta
        filling: posmak
        '''
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        '''Piekna ozdoba nazwy produktu cuekirniczego'''
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
help(Cake.full_name)