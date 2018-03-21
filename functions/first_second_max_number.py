def second_max(array):
    """
    Find first and second max number in array
    :param array: Input array
    :return: First and second max number
    """
    max1, max2 = float('-inf'), float('-inf')
    for number in array:
        if number > max2:
            if number > max1:
                max2, max1 = max1, number
        else:
            max2 = number
    print 'First number is %s, Second number %s.' % (max1, max2)


array1 = [0, 1, 2, 3, 4, 4, 5, 5, 5]
second_max(array1)