import copy

lst = []
#
# for i in range(101):
#     # if i % 6 == 0:
#     if i % 2 == 0 and i % 3 == 0:
#         lst.append(i)
# print(lst)
# #
# lst = [i for i in range(101) if i % 6 == 0]
# print(lst)
#
items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, True, None]
#
# lst = []
# count = 0
# for i in items:
#     if isinstance(i, (int, float)):
#         lst.append(i)
# for i in items:
#     if isinstance(i, (int, float)):
#         count += i
# print(sum(lst))
# print(count)
#
# for i in items:
#     if type(i) is int or type(i) is float:
#         lst.append(i)
# sum_num = sum(lst)
# print(f"{sum_num:.2f}")
#
# for i in items:
#     if type(i) in (int, float):
#         lst.append(i)
#
# print(sum(lst))
#
# print(type(5).__name__)
# break_word = "Пока"
# lst = []
# while True:
#     message = input()
#     if message == break_word:
#         print("Ну ладно, пока!")
#         lst.append(break_word)
#         print(lst)
#         break
#     lst.append(message)
#     if len(lst) > 4:
#         lst.pop(0)

# messages = []
# while True:
#     text = input('Enter text: ')
#     messages.append(text)
#     if len(messages) > 5:
#         messages.pop(0)
#     if text == 'See you':
#         print('Ok, see you!')
#         break
# print(messages)
#
# messages = []
# while True:
#     message = input("Введите сообщение: ").lower()
#     if message == "пока":
#         print("Ну ладно, пока!")
#         print(messages)
#         break
#     messages.append(message)
#     if len(messages) > 5:
#         messages.pop(0)

# ======================== SET Structure ==================================================

# set_ = {} # не верное создание сета
# set_ = set()
# set_.add(3)
# print(set_)
# set_.add(4)
# print(set_)
# set_.add(4)
# print(set_)

# lst = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# lst_check = []
# for i in lst:
#     if i not in lst_check:
#         lst_check.append(i)
# print(sorted(lst_check))
#
# set_list = set(lst)
# print(sorted(set_list))

# lst = [4,7,3,9,6,3,8]
# print(lst)
# lst_s = sorted(lst)
# lst_s.append((6, 5))
#
# print(lst)
# print(lst_s)
#
# lst_s.extend((6, 5))
# print(lst_s)

# lst.sort()
# print(lst)
#
# lst.reverse()
# lst_r = reversed(lst)

# ===================== DICT Structure ==================================================

from pprint import pprint
#
#
# products = {
#     "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#     "bread": {"quantity": 30, "price": 40}
# }
#
# for key, value in products.items():
#     value["price"] *= 1.2
# #
# # a = products.pop("milk")
# # print(a)
# # del products["milk"]
# #
# print(products)
# #
# products["salt"] = {"quantity": 7, "price": 12}
# products.setdefault("salt", {"quantity": 7, "price": 12})
# #
# pprint(products, indent=4)

# total_sum = 0
# for key, value in products.items():
#     total_sum += value["quantity"] * value["price"]
# print(total_sum)

# ===============================================================
#
from itertools import zip_longest

# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary', "jghgjhgj"]
#
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

# dct = dict(zip_longest(keys, values))
# # dct = dict(zip(keys, values))
# pprint(dct)

# dct = {}
# for i in range(len(keys)):
#     dct[keys[i]] = values[i]
#
#
# dct = {}
# for i in range(len(keys)):
#     dct.setdefault(keys[i], values[i])
#
# pprint(dct, indent=4)

# text = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# text = "зёхушж" #привет
#
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
# message = ""
# for key in text:
#     if key in cipher:
#         # print(f"key = {key}, value = {cipher[key]}")
#         message += cipher[key]
# print(message)
# #
# reverse_cipher = {value: key for key, value in cipher.items()}
# print("".join(reverse_cipher))
#
# # lst = ["g", "a", "m", "e"]
# # print("".join(lst))
# # #
# text1 = input("Введите текст: ").lower()
# message1 = ""
# for i in text1:
#     if i in reverse_cipher:
#         message1 += reverse_cipher[i]
# print(message1)

# dct = {}
# for key, value in cipher.items():
#     dct[value] = key
# print(dct)

# =====================================================

# dialog = """
# Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
# Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
# Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей
# сестры, и если ты все не исправишь, ты будешь следующим.
# Marty: Тяжелый случай.
# Doc: Вес тут совершенно ни при чем.
# """
# dct = {}
# # for i in dialog.lower():
# #     if i.isalpha():
# #         if i in dct:
# #             dct[i] += 1
# #         else:
# #             dct[i] = 1
# # pprint(dct, indent=4)
# #
#
# for i in dialog.lower():
#     if i.isalpha():
#         dct[i] = dct.get(i, 0) + 1
# print(dct)
# #
#
# char = None
# # print(len(char))
# max_count = 0
# for key, value in dct.items():
#     if value > max_count:
#         max_count = value
#         char = key
# print(char, max_count)

# ============== LIST structure =============================================

