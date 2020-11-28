class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        while not triangle:
            return 0
        n = len(triangle)
        for i in range(n+1):
            for j in range(n-i-1):
                triangle[n-i-2][j] =  triangle[n-i-2][j] + min(triangle[n-i-1][j], triangle[n-i-1][j+1])
        return triangle[0][0]
