# problem 1

import random
import string


def access_code_function(number_of_codes, length_of_code):
    letter = string.ascii_uppercase
    digit = string.digits
    codes = []

    for x in range(number_of_codes):
        code = (random.choice(letter)) + "".join(random.choice(digit) for y in range(length_of_code))
        codes.append(code)
    return codes


access_code = access_code_function(5, 5)
print(access_code)



