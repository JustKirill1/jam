from collections import Counter
def whatIsNumber(dolg):
    a = dict(Counter("{:,}".format(dolg)))
    if ',' in a:
        number = a[',']
    else:
        number = 1
    if 2 <= int(dolg / int(1000 ** number)) % 10 <= 4:
        if 10 <= int(dolg / int(1000 ** number)) % 100 <= 20:
            ending = 'ов'
        else:
            ending = 'а'
    elif 5 <= int(dolg / int(1000 ** number)) % 10 <= 9 or int(dolg / int(1000 ** number)) % 10 == 0:
        ending = 'ов'
    else:
        ending = ''
    if int(dolg / int(1000 ** number)) % 10 == 1:
        ending_1k = 'а'
    elif 2 <= int(dolg / int(1000 ** number)) % 10 <= 4:
        if 10 <= int(dolg / int(1000 ** number)) % 100 <= 20:
            ending_1k = ''
        else:
            ending_1k = 'и'
    elif 5 <= int(dolg / int(1000 ** number)) % 10 <= 9 or int(dolg / int(1000 ** number)) % 10 == 0:
        ending_1k = ''
    if 1 <= number < 2:
        b = str(int(dolg / int(1000 ** number))) + ' тысяч' + ending_1k
    if 2 <= number < 3:
        b = str(int(dolg / int(1000 ** number))) + ' миллион' + ending
    if 3 <= number < 4:
        b = str(int(dolg / int(1000 ** number))) + ' миллиард' + ending
    if 4 <= number < 5:
        b = str(int(dolg / int(1000 ** number))) + ' триллион' + ending
    if 5 <= number < 6:
        b = str(int(dolg / int(1000 ** number))) + ' квадриллион' + ending
    if 6 <= number < 7:
        b = str(int(dolg / int(1000 ** number))) + ' квинтилион' + ending
    if 7 <= number < 8:
        b = str(int(dolg / int(1000 ** number))) + ' секстилион' + ending
    if 8 <= number:
        b = str(int(dolg / int(1000 ** 8))) + ' септилион' + ending
    return b
def dayCounting(timeType, timeAmount):
    if timeType.value == 'Года':
        time_count = float(timeAmount.value) * 365.25
    if timeType.value == 'Месяцы':
        time_count = float(timeAmount.value) * 30.4375
    if timeType.value == 'Дни':
        time_count = float(timeAmount.value)
    return time_count