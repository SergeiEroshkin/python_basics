def is_fib(n):
    """
    :param n: integer
    :return: True if n belongs to Fibonacci sequence or False if not
    """
    a, b = 1, 0
    for item in range(n):
        a, b = b, a+b
        if a == n:
            return True
        else:
            continue
    return False


print is_fib(55)
print is_fib(54)
print is_fib(987)
