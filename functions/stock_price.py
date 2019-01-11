def max_profit(prices):
    """
    :param prices: List of integers
    :return: Max profit can be earned
    """
    # Lets assume that first price is lowest price
    lowest_price = prices[0]
    # Set Max Profit value = 0
    max_profit = 0
    for price in prices[1:]:
        if price < lowest_price:
            lowest_price = price
        max_profit = max(max_profit, price - lowest_price)
    return max_profit


stockPrice = [50, 60, 200, 40, 180, 90, 10]
print max_profit(stockPrice)