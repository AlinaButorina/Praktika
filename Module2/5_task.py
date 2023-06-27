import random

def play_game():
    wins = 0
    losses = 0
    consecutive_losses = 0
    while consecutive_losses < 3:
        user_choice = input("Выберите орла или решку (0 - орел, 1 - решка): ")
        if user_choice not in ["0", "1"]:
            break
        computer_choice = random.randint(0, 1)
        if int(user_choice) == computer_choice:
            print("Вы победили!")
            wins += 1
            consecutive_losses = 0
        else:
            print("Вы проиграли.")
            losses += 1
            consecutive_losses += 1
        print("Выигрыши: {}, проигрыши: {}".format(wins, losses))
    return wins, losses

# запуск игры
play_game()