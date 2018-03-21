def fib(number):
    """
    Function to get fibonacci sequence
    :param : integer
    :return: fibonacci sequence from 1 to number defined by user
    """
    my_dict = {}
    a, b = 1, 0
    counter = 1
    for i in range(number):
        a, b = b, a+b
        my_dict[counter] = str(a) * counter
        print my_dict[counter]
        counter += 1


fib(6)
