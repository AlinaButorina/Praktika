def create_vowel_consonant_dict(string):
    vowels = 'aeiou'
    result_dict = {}

    for letter in string:
        if letter.isalpha():
            if letter.lower() in vowels:
                result_dict[letter] = True
            else:
                result_dict[letter] = False

    return result_dict


input_string = "Hello, World!"
vowel_consonant_dict = create_vowel_consonant_dict(input_string)
print(vowel_consonant_dict)
