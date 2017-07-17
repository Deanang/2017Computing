import sys
input_str = input("Enter an integer: ")
has_digit = False
for char in input_str:
    if char.isnumeric():
        has_digit = True
        break
first_valid = input_str[0].isnumeric() or input_str[0] == '-'
rest_valid = input_str[1:].isnumeric() or input_str[1:] == ""
if not (has_digit and first_valid and rest_valid):
    print("Data validation failed!")
    sys.exit()
number = int(input_str)
print('Twice the input number is:', number * 2)
