class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        while not n or not k:
            return 0
        a, b = k, k ** 2
        for _ in range(n - 1):
            a, b = b, (k - 1) * (a + b)
        return a
