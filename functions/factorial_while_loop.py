def factorial(n):
    if n == 1:
        return 1
    counter = 1
    if type(n) == int and n:
        while n > 1:
            counter *= n
            n -= 1
        return counter
    else:
        return 'Invalid input %s' % n



# Test Data

a = 1
b = 2
c = 0
d = 'string'
print factorial(a)
print factorial(b)
print factorial(c)
print factorial(d)