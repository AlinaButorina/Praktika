def count_letters(string):
    letter_count = {letter: string.count(letter) for letter in string if letter.isalpha()}
    return letter_count


input_string = "Hello, World!"
letter_count_dict = count_letters(input_string)
print(letter_count_dict)
