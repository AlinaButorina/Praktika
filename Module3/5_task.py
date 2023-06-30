def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


not_prime_numbers = [number for number in range(20) if not is_prime(number)]

print(not_prime_numbers)
