import random

import flet as ft
import math
import fc
from datetime import date
import time
import os


if __name__ == '__main__':
    ending, randomLuck, randomAge = fc.deathLuck()
    def main(page: ft.Page):
        def firstApp(e):
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

            def btnClickMain(e):
                    global randomUrl
                    m = 0
                    userName = os.getlogin() #нахождение имени пользователя
                    fc.getHistoryDB() #инициализация sql таблицы истории
                    fc.getLoginDataDB()  #инициализация sql таблицы логинов
                    historyData = fc.makeDictFromHistoryDB()  #Создание словаря из sql таблицы
                    randomFact, randomUrl = fc.randomFactsFromHistory(historyData) #отображение рандомной страницы из истории
                    loginData = fc.makeDictFromLoginDataDB() #создание словаря из sql таблицы логинов
                    phoneNumber, email = fc.getLoginsFromLoginDataDB(loginData) #нахождение номеров телефона и емейла в словаре логинов
                    try:
                        for sites in historyData:
                            print(f"{sites['title']},{sites['visit_count']}")
                            if sites['visit_count'] > m:
                                m = sites['visit_count']
                        for sites in historyData:
                            if sites['visit_count'] == m:
                                maxSite = f"Вы посещали {sites['title']} чаще всего, а именно {m} раз"
                    except:
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
            btn = ft.ElevatedButton(text="Готово", on_click=btnClickMain)
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
        def secondApp(e):
            page.clean()
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

            def btnClick(e):
                page.clean()  # Убираем старые поля
                if country.value == 'Другая':
                    dateOfDeath = 'в этом году'
                else:
                    dateOfDeath = "через " + randomAge + ending

                currentTime = time.strftime("%H:%M:%S")
                hoursNow, minsNow, secsNow = currentTime.rsplit(":")

                dateOfBirth = date(int(year.value), int(month.value), int(day.value))
                dateToday = date.today()
                daysAge = (dateToday - dateOfBirth).days + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)
                monthsAge = daysAge / 30.4375  + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)/730.5
                yearsAge = daysAge / 365.25 + (int(hoursNow)/24 + int(minsNow)/1440 + int(secsNow)/86400)/8766


                hoursAge = daysAge * 24 + int(hoursNow)
                minsAge = hoursAge * 60 + int(minsNow)
                secsAge = minsAge * 60 + int(secsNow)

                Card = ft.Row(controls=[
                    ft.Column(controls=[
                        ft.Text(f"Вам:", size=30),
                        ft.Text(f"{secsAge} секунд"),
                        ft.Text(f"{minsAge} минут"),
                        ft.Text(f"{hoursAge} часов"),
                        ft.Text(f"{daysAge} дней"),
                        ft.Text(f"{monthsAge} месяцев"),
                        ft.Text(f"{yearsAge} лет"),
                        ft.Text(f"Вы умрете {dateOfDeath}"),
                        ft.FilledButton(text='Назад', on_click=goBack, width=400)
                    ])

                ], alignment=ft.MainAxisAlignment.CENTER)

                page.add(Card)
                # Добавляем текст и кнопку

            btn = ft.ElevatedButton(text="Готово", on_click=btnClick)

            # Это стартовая кнопка ибо её надо было определить

            def goBack(e):
                page.clean()
                createStart()

            # Кнопка назад
            btnBack = ft.ElevatedButton(text="На главную", on_click=mainPage)

            def createStart():
                page.add(
                    ft.ListView(
                        [
                            ft.Container(country, padding=5),
                            ft.Text(f"Ваша удача составляет: {randomLuck}"),
                            ft.Container(content=row, width=800, padding=5),
                            ft.Container(btn, padding=2),
                            ft.Container(btnBack, padding=2),

                        ],
                    )

                )  # Изначальное создание приложения

            createStart()

        def mainPage(e):
            page.clean()
            page.title = "Главная страница"
            btnFPage = ft.ElevatedButton(text="Debt calculator", on_click=firstApp)
            btnSPage = ft.ElevatedButton(text="Age calculator", on_click=secondApp)
            page.add(
                ft.ListView(
                    [ft.Row(controls=[
                     ft.Container(btnFPage, padding=2),
                     ft.Container(btnSPage, padding=2),
                     ])]))

        page.title = "Главная страница"
        btnFPage = ft.ElevatedButton(text="Debt calculator", on_click=firstApp)
        btnSPage = ft.ElevatedButton(text="Age calculator", on_click=secondApp)
        page.add(
            ft.ListView(
                [ft.Row(controls=[
                    ft.Container(btnFPage, padding=2),
                    ft.Container(btnSPage, padding=2),
                ])]))
    ft.app(target=main) #Запуск говна