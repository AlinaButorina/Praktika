numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_list = lambda numbers: [x for x in numbers if x ** 0.5 % 1 == 0]
squares = squares_list(numbers)
print(squares)
