numbers = list(range(101))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


palindromes = list(filter(is_palindrome, numbers))

print(palindromes)
