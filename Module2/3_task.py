# натуральное число, которое в данной системе счисления равно сумме своих цифр, возведённых в степень, равную количеству его цифр.
# пример 153 = 1^3+5^3+3^3 = 153
def is_armstrong_number(number):
    if not isinstance(number, int):
        print("Ошибка! Не является числом!")
        return
    else:
        num_str = str(number)
        # вычисляем количество цифр в числе
        num_digits = len(num_str)
        # вычисляем сумму цифр, возведенных в степень
        digit_sum = sum(int(digit) ** num_digits for digit in num_str)
        # если сумма равна исходному числу, то это число Армстронга
        return digit_sum == number


try:
    number = int(input("Введите число: "))
except ValueError:
    number = ""

print(is_armstrong_number(number))
