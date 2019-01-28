class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        layers = (n + 1) // 2
        result = [[0 for _ in range(n)] for _ in range(n)]

        num = 1
        for l in range(layers):
            # top
            for i in range(l, n-l-1):
                result[l][i] = num
                num += 1
            # right
            for i in range(l, n-l-1):
                result[i][n-l-1] = num
                num += 1
            # bottom
            for i in range(n-l-1, l, -1):
                result[n-l-1][i] = num
                num += 1
            # left
            for i in range(n-l-1, l, -1):
                result[i][l] = num
                num += 1

        if n % 2 == 1:
            result[n//2][n//2] = num

        return result
