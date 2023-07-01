def find_largest_number(number):
    digits = [int(d) for d in str(number)]
    sorted_digits = sorted(digits, reverse=True)
    largest_number = int(''.join(map(str, sorted_digits)))
    return largest_number


number = 12345
largest_number = find_largest_number(number)
print("Наибольшее число, полученное путем перестановки цифр числа", number, ":", largest_number)