# lst = []
# lst2 = list()
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Hello", True, [1, 2, 3]]
# print(len(lst1))
# lst = [1, 2, 3]
# lst2 = [4, 5, 6]
# print(lst + lst2)
# print(lst * 3)
# print(3 in lst1)
# print("3" in lst1)
# lst = [4, 2, 7, 5, 1, 3, 6]
# print(min(lst))
# print(max(lst))
# print(sum(lst))
# sorted_list = sorted(lst)
# sort_list = lst.sort()
# lst.sort()
# print(lst)
# print(sorted_list)
# print(sort_list)
# print(lst.sort())

# num = "1 2 3 4 5 6 7 8 9 10"
# lst = num.split()
# lst1 = []
# for i in lst:
#     lst1.append(int(i))
# # lst1 = list(map(int, num.split()))
# lst1 = [int(i) for i in num.split()]
#
# print(lst1)
# print(min(lst1))
# print(max(lst1))
# print(sum(lst1))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[::2])
# print(lst[2:6])
# print(lst[::-1])
# # lst.reverse()
# print(lst)
# print(lst[len(lst) - 1])
# print(lst[-1])
# print(lst.index(7))
# print(lst[6])

# lst = [1, 2, 3, 3, 2, 5]
# lst.append(4)
# print(lst)

# lst.clear()
# print(lst)

# lst1 = lst.copy()
# lst2 = lst[:]

# count_value = lst.count(3)
# print(count_value)

# lst = [1, 2, 3, 3, 2, 5]
# lst2 = [10, 11]
# lst.extend(lst2)
# lst.append(lst2)
# print(lst)

# lst.insert(5, 100)
# print(lst)

# b = lst.pop()
# print(lst)
# print(b)

# lst.remove(2)
# print(lst)
# for i in lst2:
#     lst.append(i)
# print(lst)

# ================ TUPLE Structure ======================================

# tuple_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple_list1 = tuple()

# d = (10,)
# print(type(d))
#
# s = 1, 2, 3, 4, 5
# print(s)
# print(type(s))

# a = (1, 2, 3, [6, 7, 8])
# a[3][1] = 10
# print(a)

# a = (1, 2, 3, 6, 7, 8)
# a1 = list(a)
# a1.append(9)
# a = tuple(a1)
# print(a)
# dct = {
#     "key": "value"
# }

# ============ More methods example ===================

# dct1 = {}
# dct2 = dict(name="Vasya")
# print(dct2)

# dct = {
#     "name": {"Vasya": 10},
#     "age": 20,
#     "phone": 12352523,
#     "address": "Moscow"
# }
#
# for key in dct.keys():
#     print(key)
# print("-" * 20)
# for value in dct.values():
#     print(value)
# print("-" * 20)
# for key, value in dct.items():
#     print(key, value)

# keys = dct.keys()
# values = dct.values()
# items = dct.items()
# print(list(keys))
# print(set(keys))
# print(tuple(values))
# print(list(items))

# d = dct.popitem()
# print(d)
# print(dct)

# a = dct.pop("phone")
# print(a)
# print(dct)
# print(dct.setdefault("phone1", 694836983))
# print(dct)

# print(dct.get("phone1", "Not found"))
# print(dct.get("phone", "Not found"))

# print(len(dct))
# print("name" in dct)
# dct.clear()
# print(dct)

# a = dct["phone"]
# dct["last_name"] = "Pupkin"
# print(a)
# print(dct)
# dct["last_name"] = "Pushkin"
# print(dct)
#
# del dct["phone"]
# print(dct)

# =========== ============= ==========

# set_v = {[1, 2], 2, 4}
# print(set_v)

# set1 = {1, 2, 3}
# set2 = {2, 4, 5}
# set3 = set1.union(set2)
# print(set3)

# set1 = {1, 2, 3}
# set2 = {2, 4, 5}
# set3 = set1.intersection(set2)
# print(set3)
#
# set1 = {1, 2, 3}
# set2 = {2, 4, 5}
# set3 = set1.difference(set2)
# print(set3)
#
# set1 = {1, 2, 3}
# set2 = {2, 4, 5}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# =========== ============ ===============

# dct = {
#     "name": {"Vasya": 10},
#     "age": 20,
#     "phone": 12352523,
#     "address": "Moscow"
# }
# k = None
# for key, value in dct.items():
#     if value == 20:
#         k = key
#         break
# print(k)

# a = {1, 2}
# b = {3, 4}
# a.update(b)
# print(a)

# words = "a" * 10000
# print(words)

# ============== ENUMERATE =====================

# lst = [4, 7, 3, 5, 8, 9, 2, [5, 6]]
# [print(f'Index {i} : according to {v} value') for i, v in enumerate(lst)]


# lst_2 = lst.copy()
# lst_2[-1][0] = 9
# print(lst_2)
# print(lst)
#
# from copy import deepcopy
#
# lst_3 = copy.deepcopy(lst)
# lst_3[-1][0] = 0
# print(lst_3)
# print(lst)