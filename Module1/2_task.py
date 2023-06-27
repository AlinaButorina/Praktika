def get_fullname_length():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    full_name = f"{surname} {name}"
    full_name_length = len(full_name)
    print(f"Полное имя: {full_name}, длина строки (включая пробел между фамилией и именем): {full_name_length}")


get_fullname_length()
