while True:
    s = input('Enter an integer:')
    if s.isnumeric() or (s[0]=='-' and s[1:].isnumeric):
        break
    else:
        print('The input is invalid!')

print('Data accepted!')
