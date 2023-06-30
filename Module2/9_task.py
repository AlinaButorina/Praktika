def find_max_digit_position(n):
    n_str = str(n)
    max_digit = -1
    max_position = -1
    for i in range(len(n_str) - 1, -1, -1):
        digit = int(n_str[i])
        if digit > max_digit:
            max_digit = digit
            max_position = len(n_str) - i
    position_from_start = -1

    for i in range(len(n_str)):
        digit = int(n_str[i])
        if digit == max_digit and position_from_start == -1:
            position_from_start = i + 1

    return max_position, position_from_start


n = int(input("Введите натуральное число: "))
result = find_max_digit_position(n)
print(f"Порядковый номер максимальной цифры от конца числа: {result[0]}")
print(f"Порядковый номер максимальной цифры от начала числа: {result[1]}")
