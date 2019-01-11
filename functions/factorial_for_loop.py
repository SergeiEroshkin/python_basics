def factorial(n):
    total = 1
    if not isinstance(n, int):
        print 'Wrong data type send {0}'.format(type(n))
        return
    if n < 0:
        print 'Factorial for negative numbers does not exist'
        return
    if n == 0 or n == 1:
        return 1
    for integer in range(2, n + 1):
        total *= integer
    return total


print factorial(1)
print factorial(4)
print factorial(0)
print factorial(1.0)
print factorial('string')
print factorial(-2)
