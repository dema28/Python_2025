"""Создать переменную n, значение которой определяется через ввод данных с клавиатуры (целое число).
Создать переменную text, значение которой определяется через ввод данных с клавиатуры (строка).
Программа должна вывести вашу строку text на экран n-раз. Если вы ввели 3, а затем “Ау”, то результат должен быть:
Ау
Ау
Ау """



n = int(input("Введите целое число: "))
text = input("Введите текст: ")

for i in range(n):
    print(text)



