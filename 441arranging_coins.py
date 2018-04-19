class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1
