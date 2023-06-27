def multiply_numbers():
    try:
        a = int(input("Введите первое число:"))
        b = int(input("Введите второе число:"))
        result = a * b
        print(f"Произведение чисел {a} и {b} равно {result}")
    except ValueError:
        print("Ошибка! Вводимые данные должны быть числами")


multiply_numbers()
