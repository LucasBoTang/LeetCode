class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n < 1:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True
