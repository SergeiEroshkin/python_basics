def fib(number):
    """
    Function to get fibonacci sequence in list format
    :param number: integer
    :return: list
    """
    fib_list = list()
    a, b = 0, 1
    fib_list.insert(a, a)
    while b < number:
        a, b = b, a + b
        fib_list.append(b)
    return fib_list

print fib(6)
print fib.__doc__
