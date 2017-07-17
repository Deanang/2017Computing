is_valid = False
while not is_valid:
    input_str = input('Enter a phone number: ')
    is_valid = len(input_str) == 9 and input_str[:4].isnumeric() \
    and input_str[4] == '-' and input_str[5:].isnumeric()
