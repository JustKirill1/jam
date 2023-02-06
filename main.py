import flet as ft
import math
import fc
import os
import random
if __name__ == '__main__':

    def main(page: ft.Page):
        page.title = "Вычисление долга"
        debtValue = ft.TextField(hint_text='Какую сумму заняли?')
        percentageField = ft.TextField(hint_text='Под какой процент взяли?')
        timeType = ft.Dropdown(
            label='Дни, Месяцы, Года',
            width=100,
            options=[
                ft.dropdown.Option("Дни"),
                ft.dropdown.Option("Месяцы"),
                ft.dropdown.Option("Года"),
            ],
        )
        timeVariance = ft.Dropdown(
            label='Количество дней / От даты к дате',
            width=100,
            options=[
                ft.dropdown.Option("Количество дней"),
                ft.dropdown.Option("От даты к дате"),
            ],
        )

        timeAmmount = ft.TextField(hint_text='Введите количество')
        debtValue.value = 1500
        percentageField.value = 30
        timeVariance.value = "Количество дней"
        timeType.value = "Дни"

        #Создание текстовые поля
        def btn_click(e):
                m = 0
                userName = os.getlogin() #нахождение имени пользователя
                fc.getHistoryDB() #инициализация sql таблицы истории
                fc.getLoginDataDB()  #инициализация sql таблицы логинов
                historyData = fc.makeDictFromHistoryDB() #Создание словаря из sql таблицы
                randomFact = fc.randomFactsFromHistory(historyData) #отображение рандомной страницы из истории
                loginData = fc.makeDictFromLoginDataDB() #создание словаря из sql таблицы логинов
                phoneNumber, email = fc.getLoginsFromLoginDataDB(loginData) #нахождение номеров телефона и емейла в словаре логинов

                for sites in historyData:
                    if sites['visit_count'] > m:
                        m = sites['visit_count']
                for sites in historyData:
                    if sites['visit_count'] == m:
                        maxSite = f"You have most visits on {sites['title']}, you visited it {m} times"

                dV = debtValue.value
                time_count = fc.dayCounting(timeType, timeAmmount)  #Здесь вычисляется окличество дней
                percentage = float(percentageField.value) #Процент долга
                inflation = int(0.1198 / 365.25 * time_count * 10000) / 100  # Вычисление инфляции
                inflationPerDay = 0.1198 / 365.25 * time_count #Инфляция в день
                debt = int(dV * ((100 + percentage)/100) * 1.01 ** time_count + dV * ((100 + percentage)/100) * inflationPerDay)  # Вычисление долга с инфляцией
                debt_without_inflation = int(dV * ((100 + percentage) / 100) * 1.01 ** time_count)  # Вычисление долга без инфляции
                debtFormat = format(debt, ",") #форматиования долга с запятыми
                debtLog = int(math.log10(debt)) #нахождение степени десятки для упрощенного отображения больших чисел
                ezNumber = fc.whatIsNumber(debt) #нахождение названия числа

                page.clean() #Убираем старые поля
                Card = ft.Row(controls=[
                    ft.Column(controls=[
                    ft.Text(f"Привет {userName}, ваш дебитор должен вам:", size=30),
                    ft.Text(f"Дней с начала: {time_count}"),
                    ft.Text(f"Долг: {debtFormat} руб. ({ezNumber}, (~10^{debtLog})"),
                    ft.Text(f"Долг без инфляции: {debt_without_inflation}"),
                    ft.Text(f"Инфляция: {inflation}"),
                    ft.Text(f"{maxSite}"),
                    ft.Text(f"{randomFact}"),
                    ft.Text(f"One of your phone numbers is {phoneNumber}, and one of your emails is {email}"),
                    ft.FilledButton(text='Go back', on_click=go_back,width=400)])
                ], alignment = ft.MainAxisAlignment.CENTER)

                page.add(Card)
                #Добавляем текст и кнопку

        btn = ft.ElevatedButton(text="Готово", on_click=btn_click)
        #Это стартовая кнопка ибо её надо было определить


        def go_back(e):
            page.clean()
            create_start()
        #Кнопка назад

        def create_start():
            page.add(
                    ft.ListView(
                        [ft.Row(controls=[ft.Text("Введите данные",size=48)], alignment= ft.MainAxisAlignment.CENTER),
                        ft.Container(content=debtValue,width=800,padding=5),
                        ft.Container(percentageField,padding=5),
                        ft.Container(content=timeVariance,width=800,padding=5),
                        ft.Container(content=timeType,width=800,padding=5),
                        ft.Container(timeAmmount, padding=5),
                        ft.Container(btn,padding=2),

                         ],
                    )
        ) #Изначальное создание приложения
        create_start()

    ft.app(target=main) #Запуск говна