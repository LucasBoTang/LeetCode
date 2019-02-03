class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]:
                break
            table[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j]:
                break
            table[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    table[i][j] = 0
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]

        return table[-1][-1]
