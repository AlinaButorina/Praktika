def create_alphabet_dict():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {}

    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = i + 1

    return alphabet_dict


alphabet_dictionary = create_alphabet_dict()
print(alphabet_dictionary)
