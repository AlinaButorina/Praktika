def create_tv_shows_list():
    tv_shows = ["Первая передача", "Вторая передача", "Третья передача", "Четвертая передача"]
    print(f"Список телевизионных передач: {tv_shows}")
    new_show = input("Введите название новой передачи: ")
    while True:
        try:
            position = int(input("Введите позицию, на которую нужно вставить новую передачу (от 1 до 5): "))

            if position < 1 or position > 5:
                print("Некорректная позиция!")
                continue

            tv_shows.insert(position - 1, new_show)
            print(f"Новый список телевизионных передач: {tv_shows}")
            return tv_shows

        except ValueError:
            print("Ошибка! Введено некорректное значение.")


create_tv_shows_list()
