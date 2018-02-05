def fib(number):
    """
    Function to get fibonacci sequence
    :param : integer
    :return: fibonacci sequence from 1 to number defined by user
    """
    fib_list = list()
    a, b = 1, 1
    for i in range(number):
        a, b = b, a+b
        fib_list.append(a)
    return fib_list


print fib(12)


def fibo(n):
    """
    :param n: integer
    :return: Value of Nth number in Fibonacci sequence
    """
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return 'Number is: ' + str(a)


print fibo(12)
