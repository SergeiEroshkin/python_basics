def factorial(n):
    if n < 0:
        print 'Factorial does not exist for negative numbers'
        return
    if n == 1 or n == 0:
        return 1
    total = 1
    if type(n) == int:
        while n > 1:
            total *= n
            n -= 1
        return total
    else:
        return 'Invalid input: "{0}"'.format(n)


# Test Data
print factorial(1)
print factorial(4)
print factorial(0)
print factorial('string')
print factorial(-2)
