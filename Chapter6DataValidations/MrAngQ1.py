while True:
    s = input('Enter an integer:')
    def containsalpha(string):
        for char in string:
            if char.isalpha():
                return True
        return False
    
    if containsalpha(s):
        print('The input is should not contain any alphabet!')
    elif s.isnumeric() or (s[0] == '-' and s[1:].isnumeric()) or float(s) == int(float(s)):
        print('Data accepted!')
    else:
        print('The input is invalid!')
        
