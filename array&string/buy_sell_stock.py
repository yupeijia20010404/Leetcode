def maxProfit1(prices):
    buy = 0
    sell = 1
    profit = 0
    while sell < len(prices):
        if prices[sell] < prices[buy]:
            buy = sell
            sell = buy + 1
        else:
            profit = max(profit, prices[sell] - prices[buy])
            sell += 1
    return profit

def maxProfit2(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit