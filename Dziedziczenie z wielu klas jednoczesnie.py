class Car:

    def __init__(self, brand, model, isOnSale):
        print('>> Class Car - init - starting')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = '{} {}'.format(brand, model)
        print('>> Class Car - init - finishing')

    def GetInfo(self):
        print('>> Class Car - GetInfo - starting')
        super().GetInfo()
        print('{} {}'.format(self.brand, self.model).upper())
        print('IS ON SALE     -     {}'.format(self.isOnSale))
        print('>> Class Car - GetInfo - stopping')
        print('-' * 30)


class Specialist:

    def __init__(self, firstname, lastname, brand):
        print('>> Class Specialist - init - starting')
        self.firstname = firstname
        self.lastname = lastname
        self.name = '{} {}'.format(firstname, lastname)
        self.brand = brand
        print('>> Class SPecialist - init - finishing')

    def GetInfo(self):
        print('>> Class Specialist - Getinfo - starting')
        print('{} {} - ({})'.format(self.firstname, self.lastname, self.brand))
        print('>> Class Specialist - GetInfo - finishing')


class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print('>> Class CarSpecialist - init - starting')
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print('>> Class CarSpecialist - init - finishing')

    def GetInfo(self):
        print('>> Class CarSpecialist - GetInfo - Starting')
        super().GetInfo()
        print('>> Class CarSpecialist - GetInfo - finishing')


tom = CarSpecialist('Toyota', 'Corolla', True, 'Tom', 'Smith')
print(vars(tom))
tom.GetInfo()

print(CarSpecialist.__mro__)
print('-' * 30, '\n')

# ćwiczenia

from datetime import date
from datetime import timedelta


class Cake:
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


class Promo():

    def __init__(self, name, discount, start_date, end_date, minimal_order):
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake.show_info()

promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
print(promo10.full_name)
print('-'*50,'\n')


class PromoCake(Cake, Promo):

    def __init__(self, cake, promo):
        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)


promo_cake = PromoCake(cake, promo10)
promo_cake.show_info()
print(promo_cake.full_name)
print(PromoCake.__mro__)