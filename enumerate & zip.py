workDays = [19,21,22,21,20,22]

print(workDays)
print(len(workDays))
print(workDays[2])

enumerateDays = list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print('Position', pos,'Value',value)

months = ['I','II','III','IV','V','VI']

monthsDays = list(zip(months,workDays))
print(monthsDays)

for m, d in monthsDays:
    print('Month',m,'days',d)

for pos,(m,d) in enumerate(zip(months,workDays)):
    print('Position',pos,'month',m,'days',d)

# ćwiczenia

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects,leaders):
    #print('Tle leader of "',p,'" is "',l,'"')
    print('Tle leader of "%s" is "%s"' % (p,l))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, d, l in zip(projects,dates,leaders):
    print('Tle leader of "%s" started %s is "%s"' % (p,d,l))

for pos,(p,d,l) in enumerate(zip(projects,dates,leaders)):
    print('{} - The leader of "{}" started {} is {}'.format(pos+1,p,d,l))