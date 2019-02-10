class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        table = [[0] * n for _ in range(m)]

        table[0][0] = grid[0][0]

        for i in range(1, m):
            table[i][0] = table[i-1][0] + grid[i][0]

        for j in range(1, n):
            table[0][j] = table[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = min(table[i-1][j], table[i][j-1]) + grid[i][j]

        return table[-1][-1]
