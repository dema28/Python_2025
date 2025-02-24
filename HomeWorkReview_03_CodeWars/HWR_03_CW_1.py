"""Дженни написала функцию, которая возвращает приветствие для пользователя.
Тем неменее, она влюблена в Джонни и хотела бы приветствовать его немного подругому.
Она добавила в свою функцию особый случай, но допустила ошибку."""

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Johnny"))
print(greet("Bob"))