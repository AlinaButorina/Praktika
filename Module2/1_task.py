import random


def guess_color():
    colors = ['красный', 'зеленый', 'синий', 'желтый', 'оранжевый']
    random_index = random.randint(0, len(colors) - 1)
    computer_color = colors[random_index]
    while True:
        print("Выберите цвет из списка: красный, зеленый, синий, желтый, оранжевый.")
        user_color = input("Введите название цвета: ")
        if user_color == computer_color:
            print("Отлично!")
            break
        else:
            print("К сожалению, вы не угадали.")
            print(f"Подсказка: загаданный цвет начинается на букву: {computer_color[0]}")
        while True:
            answer = input("Хотите попробовать еще раз? (да/нет): ")
            if answer.lower() == "да":
                break
            elif answer.lower() == "нет":
                return
            else:
                print("Введите ответ еще раз.")


guess_color()
