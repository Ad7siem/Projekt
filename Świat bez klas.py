car_01 = {
    'carBand': 'Seat',
    'carModel': 'Ibiza',
    'carIsAirBagOK': True,
    'carIsPaintingOK': True,
    'carIsMechanicOK': True,
}
car_02 = {
    'carBand': 'Opel',
    'carModel': 'Corsa',
    'carIsAirBagOK': True,
    'carIsPaintingOK': False,
    'carIsMechanicOK': True,
}


def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])


print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01, car_02]

for i in cars:
    print('{} {} damaged - {}'.format(i['carBand'], i['carModel'], IsCarDamaged(i)))
print('-' * 30, '\n')
# ćwiczenia


cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7
}

cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}


def show_cake_info(aCake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight']))


cakes = [cake_01, cake_02]

for aCake in cakes:
    show_cake_info(aCake)


