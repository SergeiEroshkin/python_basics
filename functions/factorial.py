def factorial(n):
    """
    Function to count Factorial n
    :param n:
    :return: Factorial n
    """
    total = 1
    if type(n) == int and n > 0:
        while n > 1:
            total *= n
            n -= 1
    else:
        print 'Invalid input'
    return total
print factorial(5)