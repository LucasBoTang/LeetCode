class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i, result = 1, num
        while i <= num:
            result ^= i
            i <<= 1
        return result
