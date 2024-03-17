def converter(temp):
    celsius = (temp - 32) * (5/9)
    return celsius

n = [110, 2, 3, 4, 5, 6, 7, 8, 9]
converted_temps = list(map(converter, n))

print(converted_temps)