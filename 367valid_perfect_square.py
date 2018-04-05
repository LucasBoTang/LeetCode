class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 0, num
        while start <= end:
            mid = start + (end - start) // 2
            mid_2 = mid ** 2
            if mid_2 == num:
                return True
            if mid_2 > num:
                end = mid - 1
            if mid_2 < num:
                start = mid + 1
        return False
