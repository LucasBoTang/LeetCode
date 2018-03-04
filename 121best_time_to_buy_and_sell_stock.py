class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, profit = prices[0], 0
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i]-buy)
        return profit
