number = 10
print('Vartable number:',number,id(number))
number += 2
print('Vartable number:',number,id(number))

text = 'Africa'
print('Vartable text',text,id(text))
text += 'is hot'
print('Vartable text',text,id(text))

list = [1,2,3]
print('Vartable list:',list,id(list))
list.append(4)
print('Vartable list:',list,id(list))

list2 = list
print('Vartable list:',list2,id(list2))
list2.append(5)
print('Vartable list:',list,id(list))
print('Vartable list:',list2,id(list2))

list3 = list.copy()
print('Vartable list:',list,id(list))
print('Vartable list:',list3,id(list3))
list3.append(6)
print('Vartable list:',list,id(list))
print('Vartable list:',list3,id(list3))
print('############################################','\n')

# ćwiczenia

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')
print(days,'\n',workdays)
