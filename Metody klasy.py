class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -     {}'.format(self.isAirBagOK))
        print('Painting  - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic  - ok -     {}'.format(self.isMechanicOK))
        print('-' * 30)


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

car_01.GetInfo()
car_02.GetInfo()

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)

print('-' * 30, '\n')


# ćwiczenia

class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

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

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

cake_03.set_filling('krem waniliowy')
cake_01.add_additives(['czkolada','kokos'])

print('Today in our offer:')
for cake in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {},filled with: {}'.format(cake.name, cake.kind, cake.taste,
                                                                                 cake.additives, cake.filling))
    cake.show_info()