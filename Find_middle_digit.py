middle_digits = 0
input_digit = int(input('Enter input number '))
loop_input = input_digit
i = 0
while loop_input:
    loop_input //= 10
    i += 1
i = (i // 2) + 1
loop_input = input_digit
for j in range(i):
    middle_digits = loop_input % 10
    loop_input //= 10
print('input number ',input_digit)
print('middle digit of input',middle_digits)
