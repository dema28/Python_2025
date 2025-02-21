"""Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100 включительно,
которые делятся без остатка как на 2, так и на 3.
Выведите список numbers на экран.
"""

numbers = [num for num in range(101) if num % 2 == 0 and num % 3 == 0]
print(numbers)

# Вариант с использованием генератора списков
numbers = (num for num in range(101) if num % 2 == 0 and num % 3 == 0)
print(list(numbers))

# Вариант с использованием list comprehension и filter()
numbers = list(filter(lambda num: num % 2 == 0 and num % 3 == 0, range(101)))
print(numbers)

# Вариант с использованием list comprehension и map()
numbers = list(map(lambda num: num, filter(lambda num: num % 2 == 0 and num % 3 == 0, range(101))))
print(numbers)

# Вариант с использованием list comprehension и генераторы
numbers = [num for num in (num for num in range(101) if num % 2 == 0 and num % 3 == 0)]
print(numbers)

# Вариант с использованием list comprehension и генераторы с yield
numbers = (num for num in (num for num in range(101) if num % 2 == 0 and num % 3 == 0))
print(list(numbers))
