class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        cur = n % 2
        n //= 2

        while n:
            prev, cur = cur, n % 2
            if not prev ^ cur:
                return False
            n //= 2

        return True
