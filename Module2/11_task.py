def sum_of_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a и b должны быть целыми числами")
    if a > b:
        raise ValueError("a должно быть меньше или равно b")
    total_sum = 0
    for i in range(a, b + 1):
        total_sum += i

    return total_sum


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = sum_of_integers(a, b)
print(f"Сумма всех целых чисел от {a} до {b} равна {result}")
