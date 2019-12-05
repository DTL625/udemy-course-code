import datetime
t = datetime.time(5, 25, 1)
# print('t: ' + str(t))
# print('t\'s minutes: ' + str(t.minute))
# print('t\'s hour: ' + str(t.hour))
# print('t\'s max: ' + str(t.max))
# print('t\'s min: ' + str(t.min))

today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.year)

print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)

d1 = datetime.date(2019, 10, 11)
print('d1:', d1)


d2 = datetime.date(2015, 3, 11)
print('d2:', d2)

d3 = d1.replace(year=1989)
print('d3:', d3)

print('d1 - d2:', d1 - d2)