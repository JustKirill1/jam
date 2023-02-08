import flet as ft
import math
import fc
import os
import random
if __name__ == '__main__':

    def main(page: ft.Page):
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
        def btnClick(e):
                global randomUrl
                m = 0
                userName = os.getlogin() #нахождение имени пользователя
                fc.getHistoryDB() #инициализация sql таблицы истории
                fc.getLoginDataDB()  #инициализация sql таблицы логинов
                historyData = fc.makeDictFromHistoryDB() #Создание словаря из sql таблицы
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
                    ft.FilledButton(text='Проверить ссылку', on_click=seeTheLink, width=400),
                    ft.FilledButton(text='Назад', on_click=goBack,width=400)
                    ])

                ], alignment = ft.MainAxisAlignment.CENTER)

                page.add(Card)
                #Добавляем текст и кнопку

        btn = ft.ElevatedButton(text="Готово", on_click=btnClick)
        #Это стартовая кнопка ибо её надо было определить


        def goBack(e):
            page.clean()
            createStart()
        #Кнопка назад
        def seeTheLink(e):
            page.launch_url(randomUrl)
        def createStart():
            userName = os.getlogin()
            page.add(
                    ft.ListView(
                        [ft.Row(controls=[ft.Text(f"{userName}, введите данные",size=48)], alignment= ft.MainAxisAlignment.CENTER),
                        ft.Container(content=debtField,width=800,padding=5),
                        ft.Container(percentageField,padding=5),
                        ft.Container(content=timeType,width=800,padding=5),
                        ft.Container(timeAmmount, padding=5),
                        ft.Container(btn,padding=2),

                         ],
                    )
        ) #Изначальное создание приложения
        createStart()

    ft.app(target=main) #Запуск говна