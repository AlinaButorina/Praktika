def print_float_rounded_number(number):
    if isinstance(number, float):
        rounded_number = round(number, 2)
        print(f"{number} - {rounded_number:.2f}")
    else:
        print("Не является вещественным числом!")


try:
    number = float(input("Введите число: "))
    print_float_rounded_number(number)
except ValueError:
    print_float_rounded_number("")
