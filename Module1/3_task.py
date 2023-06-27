def compare_numbers():
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
        third_number = float(input("Введите третье число: "))
        max_number = max(first_number, second_number, third_number)
        print(f"Максимальное число: {max_number}")
        numbers = [first_number, second_number, third_number]
        numbers.sort(reverse=True)
        print(f"Числа по убыванию: {numbers}")
    except ValueError:
        print("Ошибка! Введено не число")

compare_numbers()
