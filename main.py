#Уровень B
import flet as ft

def main(page: ft.Page):

    page.title = "Пример счётчика в Flet"  # Устанавливаем заголовок страницы
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Выравниваем содержимое по вертикали по центру

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)  # Создаём текстовое поле для отображения числа

    def minus_click(e):  # Обработчик события нажатия на кнопку вычитания
        txt_number.value = str(int(txt_number.value) - 1)  # Уменьшаем значение в текстовом поле
        page.update()  # Обновляем страницу

    def plus_click(e):  # Обработчик события нажатия на кнопку прибавления
        txt_number.value = str(int(txt_number.value) + 1)  # Увеличиваем значение в текстовом поле
        page.update()  # Обновляем страницу

    def reset_click(e):  # Обработчик события нажатия на кнопку сброса
        txt_number.value = "0"  # Устанавливаем значение в текстовом поле равным 0
        page.update()  # Обновляем страницу

    def save_result(e):  # Обработчик события нажатия на кнопку сохранения
        result = txt_number.value  # Сохраняем значение в текстовом поле в переменную result
        filename = "result.txt"  # Имя файла для сохранения
        with open(filename, "w") as file:  # Открываем файл для записи
            file.write(result)  # Записываем значение в файл

    # Добавляем виджеты на страницу
    page.add(
        ft.Column(
            [

                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),  # Кнопка вычитания
                        txt_number,  # Текстовое поле
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),  # Кнопка прибавления
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Выравниваем элементы строки по центру
                ),

                ft.Row(
                    [
                        ft.IconButton("DELETE_FOREVER_ROUNDED", on_click=reset_click),  # Кнопка сброса
                        ft.IconButton("SAVE", on_click=save_result),  # Кнопка сохранения
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Выравниваем элементы строки по центру
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Выравниваем элементы столбца по центру
        )
    )

ft.app(main)