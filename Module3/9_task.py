def create_square_dict():
    square_dict = {number: number ** 2 for number in range(1, 11)}
    return square_dict


square_dictionary = create_square_dict()
print(square_dictionary)
