while True:
    s = input('Enter an integer:')
    if int(float(s[1:]))==float(s[1:]):
        break
    else:
        print('The input is invalid!')
print('Data accepted!')
