class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)

'''

def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])


print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01, car_02]

for i in cars:
    print('{} {} damaged - {}'.format(i['carBand'], i['carModel'], IsCarDamaged(i)))
print('-' * 30, '\n')
'''


# ćwiczenia

class Cake:
    def __init__(self, name, kind, taste, addictions, filing):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions.copy()
        self.filing = filing


cake_01 = Cake('Sernik', 'ciasto', 'ser tortowy', ['rodzynki', 'posypka'], '')
cake_02 = Cake('Zakonnica', 'ciasto', 'kako', ['polewa kakowa', 'gorzka czekolada'],
               'kieliszek rumu lub kieliszek wódki i kropleolejku migdałowego lub rumowego')
cake_03 = Cake('Galareciak', 'tort', 'galaretki', ['truskawki', 'banan', 'brzoskiwnia'], '')

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

print('Today in our offer:')
for cake in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {},filled with: {}'.format(cake.name, cake.kind, cake.taste,
                                                                                 cake.addictions, cake.filing))
