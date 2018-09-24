add_digits = 0
input_digit = int(input('Enter input number '))
while input_digit:
    add_digits += input_digit % 10
    input_digit //= 10
print('sum of digits from input', add_digits)
