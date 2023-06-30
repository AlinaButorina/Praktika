def first_natural_square(n):
    i = 1
    while i ** 2 <= n:
        i += 1
    return i


n = int(input("Введите число n: "))
result = first_natural_square(n)
print(f"Первое натуральное число, квадрат которого больше {n}, равно {result}")
