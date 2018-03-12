class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for char in s:
            result = 26 * result + ord(char) - 64
        return result
