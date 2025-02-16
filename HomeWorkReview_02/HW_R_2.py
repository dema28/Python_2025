"""Необходимо получить слово, предложение и/или отрывок текста из консоли и присвоить их переменной/ым.
Произвести над ним действия и применить методы, изученные на уроках и самостоятельно.
Количество примененных методов и их тип зависят только от вашего воображения и изученного материала.
"""


# Получаем слово из консоли
word = input("Введите слово: ")

# Получаем предложение из консоли
sentence = input("Введите предложение: ")

# Получаем отрывок текста из консоли
paragraph = input("Введите отрывок текста: ")

# Приводим слово к нижнему регистру
lowercase_word = word.lower()

# Приводим предложение к нижнему регистру
lowercase_sentence = sentence.lower()

# Приводим отрывок текста к нижнему регистру
lowercase_paragraph = paragraph.lower()

# Переводим все буквы в слове в верхний регистр
uppercase_word = word.upper()

# Переводим все буквы в предложении в верхний регистр
uppercase_sentence = sentence.upper()

# Переводим все буквы в отрывке текста в верхний регистр
uppercase_paragraph = paragraph.upper()

# Преобразуем слово в верхний регистр и выводим
print(f"Приведенное слово в верхнем регистре: {uppercase_word}")

# Преобразуем предложение в верхний регистр и выводим
print(f"Приведенное предложение в верхнем регистре: {uppercase_sentence}")

# Преобразуем отрывок текста в верхний регистр и выводим
print(f"Приведенный отрывок текста в верхнем регистре: {uppercase_paragraph}")

# Переводим все буквы в слове в нижний регистр и выводим
print(f"Приведенное слово в нижнем регистре: {lowercase_word}")

# Переводим все буквы в предложении в нижний регистр и выводим
print(f"Приведенное предложение в нижнем регистре: {lowercase_sentence}")

# Переводим все буквы в отрывке текста в нижний регистр и выводим
print(f"Приведенный отрывок текста в нижнем регистре: {lowercase_paragraph}")

# Получаем первую букву слова
first_letter_of_word = word[0]

# Получаем последнюю букву слова
last_letter_of_word = word[-1]

# Получаем первые 3 буквы предложения
first_three_letters_of_sentence = sentence[:3]

# Получаем последние 3 буквы предложения
last_three_letters_of_sentence = sentence[-3:]

# Получаем первые 5 буквы отрывка текста
first_five_letters_of_paragraph = paragraph[:5]

# Получаем последние 5 буквы отрывка текста
last_five_letters_of_paragraph = paragraph[-5:]

# Выводим первую букву слова
print(f"Первая буква слова: {first_letter_of_word}")

# Выводим последнюю букву слова
print(f"Последняя буква слова: {last_letter_of_word}")

# Выводим первые 3 буквы предложения
print(f"Первые 3 буквы предложения: {first_three_letters_of_sentence}")
# Выводим последние 3 буквы предложения
print(f"Последние 3 буквы предложения: {last_three_letters_of_sentence}")

# Выводим первые 5 буквы отрывка текста
print(f"Первые 5 буквы отрывка текста: {first_five_letters_of_paragraph}")
# Выводим последние 5 буквы отрывка текста
print(f"Последние 5 буквы отрывка текста: {last_five_letters_of_paragraph}")

# Выводим длину слова
print(f"Длина слова: {len(word)}")

# Выводим длину предложения
print(f"Длина предложения: {len(sentence)}")


# Выводим длину отрывка текста
print(f"Длина отрывка текста: {len(paragraph)}")

# Выводим количество слов в предложении
print(f"Количество слов в предложении: {sentence.count(' ')+1}")

# Выводим количество гласных букв в слове
print(f"Количество гласных букв в слове: {sum(1 for letter in word if letter.lower() 
                                              in 'а, е, ё, и, о, у, ы, э, ю, я')}")

print(f"Количество согласных букв в слове: {sum(1 for letter in word if letter.lower() 
                                                in 'б, в, г, д, ж, з, л, м, н, р, п, ф, к, т, с, ш, х, ц, ч, щ')}")
