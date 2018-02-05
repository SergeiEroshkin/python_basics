def factorial(n):
    """
    Function to count Factorial n
    :param n:
    :return: Factorial n
    """
    if n == 1:
        return 1
    else:
        if type(n) == int and n > 1:
            return n * factorial(n-1)
        else:
            return 'Your input is: %s' % n


# Test Data
print factorial(5)
print factorial(1)
print factorial(0)
print factorial('string')
print factorial(2.0)
