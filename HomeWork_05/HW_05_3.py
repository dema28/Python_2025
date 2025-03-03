"""Общие строки.
Напишите функцию common_strings(), которая имеет 3 параметра:
list1, list2 и ingore_case=True (значение по умолчанию).
Функция должна вернуть новых список из тех значений, которые встречаются в обоих списках.
При этом, если ignore_case равен True, то функция должна игнорировать регистр и считать строки “string” и “STRING” одинаковыми.  В противном случае функция должна учитывать регистр символов и считать такие строки разными.
Все строки в результирующем списке должны быть в нижнем регистре.
Например, существуют 2 списка:
fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].
"""

def common_strings(list1, list2, ignore_case=True):
    common_strings = []
    for string1 in list1:
        for string2 in list2:
            if ignore_case:
                string1 = string1.lower()
                string2 = string2.lower()
            if string1 == string2:
                common_strings.append(string1)
                break
    return common_strings

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
print(common_strings(fruits_1, fruits_2))  # Output: ['apple', 'cherry']

fruits_1 = ['banana', 'APPLE', 'Watermelon', 'cherry']
fruits_2 = ['mango', 'APPLE', 'orange', 'CHERRY']
print(common_strings(fruits_1, fruits_2))  # Output: ['apple', 'cherry']

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['mango', 'apple', 'orange', 'CHERRY', 'grape']
print(common_strings(fruits_1, fruits_2))  # Output: ['apple', 'cherry']