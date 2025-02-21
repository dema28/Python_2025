"""Alice.
Есть два списка одинаковой длины:
keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

Создайте словарь info из ключей keys и значений values. (Каждое значение занимает ту же позицию, что и ключ в другом списке)
Выведите словарь info на экран.
"""

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

info = {keys[i]: values[i] for i in range(len(keys))}
print(info)


