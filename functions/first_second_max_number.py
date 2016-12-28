def second_max(array):
    """
    Find first and second max number in array
    :param array: Input array
    :return: First and second max number
    """
    max1, max2 = float('-inf'), float('-inf')
    for item in array:
        if item > max2:
            if item >= max1:
                max1, max2 = item, max1
            else:
                max2 = item
    print 'First maximum:', max1
    print 'Second maximum:', max2

array1 = [0, 1, 2, 3, 4]
second_max(array1)