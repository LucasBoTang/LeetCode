class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        i = 0
        while i * i <= c:
            a2 = i * i
            b2 = c - a2
            if (b2 ** 0.5).is_integer():
                return True
            i += 1

        return False
