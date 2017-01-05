def fib(number):
    """
    Function to get fibonacci sequence in list format
    :param number: integer
    :return: list
    """
    fib_list = list()
    a, b = 0, 1
    fib_list.insert(a, a)
    fib_list.insert(b, b)
    while b < number:
        a, b = b, a + b
        fib_list.append(b)
    return fib_list


print fib(20)
print fib.__doc__


def fib(n):
    """

    :param n: integer
    :return: fib number position = integer
    """
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print fib(8)