"""Составьте новый список numbers, который содержит только целые числа (int) и вещественные числа (float) из списка items.
Выведите на экран сумму чисел в numbers.
"""

items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = []

for item in items:
    if isinstance(item, (int, float)):
        numbers.append(item)

print(sum(numbers))


numbers = [item for item in items if isinstance(item, (int, float))]
print(sum(numbers))
