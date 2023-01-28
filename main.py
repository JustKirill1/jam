from collections import Counter
import flet as ft
import math
import fc
if __name__ == '__main__':
    def main(page: ft.Page):
        perc = ft.TextField(hint_text='Под какой процент взяли?')
        time_type = ft.Dropdown(
            label='Дни, Месяцы, Года',
            width=100,
            options=[
                ft.dropdown.Option("Дни"),
                ft.dropdown.Option("Месяцы"),
                ft.dropdown.Option("Года"),
            ],
        )
        time_ammount = ft.TextField(hint_text='Введите количество')
        #Создаю текстовые поля
        def btn_click(e):
                inf = int(perc.value)
                if time_type.value == 'Года':
                    time_count = float(time_ammount.value) * 365.25
                if time_type.value == 'Месяцы':
                    time_count = float(time_ammount.value) * 30.4375
                if time_type.value == 'Дни':
                    time_count = float(time_ammount.value)

                #Здесь вычисляется окличество дней

                inflation = int(0.1198 / 365.25 * time_count * 10000) / 100  # Вычисление инфляции
                debt = int(1500 * ((100 + inf)/100) * 1.01 ** time_count + 1500 * ((100 + inf)/100) * (
                            0.1198 / 365.25 * time_count))  # Вычисление долга с инфляцией
                debtFormat = format(debt, ",") #форматиования долга с запятыми
                debtLog = int(math.log10(debt)) #нахождение степени десятки для упрощенного отображения больших чисел
                debt_without_inflation = int(1500 * ((100 + inf)/100) * 1.01 ** time_count)  # Вычисление долга
                ezNumber = fc.whatIsNumber(debt) #нахождение названия числа

                page.clean()
                #Убираем старые поля
                t1 = ft.Text(f"Дней с начала: {time_count}")
                t2 = ft.Text(f"Долг: {debtFormat} руб. ({ezNumber}, (~10^{debtLog})")
                t3 = ft.Text(f"Долг без инфляции: {debt_without_inflation}")
                t4 = ft.Text(f"Инфляция: {inflation}")
                page.add(t1,t2,t3,t4)
                page.add(ft.ElevatedButton(text='Go back', on_click=go_back))
                #Добавляем текст и кнопку
        btn = ft.ElevatedButton(text="Готово", on_click=btn_click)
        #Это стартовая кнопка ибо её надо было определить


        def go_back(e):
            page.clean()
            page.add(perc, time_type, time_ammount, btn)
        #Кнопка назад


        page.add(perc, time_type,time_ammount, btn)
        #Изначальное создание приложения

    ft.app(target=main)
#Запуск говна