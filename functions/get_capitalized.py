def capitalize(string):
    return ' '.join((word.capitalize() for word in string.split(' ')))

a = 'alan weber'
b = '1lan 2eber'
print capitalize(a)
print capitalize(b)
