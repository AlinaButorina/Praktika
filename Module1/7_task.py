def reverse_case(text):
    new_str = ''
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                new_str += letter.lower()
            else:
                new_str += letter.upper()
        else:
            new_str += letter
    return new_str


word = input("Введите слово: ")
print(f"Резултат: {reverse_case(word)}")
