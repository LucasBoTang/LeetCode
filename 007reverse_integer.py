class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        if x > 0:
            while x:
                y = 10 * y + x % 10
                x //= 10
        elif x < 0:
            x = -x
            while x:
                y = 10 * y + x % 10
                x //= 10
            y = -y
        else:
            y = 0
        if abs(y) > 0x7fffffff:
            return 0
        return y
