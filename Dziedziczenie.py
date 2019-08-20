brandOnSale = 'Opel'


class Car(object):
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        print('>> This is __init__ of parent class:', self.__class__.__name__)
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
        print('IS ON SALE     -     {}'.format(self.__isOnSale))
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


class Truck(Car):

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, IsOnSale, capacityKg):
        print('>> This is __init__ of child class:', self.__class__.__name__)
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK,
                         IsOnSale)  # w nawiasie mozna dopisac (Truck, self)
        # Car.__init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, IsOnSale)
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print('CapacityKg     -     {} \n'.format(self.capacityKg))


truck_01 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck_02 = Truck('Renault', 'Trafic', True, True, True, True, 1200)

print('Calling poperties')
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale, '\t-\t', truck_02.brand, truck_02.capacityKg,
      truck_02.IsOnSale)

truck_01.GetInfo()
truck_02.GetInfo()

print('-' * 30, '\n')


# ćwiczenia

class Cake(object):
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

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
                print("\t\t\t {}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print('Occasion:    {}'.format(self.occasion))
        print('Shape:       {}'.format(self.shape))
        print('Ornaments    {}'.format(self.ornaments))
        print('Text:        {}'.format(self.text))
        print('-' * 20)


birthday = SpecialCake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', 'birthday', 'standard',
                       'hearts', '15')
wedding = SpecialCake('Vanilla Cake', 'cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                      'weddinf', 'pyramid', 'pigeons', 'Patricia & Tom')

birthday.show_info()
wedding.show_info()

for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()