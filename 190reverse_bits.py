class Solution:
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bin = bin(n)[2:]
        n_bin = '0' * (32 - len(n_bin)) + n_bin
        result = int(n_bin[::-1], 2)
        return result
