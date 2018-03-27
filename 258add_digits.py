class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # digital root
        while num == 0:
            return 0
        return (num - 1) % 9 + 1
