"""Четное или нечетное?
Создать переменную n, значение которой определяется через ввод данных с клавиатуры.
Если n является четным числом, то вывести на экран слово “четное”.
Если n является нечетным числом, то вывести на экран слово “нечетное”."""

n = int(input("Введите число: "))

if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")