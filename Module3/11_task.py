def count_unique_letters(string):
    letter_count = {letter: string.lower().count(letter) for letter in string.lower() if letter.isalpha()}
    return letter_count


input_string = "Hello, World!"
result = count_unique_letters(input_string)
print(result)
