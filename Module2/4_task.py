import math


def solve_quadratic_equation(a, b, c):
    # вычисляем дискриминант
    D = b ** 2 - 4 * a * c
    # если D меньше нуля, то корней нет
    if D < 0:
        return None
    # если D равен нулю, то имеется один корень
    elif D == 0:
        x = -b / (2 * a)
        return x,
    # если D больше нуля, то имеется два корня
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return x1, x2


# чтение коэффициентов уравнения с клавиатуры
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# решение уравнения
solution = solve_quadratic_equation(a, b, c)

# вывод результата (если корни есть)
if solution is None:
    print("Уравнение не имеет корней")
elif len(solution) == 1:
    print("Уравнение имеет один корень: x =", solution[0])
else:
    print("Уравнение имеет два корня: x1 =", solution[0], "x2 =", solution[1])
