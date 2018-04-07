class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, length, size = 1, 1, 9
        while n > length * size:
            n -= length * size
            start, length, size = start * 10, length + 1, size * 10
        num = start + (n - 1) // length
        pos = (n - 1) % length
        return int(str(num)[pos])
