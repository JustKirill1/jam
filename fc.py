from collections import Counter
import datetime
import sqlite3 as sql
import datetime
import shutil
import os
import random
def whatIsNumber(dolg):
    numbers = {'1': 'тысяч',
               '2': 'миллион',
               '3': 'миллиард',
               '4': 'триллион',
               '5': 'квадрилион',
               '6': 'квинтилион',
               '7': 'секстилион',
               '8': 'септилион',
               '9': 'октиллион',
               '10': 'нониллион',
               '11': 'дециллион',
               '12': 'ундециллион',
               '13': 'дуодециллион',
               '14': 'тредециллион',
               '15': 'кватуордециллион',
               '16': 'квиндециллион',
               '17': 'сексдециллион',
               '18': 'септендециллион',
               '19': 'октодециллион',
               '20': 'новемдециллион',
               '21': 'вигинтиллион',
               '22': 'унвигинтиллион',
               '23': 'дуовигинтиллион',
               '24': 'тревигинтиллион',
               '25': 'кватуорвигинтиллион',
               '26': 'квинвигинтиллион',
               '27': 'сексвигинтиллион',
               '28': 'септенвигинтиллион',
               '29': 'октовигинтиллион',
               '30': 'новемвигинтиллион',
               '31': 'тригинтиллион',
               '32': 'унтригинтиллион',
               '33': 'дуотригинтиллион',
               '34': 'третригинтиллион',
               '35': 'кватортригинтиллион',
               '36': 'квинтригинтиллион',
               '37': 'секстригинтиллион',
               '38': 'септентригинтиллион',
               '39': 'октотригинтиллион',
               '40': 'новемтригинтиллион',
               '41': 'квадрагинтиллион',
               '42': 'унквадрагинтиллион',
               '43': 'дуоквадрагинтиллион',
               '44': 'треквадрагинтиллион',
               '45': 'кваторквадрагинтиллион',
               '46': 'квинквадрагинтиллион',
               '47': 'сексквадрагинтиллион',
               '48': 'септенквадрагинтиллион',
               '49': 'октоквадрагинтиллион',
               '50': 'новемквадрагинтиллион',
               '51': 'квинквагинтиллион',
               '52': 'унквинкагинтиллион',
               '53': 'дуоквинкагинтиллион',
               '54': 'треквинкагинтиллион',
               '55': 'кваторквинкагинтиллион',
               '56': 'квинквинкагинтиллион',
               '57': 'сексквинкагинтиллион',
               '58': 'септенквинкагинтиллион',
               '59': 'октоквинкагинтиллион',
               '60': 'новемквинкагинтиллион',
               '61': 'сексагинтиллион',
               '62': 'унсексагинтиллион',
               '63': 'дуосексагинтиллион',
               '64': 'тресексагинтиллион',
               '65': 'кваторсексагинтиллион',
               '66': 'квинсексагинтиллион',
               '67': 'секссексагинтиллион',
               '68': 'септенсексагинтиллион',
               '69': 'октосексагинтиллион',
               '70': 'новемсексагинтиллион',
               '71': 'септагинтиллион',
               '72': 'унсептагинтиллион',
               '73': 'дуосептагинтиллион',
               '74': 'тресептагинтиллион',
               '75': 'кваторсептагинтиллион',
               '76': 'квинсептагинтиллион',
               '77': 'секссептагинтиллион',
               '78': 'септенсептагинтиллион',
               '79': 'октосептагинтиллион',
               '80': 'новемсептагинтиллион',
               '81': 'октогинтиллион',
               '82': 'уноктогинтиллион',
               '83': 'дуооктогинтиллион',
               '84': 'треоктогинтиллион',
               '85': 'кватороктогинтиллион',
               '86': 'квиноктогинтиллион',
               '87': 'сексоктогинтиллион',
               '88': 'септоктогинтиллион',
               '89': 'октооктогинтиллион',
               '90': 'новемоктогинтиллион',
               '91': 'нонагинтиллион',
               '92': 'уннонагинтиллион',
               '93': 'дуононагинтиллион',
               '94': 'тренонагинтиллион',
               '95': 'кваторнонагинтиллион',
               '96': 'квиннонагинтиллион',
               '97': 'секснонагинтиллион',
               '98': 'септеннонагинтиллион',
               '99': 'октононагинтиллион',
               '100': 'новемнонагинтиллион',
               '101': 'центиллион'}
    symbolAmount = dict(Counter("{:,}".format(dolg))) #считает сколько каких символов в dolg
    if ',' in symbolAmount:
        digitPlace = symbolAmount[','] #show how many commas in word
    else:
        digitPlace = 0
    if 2 <= int(dolg / int(1000 ** digitPlace)) % 10 <= 4: #get word ending
        if 10 <= int(dolg / int(1000 ** digitPlace)) % 100 <= 20:
            ending = 'ов'
        else:
            ending = 'а'
    elif 5 <= int(dolg / int(1000 ** digitPlace)) % 10 <= 9 or int(dolg / int(1000 ** digitPlace)) % 10 == 0:
        ending = 'ов'
    else:
        ending = ''
    if int(dolg / int(1000 ** digitPlace)) % 10 == 1:
        ending_1k = 'а'
    elif 2 <= int(dolg / int(1000 ** digitPlace)) % 10 <= 4:
        if 10 <= int(dolg / int(1000 ** digitPlace)) % 100 <= 20:
            ending_1k = ''
        else:
            ending_1k = 'и'
    elif 5 <= int(dolg / int(1000 ** digitPlace)) % 10 <= 9 or int(dolg / int(1000 ** digitPlace)) % 10 == 0:
        ending_1k = ''
    if digitPlace == 0:
        b = "< 1 тысячи"
    if digitPlace == 1:
        b = str(int(dolg / int(1000 ** digitPlace))) + ' тысяч' + ending_1k
    for digitPlace in range(2, 101):
        if 1000 ** digitPlace <= dolg < 1000 ** (digitPlace + 1):
            b = str(int(dolg / int(1000 ** digitPlace))) + ' ' + numbers[str(digitPlace)] + ending
            break

    return b
