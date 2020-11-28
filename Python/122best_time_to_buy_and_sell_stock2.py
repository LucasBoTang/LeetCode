class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit
