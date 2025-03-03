"""1
КаКоЕ-тО вОлНеНиЕ.

Создать переменную text, значение которой определяется через ввод данных с клавиатуры.
Каждый символ под четным индексом должен быть переведен в верхний регистр, а каждый нечетный в нижний.
Вывести полученную строку на экран.

Если была введена строка “Чтобы продать что-нибудь ненужное,
нужно сначала купить что-нибудь ненужное, а у нас денег нет.”,
то результат должен быть: “ЧтОбЫ ПрОдАтЬ ЧтО-НиБуДь нЕнУжНоЕ,
нУжНо сНаЧаЛа кУпИтЬ ЧтО-НиБуДь нЕнУжНоЕ, а у нАс дЕнЕг нЕт.”
"""

text = input("Введите текст: ")

result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].upper()
    else:
        result += text[i].lower()

print(result)

"""2
ОБРАТИТЕСЬ К СЛОВАМ.
Создать переменную text, значение которой определяется через ввод данных с клавиатуры."""

text = input("Введите текст: ")

words = text.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)

print(result)
