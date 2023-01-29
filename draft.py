# Тут всякое говно можно удалять/изменять
import fc
import datetime
# a, b, c = '2024,01,01'.rsplit(',')
# print(a)
# print(b)
# print(c)
a,a1,a2 = input("первая дата").rsplit(",")
b,b1,b2 = input("вторая дата").rsplit(",")
c = fc.get_days(datetime.date(int(a), int(a1), int(a2)), datetime.date(int(b), int(b1), int(b2)))
print(c)
