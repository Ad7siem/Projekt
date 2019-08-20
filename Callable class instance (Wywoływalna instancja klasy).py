'''
class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)


mem = MemoryClass([])
print('List of items in memory', mem.list_of_items)

mem.list_of_items.append('buy sugar')
print('List of items in memory', mem.list_of_items)

mem('buy milk')
print('List of items in memory', mem.list_of_items)

mem('buy coffee')
print('List of items in memory', mem.list_of_items)

print('This class is callable:', callable(MemoryClass))
print('This class is callable:', callable(mem))
'''


# ćwiczenia

class NoDuplicates:

    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for a in new_items:
            if not a in self.list:
                self.list.append(a)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)
