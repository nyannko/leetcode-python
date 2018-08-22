class Solution(object):

    def max_profit(self, prices):
        if not prices:
            return 0
        profit = 0
        curr_min = prices[0]
        for i, price in enumerate(prices):
            if i < 1: continue
            profit = max(profit, price - curr_min)
            curr_min = min(curr_min, price)
        return profit

    def max_profit_II(self, prices):
        sum = 0
        for i, price in enumerate(prices):
            if i < 1: continue
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                sum += diff
            i += 1
        return sum
