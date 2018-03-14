def max_profit(my_list):
    """
    :param my_list: List of integers
    :return: Max profit can be earned
    """
    lowest = my_list[0]
    max_pro = 0
    for price in my_list:
        if price < lowest:
            lowest = price
        max_pro = max(max_pro, price - lowest)
        print max_pro
    return max_pro


stockPrice = [80, 60, 140, 170, 90, 10]
max_profit(stockPrice)

