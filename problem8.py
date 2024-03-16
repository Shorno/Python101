celsius_temp = [0, 10, 20, 30, 40, 50]


def convert_fahrenheit_temp(temp):
    fahrenheit_temp = (temp * (9 / 5)) + 32
    return fahrenheit_temp


temp_in_fahrenheit = list(map(convert_fahrenheit_temp, celsius_temp))
print(temp_in_fahrenheit)