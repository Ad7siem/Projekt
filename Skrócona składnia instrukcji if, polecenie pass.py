dayType = 3

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = 'weekend' if dayType == 1 else '?'
print(dayDescription)

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)

# ćwiczenia

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus
print(price)

p = price - bonus if bonus_granted is True else price
print(p)

print('######################################################','\n')

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

r = 'very good' if rating == 5 else 'good' if rating == 4 else 'weak'
print(r)

print('########################################################','\n')

import datetime as dt

today_weekday = dt.date.today().strftime('%A')
print('Pomagam mamie' if today_weekday == 'Monday' else 'Mam w domu pranie' if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else 'Mam dyżur' if today_weekday == 'Tursday' else "Mam dwa zebrania" if today_weekday == 'Friday' else 'Ty w sobote nie mozesz bo na lekcje ganiasz' if today_weekday == 'Saturday' else 'Niedziela bedzie dla nas')
