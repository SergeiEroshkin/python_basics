def factorial(n):
    """
    Function to count Factorial n
    :param n:
    :return: Factorial n
    """
    total = 1
    if n == 1:
        return total
    if type(n) == int and n:
        return n * factorial(n-1)
    else:
        return 'You input is %s' % n



# Test Data
print factorial(5)
print factorial(1)
print factorial(0)
print factorial('string')
print factorial(2.0)
