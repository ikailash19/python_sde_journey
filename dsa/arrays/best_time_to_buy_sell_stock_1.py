def best_time_to_buy_sell_stock_1(prices):
    max_profit = 0
    buy = 0
    sell = 1
    while (sell < len(prices)):
        if prices[buy] > prices[sell]:
            buy = sell
            sell += 1
            continue
        transaction = prices[sell] - prices[buy]
        if transaction > max_profit:
            max_profit = transaction
        sell += 1

    return max_profit

print(best_time_to_buy_sell_stock_1([7,1,5,3,6,4]))