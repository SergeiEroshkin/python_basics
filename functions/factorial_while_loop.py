def factorial(n):
    if n == 1:
        return 1
    counter = 1
    while n > 1:
        counter *= n
        n -= 1
    return counter


# Test Data

a = 1
b = 10
c = 0
print factorial(a)
print factorial(b)
print factorial(c)