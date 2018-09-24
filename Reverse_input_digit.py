add_digits = 0
input_digit = int(input('Enter input number '))
while input_digit:
    add_digits = (add_digits * 10) + input_digit % 10
    input_digit //= 10
print(add_digits)
