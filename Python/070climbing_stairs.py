class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # init ways from 1 step
        prev_ways, cur_ways = 1, 1
        # climb to the top
        for _ in range(n - 1):
            prev_ways, cur_ways = cur_ways, prev_ways + cur_ways
        return cur_ways
