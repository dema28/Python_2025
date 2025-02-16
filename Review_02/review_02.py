import time
from time import ctime

# time.time
# time.ctime
# time.sleep

# print(time.time())
# print(type(time.time()))
# print(time.sleep(2))
# print(time.ctime())
# print(type(time.ctime()))

# num1 = 20
# print(num1)
#
# num2 = num1 + 10
# num1 = num1 + 10
#
# print(num1)
# print(num2)

# print(num3)

# False = 10
# class = "hello"
# def = 10

# a = 10
# print(type(a))
# b = "hello"
# print(type(b))

# a = input("Введите значение")
# print("*" * 10)
# print()
# print("*" * 10)

# num = input("Введите число: ")
# name = input("Введите имя : ")

# print(num)
# print(num, name)

# print(10, 20, 30, 40)
# print(10, 20, 30, 40, sep=' ')
# print("Hello", 2, 3, 4, sep='')
# print("Hello", "World", "!", sep=',')
# print("Hello", "World", "!", sep='*')
# print(1, 2, 3, 4, sep='###')

# print(10, 20, 30, 40)
# print(10, 20, 30, 40, end='\n')
# print("Hello", 2, 3, 4, end=' ')
# print("Hello", "World", "!", end=',')
# print("Hello", "World", "!", end='*')
# print(1, 2, 3, 4, end='###')

# num1 = 100
# num2 = 25
# num3 = 40

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 ** 2)
# print(num1 % num2)

# num1 = 100
# num2 = 25
# num3 = 25

# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num2)
# print(num1 != num2)
# print(num1 >= num2)
# print(num1 <= num2)

# num1 = num1 + num2
# num1 += num2
#
# num1 = num1 - num2
# num1 -= num2
#
# num1 = num1 * num2
# num1 *= num2
#
# num1 = num1 / num2
# num1 /= num2
#
# num1 = num1 // num2
# num1 //= num2
#
# num1 = num1 ** num2
# num1 **= num2
#
# num1 = num1 % num2
# num1 %= num2

# import math
# from math import trunc
# num1 = 10.5
num2 = 10.6

# print(math.trunc(num2))
# print(math.trunc(num1))
# print(trunc(num2))

# print(int(num1))
# print(int(num2))
#
# print(math.floor(num2))
# print(math.ceil(num2))
# print(round(num2))

# import math
# num1 = 10.5
# num2 = 10.6
# print(math.floor(num1))
# print(math.floor(num2))

# import math
# num1 = 10.5
# num2 = 10.6
# print(math.ceil(num1))
# print(math.ceil(num2))
# ===================================================
# name = "John"
# name = 'John'
# name = '''John'''
# name = """John"""
# print(name)

# name = "John"
# print("Hello " + name)

# name = "John"
# print(name * 2)

# name = "John"
# print(len(name))
# print(name[0])
# print(name[3])
# print(name[-2])

# name = "John"
# print("h" in name)
# print("h" not in name)
# print("a" in name)

# name = "John"
# name1 = "John"
# name2 = "john"
# print(name == name2) #J != j -> False
# print(name == name1) #J == J, o == o, h == h, n == n -> True
# print(ord(name1[0]))
# print(ord(name2[0]))

# name = "John"
# name1 = "John"
# name2 = "john"
# print(name < name2)
# print(name > name1)

# word = "Космонавт"
# print(word[0])
# print(word[4])
# print(word[-1])
# length = len(word)
# print(length)
# print(word[10])

# word = "Космонавт"
# print(word[0:3]) #Кос
# print(word[2:6]) #смон
# print(word[1:8]) #осмонав
# print(word[:4]) #Косм
# print(word[4:]) #онавт
#
# print(word[::2])
# print(word[1::2])
# print(word[::-1])
#===========================================
# word = "hello"
# print(word.count("l"))

# word = "hello"
# print(word.replace("l", "6"))

# word = "hello"
# print(word.upper())

