class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        result = ''
        hexmap = '0123456789abcdef'
        while num < 0:
            num += 16 ** 8
        while num:
            result += hexmap[num % 16]
            num //= 16
        return result[::-1]
