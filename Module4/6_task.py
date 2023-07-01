def rot13_encode(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result += encoded_char
        else:
            result += char
    return result


string = "Hello, World!"
encoded_string = rot13_encode(string)
print(encoded_string)
