def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    min_buy = prices[0]
    for index in range(1, len(prices)):
        if prices[index] - min_buy > max_profit:
            max_profit = prices[index] - min_buy
        if prices[index] < min_buy:
            min_buy = prices[index]
    return max_profit

print(max_profit([7,6,4,3,1,9]))
