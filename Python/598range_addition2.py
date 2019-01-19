class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        x_min = m
        y_min = n
        for op in ops:
            x_min = min(x_min, op[0])
            y_min = min(y_min, op[1])
        return x_min * y_min
