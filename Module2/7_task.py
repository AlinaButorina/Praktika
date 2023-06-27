def sum_number():
    sum = 0
    while True:
        try:
            user_input = float(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите число!")
            continue
        num = int(user_input)
        if num >= 0:
            break
        sum += num
    print("Сумма чисел:", sum)


sum_number()
