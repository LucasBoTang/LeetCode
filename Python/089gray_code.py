class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]

        for i in range(1,n+1):
            new = [code + 2 ** (i - 1) for code in result][::-1]
            result += new

        return result
