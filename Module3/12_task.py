def create_even_cubes_dict():
    return {num: num ** 3 for num in range(1, 11) if num % 2 == 0}


print(create_even_cubes_dict())
