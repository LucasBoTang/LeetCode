 class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # init min price
        min_price = prices[0]
        # init max profit
        max_profit = 0
        # selling
        for p in prices:
            min_price = min(min_price, p)
            profit = p - min_price
            max_profit = max(max_profit, profit)
        return max_profit
