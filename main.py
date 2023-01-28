from collections import Counter
import flet as ft
import math

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

            хуй
            inflation = int(0.1198 / 365.25 * time_count * 10000) / 100  # Вычисление инфляции
            dolg = int(1500 * ((100 + inf)/100) * 1.01 ** time_count + 1500 * ((100 + inf)/100) * (
                        0.1198 / 365.25 * time_count))  # Вычисление долга с инфляцией
            dolgFormat = format(dolg, ",") #форматиования долга с запятыми
            dolgLog = int(math.log10(dolg)) #нахождение степени десятки для упрощенного отображения больших чисел

            dolg_without_inflation = int(1500 * ((100 + inf)/100) * 1.01 ** time_count)  # Вычисление долга
            a = dict(Counter("{:,}".format(dolg)))

            if ',' in a:
                    number = a[',']
            else: number = 1
            

            if 2 <= int(dolg / int(1000 ** number))%10 <= 4:
                if 10 <= int(dolg / int(1000 ** number))%100 <= 20:
                    ending = 'ов'
                else:
                    ending = 'а'
            elif 5 <= int(dolg / int(1000 ** number))%10 <= 9 or int(dolg / int(1000 ** number))%10 == 0:
                ending = 'ов'
            else:
                ending = ''
            if int(dolg / int(1000 ** number))%10 == 1:
                ending_1k='а'
            elif 2 <= int(dolg / int(1000 ** number))%10  <= 4:
                if 10 <= int(dolg / int(1000 ** number))%100 <= 20:
                    ending_1k = ''
                else:
                    ending_1k = 'и'
            elif 5 <= int(dolg / int(1000 ** number))%10  <= 9 or int(dolg / int(1000 ** number))%10 == 0:
                ending_1k = ''

            # нахождение окончаний

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

            # нахождение названия числа


            page.clean()
            #Убираем старые поля
            t1 = ft.Text(f"Дней с начала: {time_count}")
            t2 = ft.Text(f"Долг: {dolgFormat} руб. ({b}, (~10^{dolgLog})")
            t3 = ft.Text(f"Долг без инфляции: {dolg_without_inflation}")
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