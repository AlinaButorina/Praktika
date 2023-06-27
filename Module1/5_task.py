def football_result():
    try:
        points = int(input("Введите количество очков: "))
        if points == 3:
            print("Выигрыш")
        elif points == 1:
            print("Ничья")
        elif points == 0:
            print("Проигрыш")
        else:
            print("Неверное количество очков")
    except ValueError:
        print("Ошибка! Введено не число")


football_result()
