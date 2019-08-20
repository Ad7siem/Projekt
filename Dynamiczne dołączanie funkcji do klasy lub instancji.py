import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode='w')as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  # obiekt writer tworzony
        # o modul csv. Jest skojarzony z plikiem, okresla possczegolne wartosci rozdzielone przecinkiem,
        # jesli zawieraja przecinek maja byc w cudzyslowiu, Quote_Minimal jak mocno maja byc cytowane wszystkie
        # wartosci.umiescimy tylko te wartosci ktore w srodku zawieraja przecinek. Te bez przecinka beda bez
        # cudzyslowaia
        writer.writerow(header)
        writer.writerow(data)
    print('>>> This is function exportToFile - static method')


def exportToFile_Class(cls, path):
    with open(path, mode='w')as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>> This is function exportToFile - class method')


def exportToFile_Instance(self, path):
    with open(path, mode='w')as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('>>> This is function exportToFile - instance method')


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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'If set to true, the car is available in sale/promo')


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print('Static', '-----------' * 10)
Car.ExportToFile_Static = exportToFile_Static
# exportToFile_Static(r'E:\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'],
#                    [car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFile_Static(r'E:\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'],
                        [car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))

print('Class', '-----------' * 10)
# Car.ExportToFile_Class = exportToFile_Class
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)  # w ten sposob mozna przypisac zewnetrzna funkcje
# klasy. Za pomoca metody types
Car.ExportToFile_Class(path=r'E:\temp\export_Class.csv')
print(dir(Car))

print('Instance', '-----------' * 10)
# car_01.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r'E:\temp\export_instance.csv')
print(dir(car_01))

print('-' * 50, '\n')
if hasattr(car_01, 'ExportToFile_Static') and callable(
        car_01.ExportToFile_Static):  # jedna z metod sprawdzania czy istnieje metoda w klasie
    print('The object has method ExportToFile_Static')
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print('The object has method ExportToFile_Class')
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print('The object has method ExportToFile_Instance')
if hasattr(car_01, 'IsOnSale') and callable(car_01.IsOnSale):
    print('The object has method ExportToFile_Instance')
else:
    print('no such method')

print('-' * 30, '\n')


# Ćwiczenia

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_1_cake_to_html_Class(cls, path):
    template_header = """
<table border=1>"""
    template_data = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer = """</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)


def export_1_cake_to_html_Instance(self, path):
    template = """
    <table border=1>
         <tr>
           <th colspan=2>{}</th>
         </tr>
           <tr>
             <td>Kind</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Taste</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Additives</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Filling</td>
             <td>{}</td>
           </tr>
    </table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return __text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

print('Static', '-' * 50)
Cake.Export_1_cake_to_html = export_1_cake_to_html
Cake.Export_1_cake_to_html(cake01, r'E:\temp\export_1_cake_to_html_Static.html')

print('Class', '-' * 50)
Cake.Export_1_cake_to_html_Class = types.MethodType(export_1_cake_to_html_Class, Cake)
Cake.Export_1_cake_to_html_Class(path=r'E:\temp\export_1_cake_to_html_Class.html')

print('Instance', '-' * 50)
Cake.Export_1_cake_to_html_Instance = types.MethodType(export_1_cake_to_html_Instance, cake01)
Cake.Export_1_cake_to_html_Instance(path=r'E:\temp\export_1_cake_to_html_Instance.html')

for c in Cake.bakery_offer:
    c.export_1_cake_to_html_Instance = types.MethodType(export_1_cake_to_html_Instance, c)
for c in Cake.bakery_offer:
    c.export_1_cake_to_html_Instance(r'E:\temp\{}.html'.format(c.name.replace(' ', '_')))
