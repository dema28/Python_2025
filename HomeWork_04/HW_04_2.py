"""Создать список messages, который будет хранить “сообщения”.
Программа должна в бесконечном цикле запрашивать у пользователя ввести сообщение (строку) с клавиатуры и сохранять
ее в список messages. Причем программа должна запоминать не более 5 последних сообщений. То есть,
если длина списка messages превысила 5, то первое сообщение в нем должно быть удалено.
Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно, пока!” и список последних сообщения на экран.
"""

messages = []

while True:
    user_input = input("Введите сообщение (или 'Пока' для выхода): ")

    if user_input.lower() == "пока":
        print("Ну ладно, пока!")
        break

    messages.append(user_input)

    if len(messages) > 5:
        messages.pop(0)

    print("Последние сообщения:", messages)

