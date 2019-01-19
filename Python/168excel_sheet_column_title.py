class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
            result = chr(65 + (n - 1) % 26) + result
            n = (n -1) // 26
        return result
