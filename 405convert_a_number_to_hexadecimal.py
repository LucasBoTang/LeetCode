class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        result = ''
        hexmap = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.split()
        while num < 0:
            num += 16 ** 8
        while num:
            result += hexmap[num % 16]
            num //= 16
        return result[::-1]
