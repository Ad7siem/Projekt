import datetime as dt


def MillionDays(year, month, day, maxdays):
    date = dt.date(year, month, day)

    for i in range(maxdays):
        yield date + dt.timedelta(days=i)  # funkcja yield ma za zadanie zwrocic wartosc i zamrozic funkcje


for d in MillionDays(2000, 1, 1, 3):
    print(d)

print('-' * 30)


def GetMagicNumbers():
    yield (22)
    yield (4)
    yield (5)


r = GetMagicNumbers()
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

for m in r:
    print(m)

print('-' * 30)


# ćwiczenia

def Combinations(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield ("{} - {} -{}".format(i, j, k))

    current_customer += 1


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for c in Combinations(products, promotions, customers):
    print(c)
