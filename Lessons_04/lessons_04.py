# items = [1, 2, 3, "ABC", True, 3.14, [1, 2, 3]]
#
# print(items)

# numbers = [45, 3, 1, 0, 5]

# print(numbers)
# print(numbers[0])
# print(numbers[2])

# del numbers[1]

# numbers[3] = 222

# for item in numbers:
#     print(item)

# print(numbers[-2])

# numbers = [45, 6, 7, 1, 0, 2]
#
# numbers.clear() # []
# numbers.append("ABC")
# numbers.append(True)
# numbers.insert(0, False)
#
# elem = numbers[1]
#
# print(elem)
# print(numbers)
#
# sorted_numbers = sorted(numbers)
# len_numbers = len(numbers)
# sum_numbers = sum(numbers)
# min_numbers = min(numbers)
# max_numbers = max(numbers)
#
# print(min_numbers, max_numbers)

# words = ["ABC", "DDD", "AAA", 100]
#
# print(min(words))

# items = [1, 56, 7, 2, [1, 2, 3], "ABC", 1]
# numbers = []

# 1, True, "ABC" - True, [1, 2, 3]
# 0, "", False, None, []
#
# for i in range(100):
#     if i % 2:
#         numbers.append(i)
#
# print(numbers)

# 123 - int, "ABC" - str, True - bool, 3.14 - float, [] - list

# for item in items:
#     if isinstance(item, int):
#         numbers.append(item)
#
# print(numbers)

#
# numbers = []
#
# for i in range(1000):
#     if i % 2:
#         numbers.append(i)
#
# print(numbers)
#
# numbers_2 = [i for i in range(1000) if i % 2]
#
# print(numbers_2)

# a = 1
# b = a # 1
# b += 1
#
# print(a, b)

# numbers = [1, 2, 3]
# # numbers2 = numbers.copy()
# numbers2 = list(numbers)
# numbers2.append(4)
#
# print(numbers, numbers2)

# list_numbers = [5, 5, 5]
# numbers = (1, 2, 3, 4)
#
# print(tuple(list_numbers))


# data = {"names": ["Oksana", "Mike"], "age": 29, "phone": "+4833333321"}
#
# data["name"] = "Mike"
# del data["name"]
#
# print(data)
# data["names"] = None
# names = data["names"] # ["Oksana", "Mike"]
#
# print(names[0])
# print(data["names"][0])

# values_data = data.values() # ['Oksana', 'Mike'], 29, ...
# info_data = data.items()

# a, b = (1, 2)
#
# print(a, b)

# for key, value in data.items():
#     print(key, value)

# data = [{"name": "Oksana", "age": 29}, {"name": "Mike", "age": 15}, {"name": "Slava", "age": 30}]
# find_name = input("Введите имя, которое хотите найти: ")
# value = int(input("Введите возраст, который хотите задать"))
#
# for info in data:
#     if info["name"] == find_name:
#         info["age"] = value
#         print(info)

# name = input()
# age = int(input())
#
# data.append({"name": name, "age": age})
#
# print(data)


