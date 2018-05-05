class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            carry = (a & b) << 1
            a = (a ^ b) % 0x100000000
            b = carry % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