# word = "HELLO"
# print(word.lower())

# word = "hello"
# word1 = "hello world"
# print(word.title())
# print(word1.title())

# word = "helLo"
# word1 = "hello World"
# print(word.capitalize())
# print(word1.capitalize())

# word = "HeLLo"
# print(word.swapcase())

# text = 'hello world'
# print(text.find("l"))
# print(text.find("l", 5))
# print(text.find("l", 5, 7))
#
# print("==========================")
#
# text = 'hello world'
# print(text.index("l"))
# print(text.index("l", 5))
# print(text.index("l", 5, 7))

# word = "hello"
# print(word.startswith("he"))
# print(word.startswith("lo"))

# word = "hello"
# print(word.endswith("he"))
# print(word.endswith("lo"))

# word = "hello"
# print(word.ljust(10))
# print(word.ljust(10, "*"))

# word = "hello"
# print(word.rjust(10))
# print(word.rjust(10, "*"))

# word = "hello"
# print(word.center(10))
# print(word.center(10, "*"))

# word = "hello"
# print(word.zfill(10))

# num = "123"
# print(num.zfill(5))

# word = "  hello  "
# print(word)
# print(word.strip())

# word1 = "\n\nhello\n\n"
# print(word1)
# print(word1.strip("\n"))

# word = "hello"
# print(word.strip("h"))

# word1 = "Hello"
# word2 = "Hello "

#===================================================================

# hello = "hello"
# world = "world"
# print(hello + " " + world)

# age = 10
# name = "Denis"
# print("Меня зовут " + name + " и мне " + str(age) + " лет.")

# age = 10
# name = "Denis"
# print("Меня зовут {} и мне {} лет.".format(name, age))
# print("Меня зовут {0} и мне {1} лет.".format(name, age))
# print("Меня зовут {1} и мне {0} лет.".format(age, name))
# print("Меня зовут {name} и мне {age} лет.".format(name=name, age=age))

# age = 10
# name = "Denis"
# print(f"Меня зовут {name} и мне {age} лет.")

#============================================

# a = 1/6
# b = 1/3
# c = 1/8
# d = 10
# print(a)
# print(b)
# print(c)
# print(d)
#
# print(f"{a:.2f}")
# print(f"{b:.2f}")
# print(f"{c:.2f}")
# print(f"{d:.2f}")

# a = 765525
# b = 123252
# print(f"{a:8d}")
# print(f"{b:10d}")
#
# print(f"{a:08d}")
# print(f"{b:010d}")

# print(f"{a:,d}")
# print(f"{a:_d}")

#========================================================

# word = "hello"
# print(word.islower())
# word = "Hello"
# print(word.islower())

# word = "HELLO"
# print(word.isupper())
# word = "Hello"
# print(word.isupper())

# word = "123"
# print(word.isdigit())
# word = "Hello"
# print(word.isdigit())

# word = "hello"
# print(word.isalpha())
# word = "123"
# print(word.isalpha())

# word = "hello123"
# print(word.isalnum())
# word = "123"
# print(word.isalnum())

# word = "Hello"
# print(word.istitle())
# word = "hello"
# print(word.istitle())

"""
Задача 1:
Необходимо ввести 2 числа из консоли, присвоив значения переменным.
Произвести вывод результатов всех произведенных математических действий в консоль.
Виды операций на Ваше усмотрение.
Вывод необходимо производить используя один из трех вариантов форматирования строк.
Пример получившегося вывода: "Результатом __операция__ над числами __а__ и __b__ будет __результат__"
(Подсказка: __х__ - необходимые значения)
(Пример вывода: "Результатом сложения над числами 3 и 5 будет 8")

Задача 2:
Необходимо получить слово, предложение и/или отрывок текста из консоли и присвоить их переменной/ым.
Произвести над ним действия и применить методы, изученные на уроках и самостоятельно.
Количество примененных методов и их тип зависят только от вашего воображения и изученного материала.
"""