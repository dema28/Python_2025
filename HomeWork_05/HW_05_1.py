"""Треугольник.
Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
Функция должна возвращать True, если треугольник с переданными сторонами может существовать,
и False в противном случае.
Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True."""

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(is_triangle(2, 4, 9))  # False
print(is_triangle(3, 4, 5))  # True
print(is_triangle(1, 2, 3))  # True
print(is_triangle(0, 4, 5))  # False
print(is_triangle(1, 1, 1))  # True
print(is_triangle(1, 1, 2))  # False
print(is_triangle(1, 2, 3))  # False


"""Определение площади треугольника.
Напишите функцию calculate_triangle_area(), которая имеет 3 параметра - длины сторон треугольника. 
Функция должна возвращать площадь треугольника с переданными сторонами.
Для calculate_triangle_area"""

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(calculate_triangle_area(2, 4, 9))  # 6.0
print(calculate_triangle_area(3, 4, 5))  # 6.0
print(calculate_triangle_area(1, 2, 3))  # 1.9843853481629193
print(calculate_triangle_area(0, 4, 5))  # 0.0
print(calculate_triangle_area(1, 1, 1))  # 0.4330127018922193
print(calculate_triangle_area(1, 1, 2))  # 0.0
print(calculate_triangle_area(1, 2, 3))  # 0.4330127018922193

