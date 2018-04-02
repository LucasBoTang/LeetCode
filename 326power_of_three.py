class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while not n:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

        # while n <= 0:
        #     return False
        # return 1162261467 % n == 0
