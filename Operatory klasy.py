class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accessories = accessories

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -    {}'.format(self.isAirBagOK))
        print('Painting - ok -    {}'.format(self.isPaintingOK))
        print('Mechanic - ok -    {}'.format(self.isMechanicOK))
        print('Accessories        {}'.format(self.accessories))
        print('-' * 30)

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK, accessories)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __str__(self):
        return 'Brand: {} - Model: {}'.format(self.brand, self.model)


car_01 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
car_01.GetInfo()

car_01 += ['navigation', 'roof rack']
car_01.GetInfo()

car_01 += 'loudspeeker system'
car_01.GetInfo()

car_02 = Car('Opel', 'Corsa', True, False, True, [])

car_pack = car_01 + car_02
print('car_01+car_02=', car_pack[0].brand, car_pack[1].brand)
print(car_pack)

print(car_01)
print('-' * 30, '\n')


# ćwiczenia

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
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __iadd__(self, other):
        if type(other) is list:
            self.additives.extend(other)
            return self
        elif type(other) is str:
            self.additives.append(other)
            return self
        else:
            raise Exception('Adding type {} to Cake is not implemented'.format(type(other)))

    def __str__(self):
        return 'Kind {} - Name {} - additives {}'.format(self.kind, self.name, self.additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)

cake01 += 'cherry'
print(cake01)

cake01 += ['whipped cream', 'raspberry']
print(cake01)
