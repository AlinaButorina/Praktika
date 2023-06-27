def request_number():
    while True:
        try:
            number = int(input("Введите число от 10 до 20: "))
            if 10 <= number <= 20:
                print("Спасибо")
                break
            elif number < 10:
                print("Число меньше требуемого диапазона")
            else:
                print("Число больше требуемого диапазона")
        except ValueError:
            print("Не является числом. Пожалуйста, попробуйте еще раз.")


request_number()
