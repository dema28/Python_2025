def add_into_list(lst = None):
    if lst is None:
        lst = []

    while True:
        value = input("Введите число (или 'q' для выхода): ")

        if value.lower() == 'q':
            break

        try:
            num = float(value)
            lst.append(num)
        except ValueError:
            print("Введено некорректное значение. Пожалуйста, введите число.")

add_into_list()
add_into_list([])
add_into_list([1, 2, 3])
add_into_list()

import random
import time
from pprint import pprint

# DRY -> don't repeat yourself

# def add_numbers(a, b):
#     return a + b
#
#
# num1 = int(input())
# num2 = int(input())
# sum_num = add_numbers(num1, num2)
# print(sum_num)


# def sum_ignore_non_numbers(items: list) -> int | float:
#     # lst = []
#     # for i in items:
#     #     if isinstance(i, (int, float)):
#     #         lst.append(i) # [1, 2, 4.3]
#     # print(*lst)
#     # return sum(lst)
#
#     # count = 0
#     # for i in items:
#     #     if isinstance(i, (int, float)):
#     #         count += i
#     # return count
#
#     return sum(i for i in items if isinstance(i, (int, float)))
#
# print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))


# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
# print(is_triangle(2, 4, 9))
# print(is_triangle(3, 4, 5))

# def sum_numbers(*args):
#     print(type(args))
#     return sum(*args)
#
#
# print(sum_numbers([4, 6, 8, 9, 9]))

# def concat_several_strings(**kwargs):
#     print(type(kwargs))
#     return " ".join([v for v in kwargs.values()])
#
#
# str1 = "Hello"
# str2 = "World"
# str3 = "New"
# str4 = "Year"
# str5 = "!"
# print(concat_several_strings(str1=str1, str2=str2, str3=str5))
# print(concat_several_strings(str1=str1, str2=str2))
# print(concat_several_strings(str1=str3, str2=str4, str3=str5))

# [] -> list
# () -> tuple
# {} -> dictionary
# set() -> set

# def average(*args):
#     if len(args) == 0:
#         return 0
#     lst = []
#     for i in args:
#         if isinstance(i, (int, float)):
#             lst.append(i)
#     # count = 0
#     # len_list = 0
#     # for i in args:
#     #     if isinstance(i, (int, float)):
#     #         count += i
#     #         len_list += 1
#     return sum(lst) / len(lst)
#     # return count / len_list
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, "Hello", None))

# def common_strings(list1, list2, ignore_case=True):
#     lst = []
#     if ignore_case:
#         for i in list1:
#             for j in list2:
#                 if i.lower() == j.lower():
#                     lst.append(i.lower())
#     else:
#         for i in list1:
#             for j in list2:
#                 if i == j:
#                     lst.append(i)
#     return lst
#
# fruits_1 = ["banana", "APPLE", "watermelon", "cherry"]
# fruits_2 = ["Mango", "apple", "orange", "cherry"]
#
# print(common_strings(fruits_1, fruits_2))
# print(common_strings(fruits_1, fruits_2, ignore_case=False))

# print(set(fruits_1).intersection(set(fruits_2)))
# print(set([i.lower() for i in fruits_1]).intersection(set([i.lower() for i in fruits_2])))

# def add_into_list(lst=None):
#     if lst is None:
#         lst = []
#
#     while str := input("Input any string: "):
#         if str == "stop": break
#         lst.append(str)
#     print(lst)
#
#
# add_into_list()
# add_into_list([3, 5, 7])
# add_into_list()

# def upper_lower(txt):
#     lst = []
#     for i in range(len(txt)):
#         if i % 2 == 0:
#             lst.append(txt[i].upper())
#         else:
#             lst.append(txt[i].lower())
#     return "".join(lst)
#
#     # txt1 = ""
#     # for i in range(len(txt)):
#     #     if i % 2 == 0:
#     #         txt1 += txt[i].upper()
#     #     else:
#     #         txt1 += txt[i].lower()
#     # return txt1
#
#
# txt = input()
# print(upper_lower(txt))

def sum_num(a: int, b: int) -> int:
    """
    Return sum of two numbers

    :param a: первое число, например: 1
    :param b: второе число, например: 2
    :return: сумма двух чисел, например: 3
    """
    return a + b


# a = int(random.random() * 100)
# b = random.randint(0, 100)
# print(a)
# print(b)
# print(sum_num(a, b))
# print("-" * 30)
# num = sum_num(a, b) * 10
# print(num)
# print(sum_num.__doc__)
# help(sum_num)
# print(sum_num(3, 6).__doc__)
#
# def sum_square(x, y):
#     return x**2 + y**2
#
# print(sum_square(3, 4))


# card = ("css selector", f"div[data-test='inventory-item']:nth-child(1)")

# def get_card(card_num):
#     return f"css selector", f"div[data-test='inventory-item']:nth-child({card_num})"
#
# def f():
#     return 1, 2, 3, 4
# print(f())
#
# print(get_card(1))
# a1, a2, *a3 = f()
# print(a1)
# print(a2)
# print(a3)
# print(a1)
# print(a2)
# print(a3)

# a = "/counterparties/"
# b = "/is_issues_certificates_only/"
#
#
# def cert_only(param):
#     return f"/counterparties/{param}/is_issues_certificates_only/"
#
#
# print(a + "3" + b)
# print(cert_only(3))

# def rec(s):
#     print(s)
#     s += 1
#     if s == 10:
#         return None
#     return rec(s)
#
#
# print(rec(1))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# print(fib(10))
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(10))

# def fac(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# print(fac(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# a = 2
# b = 3
# if a < b:
#     a, b = b, a
# print(a, b)
#


# def f():
#     s = "I love Python"
#     print(s)
#
#
# f()


# def f():
#     print(s)
#
#
# s = "I love learn Python"
# f()


# def f():
#     s = "I love Local Python"
#     print(s)
#
#
# s = "I love Global Python"
# f()
# print(s)

# def f():
#     local_var = "local var"
#     print(local_var)
#     print(f"Locals variables: {locals()}")
#     global s
#     print(f'First: {s}')
#     s = "Do you want to change Python language?"
#     print(f'Second: {s}')
#
#
# s = "Python is great!"
# f()
# print(s)
# pprint(f"Global variables: {globals()}")