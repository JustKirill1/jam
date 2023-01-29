import flet as ft
import math
import fc

if __name__ == '__main__':
    def main(page: ft.Page):
        page.title = "Вычисление долга"
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

        time_ammount = ft.TextField(hint_text='Введите количество')

        #Создание текстовые поля
        def btn_click(e):

                time_count = fc.dayCounting(timeType, time_ammount)  #Здесь вычисляется окличество дней
                percentage = float(percentageField.value) #Процент долга
                inflation = int(0.1198 / 365.25 * time_count * 10000) / 100  # Вычисление инфляции
                inflationPerDay = 0.1198 / 365.25 * time_count #Инфляция в день
                debt = int(1500 * ((100 + percentage)/100) * 1.01 ** time_count + 1500 * ((100 + percentage)/100) * inflationPerDay)  # Вычисление долга с инфляцией
                debt_without_inflation = int(1500 * ((100 + percentage) / 100) * 1.01 ** time_count)  # Вычисление долга без инфляции
                debtFormat = format(debt, ",") #форматиования долга с запятыми
                debtLog = int(math.log10(debt)) #нахождение степени десятки для упрощенного отображения больших чисел
                ezNumber = fc.whatIsNumber(debt) #нахождение названия числа

                page.clean() #Убираем старые поля
                Card = ft.Row(controls=[
                    ft.Column(controls=[
                    ft.Text("Ваш дебитор должен вам:", size=30),
                    ft.Text(f"Дней с начала: {time_count}"),
                    ft.Text(f"Долг: {debtFormat} руб. ({ezNumber}, (~10^{debtLog})"),
                    ft.Text(f"Долг без инфляции: {debt_without_inflation}"),
                    ft.Text(f"Инфляция: {inflation}"),
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
                        ft.Container(percentageField,padding=5),
                        ft.Container(content=timeVariance,width=800,padding=5),
                        ft.Container(content=timeType,width=800,padding=5),
                        ft.Container(time_ammount, padding=5),
                        ft.Container(btn,padding=2),

                         ],
                    )
        ) #Изначальное создание приложения
        create_start()

    ft.app(target=main) #Запуск говна