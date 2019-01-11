def fib(number):
    """
    Function to get fibonacci sequence
    :param : integer
    :return: fibonacci sequence from 1 to number defined by user
    """
    if number == 0:
        return 0
    fib_list = []
    a, b = 1, 0
    for num in range(number+1):
        a, b = b, a + b
        fib_list.append(a)
    return fib_list


print fib(12)


def fibo(n):
    """
    :param n: integer
    :return: Value of Nth number in Fibonacci sequence
    """
    a, b = 1, 0
    for item in range(n+1):
        a, b = b, a+b
    return a


print fibo(12)


def fib_rec(n):
    """
    :param n: Integer
    :return: fib
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


print fib_rec(12)