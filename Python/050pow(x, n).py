class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1

        if n < 0:
            n = -n
            x = 1 / x

        while n:
            if n % 2 == 1:
                result *= x
            n //= 2
            x *= x

        return result
