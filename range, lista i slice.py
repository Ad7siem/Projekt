for i in range(10,0,-1):
    print(i)

list = list(range(10))
print('List',list,type(list), id(list))
list2 = list.copy()
print('List',list2,type(list2), id(list2))
list3 = list[:]
print('List',list3,type(list3), id(list3))

print(list[5:7])
print(list[5:])
print(list[:-1])
print(list[5:-3])
print(list[:8:2])
print(list[-1:0:-1])
print(list[-1::-1])
print(list[-1::-1])

# ćwiczenia


def NewCopyList(colors,n):
    return colors[:n]

colors = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']

for i in range(1,len(colors)+1):
    print(NewCopyList(colors,i))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(definition[definition.index('(')+1:definition.index(')')])