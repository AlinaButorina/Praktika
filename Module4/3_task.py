def find_prime_numbers(start, end):
    prime_numbers = []

    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, int(number / 2) + 1):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)

    return prime_numbers


start = 10
end = 90
prime_numbers = find_prime_numbers(start, end)
print("Простые числа в диапазоне от", start, "до", end, ":", prime_numbers)