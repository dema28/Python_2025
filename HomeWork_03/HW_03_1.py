"""Какой сегодня день?
Создать переменную day, значение которой определяется через ввод данных с клавиатуры.
Если значение day равно “суббота” или “воскресенье”, то вывести на экран строку “Сегодня выходной!”.
Если значение day равно “среда”, то вывести на экран “Мне сегодня к стоматологу в 15:30”.
Во всех остальных случая выводить на экран “Сегодня обычный день.”."""

day = input("Введите день недели: ")

if day.lower() == "суббота" or day.lower() == "воскресенье":
    print("Сегодня выходной!")
elif day.lower() == "среда":
    print("Мне сегодня к стоматологу в 15:30")
else:
    print("Сегодня обычный день.")
