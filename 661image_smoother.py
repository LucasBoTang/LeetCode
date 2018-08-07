class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        r, c = len(M), len(M[0])
        neighbors = [-1, 0, 1]

        result = []
        for i in range(r):
            result.append([0] * c)

        for i in range(r):
            for j in range(c):
                temp = []
                for nr in neighbors:
                    if i + nr >= 0 and i + nr < r:
                        for nc in neighbors:
                            if j + nc >= 0 and j + nc < c:
                                temp.append(M[i+nr][j+nc])
                result[i][j] = sum(temp) // len(temp)

        return result