def dayCounting(timeType, timeAmount):
    if timeType.value == 'Года':
        timeAmount = float(timeAmount.value) * 365.25 #get days from years
    if timeType.value == 'Месяцы':
        timeAmount = float(timeAmount.value) * 30.4375 #get days from months
    if timeType.value == 'Дни':
        timeAmount = float(timeAmount.value)
    return timeAmount
def getDays(dates):
    date1, date2 = dates.rsplit(";")
    return (date2 - date1).days #get days from two dates
def dateFromWebkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta
def getHistoryDB():
    try:
        original = os.getenv('localappdata') + r'\Google\Chrome\User Data\Default\History'
        target = str(os.path.abspath(os.curdir)) + r'\History.db' #get history db from google chrome
        shutil.copy2(original, target)
    except:
        try:
            original = os.getenv('appdata') + r'\Opera Software\Opera GX Stable\History' #get history db from opera gx
            target = str(os.path.abspath(os.curdir)) + r'\History.db'
            shutil.copy2(original, target)
        except:
            print("Браузер не поддерживается")
def getLoginDataDB():
    try:
        original = os.getenv('localappdata') + r'\Google\Chrome\User Data\Default\Login Data' #get login db from google chrome
        target = str(os.path.abspath(os.curdir)) + r'\Login Data.db'
        shutil.copy2(original, target)
    except:
        try:
            original = os.getenv('appdata') + r'\Opera Software\Opera GX Stable\Login Data' #get login db from opera gx
            target = str(os.path.abspath(os.curdir)) + r'\Login Data.db'
            shutil.copy2(original, target)
        except:
            print("Браузер не поддерживается")
def dictFactory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def makeDictFromHistoryDB():
    try:
        con = sql.connect('History.db') #work with sql db
        con.row_factory = dictFactory
        cur = con.cursor()
        cur.execute("select * from urls")
        var1 = cur.fetchmany(-1)
    except:
        var1 = [None]

    return var1
def makeDictFromLoginDataDB():
    try:
        con = sql.connect('Login Data.db')
        con.row_factory = dictFactory
        cur = con.cursor()
        cur.execute("select * from logins")
        var1 = cur.fetchmany(-1)
    except:
        var1 = [None]
    return var1
def getLoginsFromLoginDataDB(logins):
    try:
        phoneNumber = []
        email = []
        for sites in logins:
            if '+7' in sites['username_value'] is not None: #find phone number
                phoneNumber.append(sites['username_value'])
            if '@' in sites['username_value'] is not None: #find email address
                email.append(sites['username_value'])
        return random.choice(phoneNumber), random.choice(email)
    except TypeError:
        phoneNumber, email = None, None
        return phoneNumber, email
def randomFactsFromHistory(var1):
    try:
        randomSite = random.choice(var1) #random choice of site from history
        randomFact = f"Last time you visited {randomSite['title']}, was {dateFromWebkit(randomSite['last_visit_time'])}"
        randomUrl = randomSite['url'] #get url of this random site
    except:
        randomFact = None
        randomUrl = None
    return randomFact, randomUrl
def minEnding(minutes): #get word ending for minutes
    if 2 <= int(minutes) % 10 <= 4:
        if 10 <= int(minutes) % 100 <= 20:
            ending = 'минут'
        else:
            ending = 'минуты'
    elif 5 <= int(minutes) % 10 <= 9 or int(minutes) % 10 == 0:
        ending = 'минут'
    else:
        if 10 <= int(minutes) % 100 <= 20:
            ending = 'минут'
        else:
            ending = 'минута'
    return ending
def secEnding(minutes): #get word ending for seconds
    if 2 <= int(minutes) % 10 <= 4:
        if 10 <= int(minutes) % 100 <= 20:
            ending = 'секунд'
        else:
            ending = 'секунды'
    elif 5 <= int(minutes) % 10 <= 9 or int(minutes) % 10 == 0:
        ending = 'секунд'
    else:
        if 10 <= int(minutes) % 100 <= 20:
            ending = 'секунд'
        else:
            ending = 'секунда'
    return ending
def hourEnding(hours): #get word ending for hours
    if 2 <= int(hours) % 10 <= 4:
        if 10 <= int(hours) % 100 <= 20:
            ending = 'часов'
        else:
            ending = 'часа'
    elif 5 <= int(hours) % 10 <= 9 or int(hours) % 10 == 0:
        ending = 'часов'
    else:
        if 10 <= int(hours) % 100 <= 20:
            ending = 'часов'
        else:
            ending = 'час'
    return ending
def daysEnding(days): #get word ending for days
    if 2 <= int(days) % 10 <= 4:
        if 10 <= int(days) % 100 <= 20:
            ending = 'дней'
        else:
            ending = 'дня'
    elif 5 <= int(days) % 10 <= 9 or int(days) % 10 == 0:
        ending = 'дней'
    else:
        if 10 <= int(days) % 100 <= 20:
            ending = 'дней'
        else:
            ending = 'день'
    return ending
def monthEnding(months): #get word ending for motnhs
    if 2 <= int(months) % 10 <= 4:
        if 10 <= int(months) % 100 <= 20:
            ending = 'месяцев'
        else:
            ending = 'месяца'
    elif 5 <= int(months) % 10 <= 9 or int(months) % 10 == 0:
        ending = 'месяцев'
    else:
        if 10 <= int(months) % 100 <= 20:
            ending = 'месяцев'
        else:
            ending = 'месяц'
    return ending


def ageEnding(randomAge): #get word ending for age
    b = []
    for i in str(int(randomAge)):
        b.append(i)
    if int(b[-1]) == 0 or 5 <= int(b[-1]) <= 9:
        ending = " лет"
    elif int(b[-1]) == 1:
        if str(b)[-2:] == 11:
            ending = " лет"
        else:
            ending = " год"
    else:
        ending = " года"
    return ending