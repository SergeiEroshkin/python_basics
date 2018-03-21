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
print factorial(1)
print factorial(2)
print factorial(0)
print factorial('string')
