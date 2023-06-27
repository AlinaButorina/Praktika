def can_reach_destination(distance, fuel_efficiency, fuel_in_tank):
    # вычисляем количество топлива, необходимое для проезда заданного расстояния
    required_fuel = distance * fuel_efficiency / 100
    # если количество топлива в баке меньше, чем необходимо для проезда, то мы не доехали
    return fuel_in_tank >= required_fuel


# запрашиваем данные у пользователя
distance = float(input("Сколько километров хотите проехать? "))
fuel_efficiency = float(input("Сколько литров топлива расходует ваш автомобиль на 100 километров? "))
fuel_in_auto = float(input("Сколько литров топлива в вашем баке? "))

# определяем можно ли проехать заданное расстояние
if can_reach_destination(distance, fuel_efficiency, fuel_in_auto):
    print("Доезжаем!")
else:
    print("Не доехали!")
