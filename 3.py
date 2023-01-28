from collections import Counter
percentage = float(input('Под какой процент взяли? (В десятичных!Например при 30% Писать: 0.3) '))

which_time_count = input('y - года, m - месяца, d - дни: ')
if which_time_count == 'y':
    time_count = float(input('Введите количество лет: '))*365.25
if which_time_count == 'm':
    time_count = float(input('Введите количество месяцев: ')) * 30.4375
if which_time_count == 'd':
    time_count = float(input('Введите количество дней: '))
inflation = int(0.1198/365.25*time_count*10000)/100 #Вычисление инфляции
dolg = int(1500*(1+percentage)*1.01**time_count+1500*(1+percentage)*(0.1198/365.25*time_count)) #Вычисление долга с инфляцией
dolg_without_inflation = int(1500*(1+percentage)*1.01**time_count) #Вычисление долга
a = dict(Counter("{:,}".format(dolg)))
if ',' in a:
    number = a[',']
else:
    number=1
if 1 <= number < 2:
    b = str(int(dolg/int(1000**number))) + ' тысяч'
if 2 <= number < 3:
    b = str(int(dolg/int(1000**number))) + ' миллионов'
if 3 <= number < 4:
    b = str(int(dolg/int(1000**number))) + ' миллиардов'
if 4 <= number < 5:
    b = str(int(dolg/int(1000**number))) + ' триллионов'
if 5 <= number < 6:
    b = str(int(dolg/int(1000**number))) + ' квадриллионов'
if 6 <= number < 7:
    b = str(int(dolg/int(1000**number))) + ' квинтилионов'
if 7 <= number < 8:
    b = str(int(dolg/int(1000**number))) + ' секстилионов'
if 8 <= number:
    b = str(int(dolg/int(1000**8))) + ' септилионов'

print('Дней с начала: ',int(time_count), '\nДолг:', "{:,}".format(dolg),'(', b,')',"руб."'\nДолг без инфляции: ',dolg_without_inflation,'руб.', '\nИнфляция: ', inflation, '(',dolg - dolg_without_inflation,'руб.)')