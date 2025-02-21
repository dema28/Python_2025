"""Магазин.
Есть словарь с товарами:
products = {
     "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk":{"quantity": 12, "price": 90},
     "bread": {"quantity": 30, "price": 40}
}
Необходимо увеличить цену всех продуктов на 20 процентов.
Удалить товар “milk”.
Добавить товар “Salt” с количеством 7 и ценой 12.
Вывести общую стоимость всех товаров в магазине.
Ответ: 6516.0
"""

products = {
     "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk":{"quantity": 12, "price": 90},
     "bread": {"quantity": 30, "price": 40}
}

# Увеличение цены всех продуктов на 20 процентов
for product, data in products.items():
    data["price"] *= 1.20
    print(f"цена продукта {product} увеличена на 20%: {data['price']}")


# Удаление товара "milk"
del products["milk"]
print(f"Товар 'milk' удален.")


# Добавление товара "Salt" с количеством 7 и ценой 12
products["salt"] = {"quantity": 7, "price": 12}
print(f"Товар 'salt' добавлен.")


# Вывод общей стоимости всех товаров в магазине
total_price = sum(data["price"] * data["quantity"] for data in products.values())
print(f"Общая стоимость всех товаров в магазине: {total_price}")