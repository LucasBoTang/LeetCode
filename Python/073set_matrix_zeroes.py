class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void (Do not return anything, modify matrix in-place instead.)
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for r in range(m):
                        if matrix[r][j] != 0:
                            matrix[r][j] = 'i'
                    for c in range(n):
                        if matrix[i][c] != 0:
                            matrix[i][c] = 'i'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'i':
                    matrix[i][j] = 0
