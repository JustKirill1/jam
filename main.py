import random

import flet as ft
import math
import fc
from datetime import date
import time
import os
import json

if __name__ == '__main__':
    stopLoop = 0
    def main(page: ft.Page):
        def debtCalculatorApp(e): #event for button to create app's page
            page.clean()
            page.title = "Вычисление долга"
            debtField = ft.TextField(label='Какую сумму заняли?')
            percentageField = ft.TextField(label='Под какой процент взяли?')
            timeType = ft.Dropdown(
                label='Дни, Месяцы, Года',
                width=100,
                options=[
                    ft.dropdown.Option("Дни"),
                    ft.dropdown.Option("Месяцы"),
                    ft.dropdown.Option("Года"),
                ],
            )

            timeAmmount = ft.TextField(hint_text='Введите количество')
            debtField.value = 1500
            percentageField.value = 30
            timeType.value = "Дни"

            #Создание текстовые поля

            def calculateDebt(e):
                    global randomUrl
                    m = 0
                    userName = os.getlogin() #нахождение имени пользователя
                    fc.getHistoryDB() #инициализация sql таблицы истории
                    fc.getLoginDataDB()  #инициализация sql таблицы логинов
                    historyData = fc.makeDictFromHistoryDB()  #Создание словаря из sql таблицы
                    randomFact, randomUrl = fc.randomFactsFromHistory(historyData) #отображение рандомной страницы из истории
                    loginData = fc.makeDictFromLoginDataDB() #создание словаря из sql таблицы логинов
                    phoneNumber, email = fc.getLoginsFromLoginDataDB(loginData) #нахождение номеров телефона и емейла в словаре логинов
                    try: #random things from browser's history data
                        for sites in historyData:
                            print(f"{sites['title']},{sites['visit_count']}")
                            if sites['visit_count'] > m:
                                m = sites['visit_count']
                        for sites in historyData:
                            if sites['visit_count'] == m:
                                maxSite = f"Вы посещали {sites['title']} чаще всего, а именно {m} раз"
                    except: #if nothing found - None
                        m = None
                        maxSite = None
                    debtValue = int(debtField.value)
                    dayAmount = fc.dayCounting(timeType, timeAmmount)  #Здесь вычисляется окличество дней
                    percentage = float(percentageField.value) #Процент долга
                    inflation = int(0.1198 / 365.25 * dayAmount * 10000) / 100  # Вычисление инфляции
                    inflationPerDay = 0.1198 / 365.25 * dayAmount #Инфляция в день
                    debt = int(debtValue * ((100 + percentage)/100) * 1.01 ** dayAmount + debtValue * ((100 + percentage)/100) * inflationPerDay)  # Вычисление долга с инфляцией
                    debtWithoutInflation = int(debtValue * ((100 + percentage) / 100) * 1.01 ** dayAmount)  # Вычисление долга без инфляции
                    debtWithoutInflationFormat = format(debtWithoutInflation, ",")
                    debtFormat = format(debt, ",") #форматиования долга с запятыми
                    debtLog = int(math.log10(debt)) #нахождение степени десятки для упрощенного отображения больших чисел
                    ezNumber = fc.whatIsNumber(debt) #нахождение названия числа

                    page.clean() #Убираем старые поля
                    Card = ft.Row(controls=[
                        ft.Column(controls=[
                        ft.Text(f"Привет {userName}, ваш дебитор должен вам:", size=30),
                        ft.Text(f"Дней с начала: {dayAmount}"),
                        ft.Text(f"Долг: {debtFormat} руб. ({ezNumber}, (~10^{debtLog})"),
                        ft.Text(f"Долг без инфляции: {debtWithoutInflationFormat} руб."),
                        ft.Text(f"Инфляция: {inflation}"),
                        ft.Text(f"{maxSite}"),
                        ft.Text(f"{randomFact} (UTC-0)"),
                        ft.Text(f"Один из ваших номеров телефона {phoneNumber}, и один из ваших е-мейлов {email}"),
                            ft.Image(
                                src="https://sun9-74.userapi.com/impg/F0G0xDCHnoLSWySFmUB62N-ef1QPWZ3q6LkaIA/43lWLgXZN0Y.jpg?size=1215x2160&quality=95&sign=f4e2490312579d8fe0788a6e05985e5f&type=album",
                                width=300,
                                height=300,
                                fit=ft.ImageFit.SCALE_DOWN,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                border_radius=ft.border_radius.all(10),
                            ),
                        ft.FilledButton(text='Проверить ссылку', on_click=seeTheLink, width=400),
                        ft.FilledButton(text='Назад', on_click=goBack,width=400)
                        ])

                    ], alignment = ft.MainAxisAlignment.CENTER)

                    page.add(Card)
                    #Добавляем текст и кнопку

            btnBack = ft.ElevatedButton(text="На главную", on_click=mainPage)
            btn = ft.ElevatedButton(text="Готово", on_click=calculateDebt)
            #Это стартовая кнопка ибо её надо было определить


            def goBack(e):
                page.clean()
                createStartPage()
            #Кнопка назад
            def seeTheLink(e):
                page.launch_url(randomUrl)
            def createStartPage():
                userName = os.getlogin()

                page.add(
                        ft.ListView(
                            [ft.Row(controls=[ft.Text(f"{userName}, введите данные",size=48)], alignment= ft.MainAxisAlignment.CENTER),
                            ft.Container(content=debtField,width=800,padding=5),
                            ft.Container(percentageField,padding=5),
                            ft.Container(content=timeType,width=800,padding=5),
                            ft.Container(timeAmmount, padding=5),
                            ft.Container(btn,padding=2),
                            ft.Container(btnBack, padding=2),

                             ],
                        )

            ) #Изначальное создание приложения
            createStartPage()
        def ageCalculatorApp(e):
            page.clean()
            userName = ft.TextField(label='ФИО')
            day = ft.TextField(label='День рождения')
            global row
            page.title = "Узнай свой возраст"
            day = ft.TextField(label='День рождения')
            month = ft.TextField(label='Месяц рождения')
            year = ft.TextField(label='Год рождения')
            country = ft.Dropdown(
                label='В какой стране живешь?',
                width=100,
                options=[
                    ft.dropdown.Option("Россия"),
                    ft.dropdown.Option("Другая"),
                ],
            )
            row = ft.Row(controls=(day, month, year))
            def goBack(e):
                global stopLoop
                page.clean()
                createStart()
                stopLoop = 1

            def checkUserData(e):
                page.clean()
                with open("userdata.txt", "r") as file:  # Открытие файла
                    userData = json.load(file)
                for key, users in userData.items():
                    for user in users:
                        if 'timeStamp' in user:
                            user['timeStamp'] = user['timeStamp']
                        else:
                            user['timeStamp'] = None
                        Card = ft.Row(controls=[
                            ft.Column(controls=[
                                ft.Text(f"{user['user']} has {user['luck']} luck and will live for {user['age']} years. Was created {user['timeStamp']}")
                            ])

                        ], alignment=ft.MainAxisAlignment.CENTER)
                        page.add(Card)
                button = ft.Row(controls=[
                    ft.Column(controls=[
                        ft.FilledButton(text='Назад', on_click=goBack, width=400)
                    ])

                ], alignment=ft.MainAxisAlignment.CENTER)
                page.add(button)
            btnCheckUD = ft.ElevatedButton(text="проверить UserData", on_click=checkUserData)
            def seeTopUnluck(e):
                page.clean()
                with open("userdata.txt", "r") as file:  # Открытие файла
                    userData = json.load(file)
                unsortedLuck = []
                sortedNameLuck = []
                for key, users in userData.items():
                    for user in users:
                        unsortedLuck.append(int(user['luck']))
                sortedLuck = sorted(unsortedLuck)
                for key, users in userData.items(): #не знаю насколько написанная мною сортировка оптимизирована но она работает
                    for a in range(0, len(sortedLuck)):
                        for user in users:
                            if int(user['luck']) == sortedLuck[a]:
                                sortedNameLuck.append({user['user']: sortedLuck[a]})
                Title = ft.Row(controls=[
                    ft.Column(controls=[
                        ft.Text(f"Самые неудачные пользователи:", size=30),
                    ])

                ], alignment=ft.MainAxisAlignment.CENTER)
                page.add(Title)
                for sortedUsers in sortedNameLuck:
                    for name, luck in sortedUsers.items():
                        Card = ft.Row(controls=[
                            ft.Column(controls=[
                                ft.Text(f"{sortedLuck.index(luck) + 1}. {name} с удачей {luck}")
                            ])

                        ], alignment=ft.MainAxisAlignment.CENTER)
                        page.add(Card)
                button = ft.Row(controls=[
                    ft.Column(controls=[
                        ft.FilledButton(text='Назад', on_click=goBack, width=400)
                    ])

                ], alignment=ft.MainAxisAlignment.CENTER)
                page.add(button)
            btnTop = ft.ElevatedButton(text="Увидеть топ", on_click=seeTopUnluck)
            def seeResult(e):
                global stopLoop
                stopLoop = None #variable to stop the loop
                page.clean()  # Убираем старые поля
                class User:
                    def __init__(self, user, luck, age, timeStamp):
                        self.user = user
                        self.luck = luck
                        self.age = age
                        self.timeStamp = timeStamp
                with open("userdata.txt", "r") as file: #Открытие файла
                    userData = json.load(file)
                check = None
                for key, users in userData.items():
                    for user in users:
                        if str(userName.value) in user.values(): # проверка если пользователь уже существует
                            checkedUser = user
                            check = True
                        elif check != True:
                            check = False
                if check == True:
                    randomLuck = checkedUser["luck"]
                    randomAge = checkedUser["age"]

                else: #if user does not exist creating variables for him
                    randomLuck = random.randint(1, 100) #finding luck
                    endOfRange = int(100 * (randomLuck / 100))
                    randomList = []
                    for i in range(1, 100):
                        a = random.randint(1, endOfRange)
                        randomList.append(a)
                    randomAge = str(random.choice(randomList)) #finding age
                    currentTime = time.strftime("%H:%M:%S")
                    tDate = str(date.today())
                    todaysDate = f"{tDate.rsplit('-')[-1]}-{tDate.rsplit('-')[-2]}-{tDate.rsplit('-')[-3]}" #better view of - date d-m-y instead of y-m-d
                    timeStamp = f"{currentTime} {todaysDate}"
                    userInit = User(userName.value, randomLuck, randomAge, timeStamp) #initialization of user
                    for key, values in userData.items():
                        values.append(userInit.__dict__)
                    with open("userdata.txt", "w") as file: #writing new user
                        json.dump(userData, file)

                if country.value == 'Другая':
                    dateOfDeath = 'в этом году'
                else:
                    dateOfDeath = "через " + randomAge + fc.ageEnding(randomAge)


                while stopLoop != 1: #dynamicly changing age

                    currentTime = time.strftime("%H:%M:%S")
                    hoursNow, minsNow, secsNow = currentTime.rsplit(":") #нахождение нынешних часов минут секунд
                    dateOfBirth = date(int(year.value), int(month.value), int(day.value))
                    dateToday = date.today()

                    daysAge = (dateToday - dateOfBirth).days + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)
                    monthsAge = daysAge / 30.4375  + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)/730.5
                    yearsAge = daysAge / 365.25 + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)/8766
                    thisYear = int(str(date.today()).rsplit('-')[0])
                    nextBD = date(thisYear+1, int(month.value), int(day.value))
                    daysTillNextBD = (nextBD - dateToday).days
                    hoursAge = daysAge * 24 + int(hoursNow)
                    minsAge = hoursAge * 60 + int(minsNow)
                    secsAge = minsAge * 60 + float(secsNow)
                    yearsEnding = fc.ageEnding(yearsAge)

                    Card = ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(f"Вам:", size=30),
                            ft.Text(f"{format(round(secsAge,0), ',')} {fc.secEnding(secsAge)}"),
                            ft.Text(f"{format(round(minsAge,2), ',')} {fc.minEnding(minsAge)}"),
                            ft.Text(f"{format(round(hoursAge,3), ',')} {fc.hourEnding(hoursAge)}"),
                            ft.Text(f"{format(round(daysAge,5), ',')} {fc.daysEnding(daysAge)}"),
                            ft.Text(f"{format(round(monthsAge,6), ',')} {fc.monthEnding(monthsAge)}"),
                            ft.Text(f"{format(round(yearsAge,7), ',')} {yearsEnding}"),
                            ft.Text(f"До следующего др {daysTillNextBD} дней"),
                            ft.Text(f"Вы умрете {dateOfDeath}"),
                            ft.Text(f"Ваша удача: {randomLuck}"),
                            ft.FilledButton(text='Назад', on_click=goBack, width=400)
                        ])

                    ], alignment=ft.MainAxisAlignment.CENTER)

                    page.add(Card)
                    time.sleep(1)
                    page.clean()
                page.clean() #after loop stopped come back to app's page
                createStart()
            btn = ft.ElevatedButton(text="Готово", on_click=seeResult)


            btnBack = ft.ElevatedButton(text="На главную", on_click=mainPage)

            def createStart():
                    page.add(
                        ft.ListView(
                            [
                                ft.Container(userName, padding=5),
                                ft.Container(country, padding=5),
                                ft.Container(content=row, width=800, padding=5),
                                ft.Container(btn, padding=2),
                                ft.Container(btnBack, padding=2),
                                ft.Container(btnTop, padding=2),
                                ft.Container(btnCheckUD, padding=2),

                            ],
                        )
                    )
            createStart()
        def EgeCalculatorApp(e): #event for button to create app's page
            page.clean()
            page.title = "Сколько осталось до ЕГЭ"
            egeSubject = ft.Dropdown(
                label='Какой предмет интересует',
                width=100,
                options=[
                    ft.dropdown.Option("География"),
                    ft.dropdown.Option("Литература"),
                    ft.dropdown.Option("Химия"),
                    ft.dropdown.Option("Русский язык"),
                    ft.dropdown.Option("Математика базовый уровень"),
                    ft.dropdown.Option("Математика профильный уровень"),
                    ft.dropdown.Option("История"),
                    ft.dropdown.Option("Физика"),
                    ft.dropdown.Option("Обществознание"),
                    ft.dropdown.Option("Биология"),
                    ft.dropdown.Option("Иностранные языки (Письменная часть)"),
                    ft.dropdown.Option("Иностранные языки (Устная часть)"),
                    ft.dropdown.Option("Информатика"),
                ],
            )
            #Создание текстовые поля

            def calculateDays(e):
                page.clean()  # Убираем старые поля
                print(egeSubject.value)
                if str(egeSubject.value) == 'География':
                    subjectWord = 'географии'
                    daysTillEge = (date(2023, 5, 26) - date.today()).days
                elif str(egeSubject.value) == 'Литература':
                    subjectWord = 'литературы'
                    daysTillEge = (date(2023, 5, 26) - date.today()).days
                elif str(egeSubject.value) == 'Химия':
                    subjectWord = 'химии'
                    daysTillEge = (date(2023, 5, 26) - date.today()).days
                elif str(egeSubject.value) == 'Русский язык':
                    subjectWord = 'русского языка'
                    daysTillEge = (date(2023, 5, 29) - date.today()).days
                elif str(egeSubject.value) == 'Математика базовый уровень':
                    subjectWord = 'математика базового уровня'
                    daysTillEge = (date(2023, 6, 1) - date.today()).days
                elif str(egeSubject.value) == 'Математика профильный уровень':
                    subjectWord = 'математики профильного уровня'
                    daysTillEge = (date(2023, 6, 1) - date.today()).days
                elif str(egeSubject.value) == 'История':
                    subjectWord = 'истории'
                    daysTillEge = (date(2023, 6, 5) - date.today()).days
                elif str(egeSubject.value) == 'Физика':
                    subjectWord = 'физики'
                    daysTillEge = (date(2023, 6, 5) - date.today()).days
                elif str(egeSubject.value) == 'Обществознание':
                    subjectWord = 'обществознанания'
                    daysTillEge = (date(2023, 6, 5) - date.today()).days
                elif str(egeSubject.value) == 'Биология':
                    subjectWord = 'биологии'
                    daysTillEge = (date(2023, 6, 13) - date.today()).days
                elif str(egeSubject.value) == 'Иностранные языки (Письменная часть)':
                    subjectWord = 'иностранных языков (Письменная часть)'
                    daysTillEge = (date(2023, 6, 13) - date.today()).days
                elif str(egeSubject.value) == 'Иностранные языки (Устная часть)':
                    subjectWord = 'иностранных языков (Устная часть)'
                    daysTillEge = (date(2023, 6, 16) - date.today()).days
                elif str(egeSubject.value) == 'Информатика':
                    subjectWord = 'информатики'
                    daysTillEge = (date(2023, 6, 19) - date.today()).days
                Card = ft.Row(controls=[
                    ft.Column(controls=[
                    ft.Text(f"До {subjectWord} {daysTillEge} {fc.daysEnding(daysTillEge)}", size=40),
                    ft.FilledButton(text='Назад', on_click=goBack,width=400)
                    ])

                ], alignment = ft.MainAxisAlignment.CENTER)
                page.add(Card)
            btnBack = ft.ElevatedButton(text="На главную", on_click=mainPage)
            btn = ft.ElevatedButton(text="Готово", on_click=calculateDays)
            #Это стартовая кнопка ибо её надо было определить


            def goBack(e):
                page.clean()
                createStartPage()
            #Кнопка назад

            def createStartPage():
                userName = os.getlogin()

                page.add(
                        ft.ListView(
                            [ft.Row(controls=[ft.Text(f"{userName}, введите данные",size=48)], alignment= ft.MainAxisAlignment.CENTER),
                            ft.Container(content=egeSubject,width=800,padding=5),
                            ft.Container(btn,padding=2),
                            ft.Container(btnBack, padding=2),

                             ],
                        )

            ) #Изначальное создание приложения
            createStartPage()
        def mainPage(e): #button event to come back to main page with buttons to other pages
            page.clean()
            page.title = "Главная страница"
            btnDebtCalc = ft.ElevatedButton(text="Debt calculator", on_click=debtCalculatorApp)
            btnAgeCalc = ft.ElevatedButton(text="Age calculator", on_click=ageCalculatorApp)
            btnEgeCalc = ft.ElevatedButton(text="Ege calculator", on_click=EgeCalculatorApp)
            page.add(
                ft.ListView(
                    [ft.Row(controls=[
                     ft.Container(btnDebtCalc, padding=2),
                     ft.Container(btnAgeCalc, padding=2),
                    ft.Container(btnEgeCalc, padding=2),
                     ])]))

        page.title = "Главная страница"
        btnFPage = ft.ElevatedButton(text="Debt calculator", on_click=debtCalculatorApp)
        btnSPage = ft.ElevatedButton(text="Age calculator", on_click=ageCalculatorApp)
        btnEgeCalc = ft.ElevatedButton(text="Ege calculator", on_click=EgeCalculatorApp)
        page.add(
            ft.ListView(
                [ft.Row(controls=[
                    ft.Container(btnFPage, padding=2),
                    ft.Container(btnSPage, padding=2),
                    ft.Container(btnEgeCalc, padding=2),
                ])]))
    ft.app(target=main) #Запуск говна