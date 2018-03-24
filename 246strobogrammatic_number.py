class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        map = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        n = len(num)
        for i in range(n//2+1):
            if (num[i], num[-i-1]) not in map:
                return False
        return True
