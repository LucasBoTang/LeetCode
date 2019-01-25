class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])
        layers = (min(m, n) + 1) // 2

        # iterate for each layers
        for l in range(layers):
            # top
            for i in range(l, n-l):
                result.append(matrix[l][i])
            # right
            for i in range(l+1, m-l):
                result.append(matrix[i][n-l-1])
            # bottom
            if l < m - l - 1:
                for i in range(n-l-2, l, -1):
                    result.append(matrix[m-l-1][i])
            # right
            if l < n - l - 1:
                for i in range(m-l-1, l, -1):
                    result.append(matrix[i][l])

        return result
