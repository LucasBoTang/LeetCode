class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        pascal = [[1]]
        row = 1
        while row != numRows:
            cur = pascal[-1]
            tmp = [1]
            for i in range(row-1):
                tmp.append(cur[i]+cur[i+1])
            tmp.append(1)
            pascal.append(tmp)
            row += 1
        return pascal   
