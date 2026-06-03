def best_time_buy_sell_stock(prices):
    left = 0
    max_profit = 0
    right = 1
    while right < len(prices):
        if (prices[right] < prices[left]):
            left = right
        else:
            transaction = prices[right] - prices[left]
            max_profit = max(transaction, max_profit)
        right += 1
    return max_profit
print(best_time_buy_sell_stock([7,1,5,3,6,4]))