def factorial(n):
    """
    Function to count Factorial n
    :param n:
    :return: Factorial n
    """
    if n < 0:
        print 'Factorial does not exist for negative numbers'
        return
    if n == 1 or n == 0:
        return 1
    if isinstance(n, int):
        return n * factorial(n-1)
    else:
        print 'Invalid input: "{0}"'.format(n)


def main():
    print factorial(4)
    print factorial(1)
    print factorial(0)
    print factorial('string')
    print factorial(2.0)
    print factorial(-2)


if __name__ == '__main__':
    main()
