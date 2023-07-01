def find_palindromes(s):
    palindromes = []

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.append(substring)

    return palindromes


s = "ababa"
palindromes = find_palindromes(s)
print("Палиндромные подстроки строки", s, ":", palindromes)
