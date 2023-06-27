def greeting_message():
    try:
        name = input("Введите ваше имя: ")
        age = int(input("Введите ваш возраст: "))
        print(f"Привет, {name}! Тебе уже {age} лет.")
    except ValueError:
        print("Неправильные типы данных. Аргумент name должен быть строкой, а age - целым числом.")


greeting_message()
