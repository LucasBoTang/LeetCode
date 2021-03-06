class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
