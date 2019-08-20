import random


class MemoryClass:
    list_of_already_selected_itemes = []

    def __init__(self, funct):
        # print('>> this is init od MemoryClass')
        self.funct = funct

    def __call__(self, list):
        # print('>> this is call of MemoryClass instance')
        items_nor_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_itemes]
        # print('+-- selecting only from a list of', items_nor_selected)
        item = self.funct(items_nor_selected)
        MemoryClass.list_of_already_selected_itemes.append(item)
        return item


cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porsche', 'Audi', 'VW', 'Mazda']


@MemoryClass
def SelectTodayPromation(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)


print('Promotion:', SelectTodayPromation(cars), '\n', '-' * 30)
print('Show:', SelectTodayShow(cars), '\n', '-' * 30)
print('Free accessories', SelectFreeAccessories(cars), '\n', '-' * 30)

print('\n')


# ćwiczenia

class NoDuplicates:

    def __init__(self, funct):
        self.funct = funct

    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            if not a in cake.additives:
                no_duplicate_list.append(a)
            self.funct(cake, no_duplicate_list)


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

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts'])
cake01.show_info()
