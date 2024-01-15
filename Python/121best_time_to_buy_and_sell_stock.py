class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # init max profit
        max_profit = 0
        # init min price
        min_price = prices[0]
        for p in prices[1:]:
            # get min prices to buy a stock
            min_price = min(min_price, p)
           # sell stock with lowest buying price
            max_profit = max(max_profit, p - min_price)
        return max_profit
