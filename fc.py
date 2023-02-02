from collections import Counter
import datetime
import sqlite3 as sql
import datetime
import shutil
import os
import random
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
def getDays(dates):
    date1, date2 = dates.rsplit(";")
    return (date2 - date1).days
def dateFromWebkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta
def getHistoryDB():
    original = os.getenv('localappdata') + r'\Google\Chrome\User Data\Default\History'
    target = r'F:\pythonProject1\History.db'
    shutil.copy2(original, target)
def dictFactory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def makeDictFromDB():
    con = sql.connect("History.db")
    con.row_factory = dictFactory
    cur = con.cursor()
    cur.execute("select * from urls")
    var1 = cur.fetchmany(-1)
    return var1
def randomFactsFromHistory(var1):
    randomSite = random.choice(var1)
    randomFact = f"Last time you visited {randomSite['title']}, was {dateFromWebkit(randomSite['last_visit_time'])}"
    return randomFact

