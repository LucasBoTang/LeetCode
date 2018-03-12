class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n // 5
            n //= 5
        return result
