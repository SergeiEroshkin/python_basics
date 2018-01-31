def average_num(heights):
    """
    :param heights: Input string
    :return: Average number in string
    """
    return sum(map(int, heights.split())) / float(len(heights.split()))


heights = '1 2 3 4 5 6 7 8'
print average_num(heights)
