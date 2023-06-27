def capitalize_text(text):
    words = text.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result


word = input("Введите слово: ")
print(f"Резултат: {capitalize_text(word)}")
