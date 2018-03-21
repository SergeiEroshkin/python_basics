def max_profit(prices):
    """
    :param prices: List of integers
    :return: Max profit can be earned
    """
    # Lets assume that first price is lowest price
    lowest = prices[0]
    max_pro = 0
    # Lets iterate through prices and skip index 0
    for price in prices[1:]:
        # Check if current stock price in lowest
        if price < lowest:
            lowest = price
        # Compare current max profit with (price - lowest)
        if max_pro < price - lowest:
            max_pro = price - lowest
        else:
            continue
    return max_pro


stockPrice = [50, 60, 200, 40, 180, 90, 10]
print max_profit(stockPrice)

