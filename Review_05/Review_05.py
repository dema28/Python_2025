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