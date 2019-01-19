class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        period = 2 * numRows - 2
        index_map = {}
        for i in range(period):
            if i < numRows:
                index_map[i] = i
            else:
                index_map[i] = period - i

        rows = []
        for i in range(numRows):
            rows.append([''])

        for i in range(len(s)):
            rows[index_map[i%period]][0] += s[i]

        result = ''
        for i in range(numRows):
            result += rows[i][0]

        return result
